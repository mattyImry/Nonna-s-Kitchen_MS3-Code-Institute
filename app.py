import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# CONFIGURATION

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    """
    Landing page.
    4 recipes can be viewed,
    by clicking the card the
    full recipe will be displayed.
    """
    # idea & code for pagination  taken from
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes
    # pagination

    recipes_per_page = 4

    current_page = int(request.args.get('current_page', 1))

    recipes = mongo.db.recipes.find().skip(
        (current_page - 1)*recipes_per_page).sort(
            '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*recipes_per_page).limit(recipes_per_page)

    number_recipes = recipes.count()

    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)

    return render_template(
        "index.html", recipes=recipes,
        current_page=current_page, pages=pages,
        recipes_per_page=recipes_per_page,
        number_recipes=number_recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Searching the database with the use
    of searchbar in landing page
    A number of recipe will be displayed and paginated
    depending of the search made by user
    """

    # idea & code for pagination  taken from
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes
    # pagination

    recipes_per_page = 4
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        query = request.form.get("query")
    else:
        query = request.args.get("query")

    sort_by = "Sort by"

    recipes = mongo.db.recipes.find(
        {"$text": {"$search": str(
            query)}}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*recipes_per_page).limit(recipes_per_page)

    number_recipes = recipes.count()

    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)

    return render_template(
        "index.html", recipes=recipes,
        current_page=current_page, pages=pages,
        recipes_per_page=recipes_per_page,
        number_recipes=number_recipes,
        query=query, sort_by=sort_by)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user. Before registering the
    username is checked to see if the same
    one already exist.
    If registration is complete
    the user is logged in.

    """
    if request.method == "POST":
        # checking of users exist in database
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry Username already exist, try again")
            return render_template("register.html")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thank you! You are now registered")
        return redirect(url_for("myprofile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in the user after checkhing
    the username and password.
    In case of mistaken username or
    password the user won't know
    which is the wrong entry
    to avoid force entry
    """
    if request.method == "POST":
        # check if username exist in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if password match user
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                # if username and password match create session cookie
                session["user"] = request.form.get("username").lower()
                flash("Welcome back {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "myprofile", username=session["user"]))
            else:
                # password no matched
                flash("Incorrect Username or password")
                return redirect(url_for("login"))

        else:
            # user no matched
            flash("Incorrect Username/password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/myprofile/<username>", methods=["GET", "POST"])
def myprofile(username):
    """
    Display user profile with
    recipes created by user
    Only when user is logged in
    can view its profile
    """

    # session user's username form database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # idea & code for pagination  taken from
    # https://github.com/Sean-Mc-Mahon/McTasticRecipes

    # pagination for user's profile

    user_recipes = mongo.db.recipes.find({"author": username})
    number_of_user_rec = user_recipes.count()
    recipes_per_page = 4

    current_page = int(request.args.get('current_page', 1))

    recipes = user_recipes.sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1) * recipes_per_page).limit(recipes_per_page)

    number_recipes = recipes.count()
    pages = range(1, int(math.ceil(number_recipes / recipes_per_page)) + 1)

    user_number_of_recipes = mongo.db.recipes.count({"author": username})

    if session["user"]:
        return render_template(
            "myprofile.html", username=username,
            user_number_of_recipes=user_number_of_recipes,
            recipes=recipes, current_page=current_page,
            pages=pages, number_recipes=number_recipes,
            recipes_per_page=recipes_per_page,
            user_recipes=user_recipes,
            number_of_user_rec=number_of_user_rec)

    return redirect(url_for("login"))


@app.route("/delete_user/<username>")
def delete_user(username):
    """
    The user can delete
    its own account and
    recipes created when
    logged in.
    """

    mongo.db.users.remove({"username": username})
    mongo.db.recipes.remove({"author": username})
    flash("Profile removed succesfully")

    # delete user from session cookie.
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    """
    Log out the user from session
    redirect the user to
    index page
    """

    flash("You are now logged out")

    # delete user from session cookie.
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Add recipe to the database
    after filling the form completely
    """

    if request.method == "POST":

        # help from tutor team to write code
        # for splittin ingredients and preparetion

        ingredients = request.form.get("ingredients").split(",")
        preparation = request.form.get("preparation").split(".")

        recipe = {
            "type": request.form.get("type"),
            "recipe_name": request.form.get("recipe_name"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "ingredients": ingredients,
            "preparation": preparation,
            "is_vegetarian": request.form.get("is_vegetarian"),
            "author": session["user"],
            "image": request.form.get("image")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Succesfully!")
        return redirect(url_for("index"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Function to edit the recipe.
    Only the user that created
    the recipe and admin
    can use edit button
    """
    if request.method == "POST":

        # help from tutor team to write code
        # for splitting ingredients and preparetion

        ingredients = request.form.get("ingredients").split(",")
        preparation = request.form.get("preparation").split(".")

        submit = {
            "type": request.form.get("type"),
            "recipe_name": request.form.get("recipe_name"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serving": request.form.get("serving"),
            "ingredients": ingredients,
            "preparation": preparation,
            "is_vegetarian": request.form.get("is_vegetarian"),
            "author": session["user"],
            "image": request.form.get("image")
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        username = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})["author"]

        flash("Recipe Succesfully Updated!")
        return render_template(
            "single_recipe.html", recipe=recipe, username=username)

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    User when logged in or admin can
    delete recipe from database
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted succesfully!")
    return redirect(url_for("index"))


@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    """
    View the full description
    of recipe when clicking card
    on landing page
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})["author"]

    return render_template(
        "single_recipe.html", recipe=recipe, username=username,)


@app.route("/contact_us")
def contact_us():
    """
    Contact page for any user to be
    able to send email to developer.
    Also a confirmation email is sent to
    user after filling the form
    correctly
    """
    return render_template("contact_us.html")


@app.errorhandler(404)
def error_handler_404(error):
    """
    In case of page not found
    display error 404
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def error_handler_500(error):
    """
    In case of internal error
    display error 500
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
