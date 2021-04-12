# **_Nonna's Kitchen_**

This project is my third Milestone Project for the [Code Institute](https://codeinstitute.net/) Fullstack Web Developer Diploma. This project is created to demonstate my ability to design and implement back-end functionality with the use of [Python3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/). Data is stored in [MongoDB](https://www.mongodb.com/) a document-base database. I will be following the CRUD principles Create, Read, Update and Delete. With this priciples I can allow the User to store and manipulate his recipes in the database.
The deployed application can be accessed here "ADD LINK"  

## **_UX_**  
### **_Strategy / Site Owner story_**

I have design this website to allow the User to create and save recipes. The main Users will be people that love cooking and like to try new recipes. The Users can come to the website anytime to view the recipes written by themselves or by other users. Without registering the casual User can only view other Users' recipes. If the User decides to register will be able to create, store, modify and delete his own recipes, basically creating his own recipe book. There will be also an Admin functionality only for maintenance purposes. I have also created this website, as for the Developer I can collect other's Users recipes and try them myself. The main type of recipes created by the Developer will be Italian but any other type of cusine is welcome.  

#### **_Data schema_**
The data is stored by using [MongoDB](https://www.mongodb.com/). The documents stored in collections in MongoDB are more flexible than SQL databases. Documents can be modified also during the development. I have created two collections. The first one is collection "recipes". This collection holds all the informations needed to prepare the recipes. Click [here](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/media/database_recipes.jpg) to view a screenshot of the recipes collection.  
The second one is collection "Users". This collection will hold the username of the User and a password. Click [here](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/media/database_users.jpg) to view a screenshot of the users collection.  
The connection between the two collections is achived by the `key` "author" stored in the recipes collection which is the same as the `key` "username" in the users. This key will guarantee that every recipe created will be only connected to the user that created it.

#### **_Security_**
Due to the possibility on the website to register and being able to store information security features are implemented. By using [Flask](https://flask.palletsprojects.com/en/1.1.x/)  I will implement Password Hashing and salting with the use of Flask dependence called Werkzeug. Password hashing algorithm is supplied by Werkzeug  and the function is to mask the password inserted by the user during registration, so that can be stored safely in a database. Defensive programing will also be used during the production process.
To protect password and sensible information for MongoDB and Flask a file called env.py has been created. 


### **_Scope_**

Features that I want to implement are:

*  CRUD operations to allow Users to interact with the application.  
*  Ability for the User and developer to create a recipe
*  Ability for the User and developer read a recipe
*  Ability for the User and developer update a recipe
*  Ability for the User and developer delete a recipe
*  Ability for the Users and developer register an account.
*  Ability for the Users and developer to search recipes.
*  Ability for the Users to contact the Developer with EmailJs functionality.
*  Ability for the Admin to delete recipes and accouts.
*  Easy design and navigation.
*  Mobile first design.

### **_Structure_**

* The recipes will be categorised and stored in three main courses type: first course, main course and dessert.  
 
* A list of all recipes stored in the website will be shown to all the Users in the main page. 

* The Users will be able to view all the recipes that they have created via "My profile" page.




### **_Skeleton_**

* The recipes will be presented with all the informations needed for the preparation on a card style format for easy navigation. 

* To add the recipes to the website a minimalistic style form will be use.  

* A search function will be present for all the Users, logged in or not, in the main page to search the recipes database.

* A search function will be present in the profile page. The profile page will only be visible when the user is logged in.

* The Users can use the Navigation bar to navigate the different pages within the website.

* The collection of all recipes will be visible in a card style format in the index page.

* In the User's profile page, the recipes created by the user will be visible in a card style format.

* On the footer a link for directing the Users to the contact page will always be present.

* On the footer two links will be present to redirect the Users to the developer LinkedIn acoount and GitHub account.

* The logo and "Home" link in the Navigation bar will redirect the Users to the main page.

* The contact page will hold a from to contact the developer.


### **_Surface_**

The website uses [Materialize](https://materializecss.com/) as a framework. I have decided to use it because of the classic design that many users today are expecting from any website. 
The pages will looks like they are compose by cards. 
The color scheme is very minimal with these colors used:  
* #3e2723 is used for title's texts and borders for buttons and cards.
* #d7ccc8 is used for texts
* #a1887f is used for the navbar anf footer.
* text shadow is also used for the navbar elements
* #448aff is used for footer icons and icons in all pages.

The fonts choosen are from [Google Fonts](https://fonts.google.com/).
Font "Princess Sofia" has been used for main titles and logo.
Font "Raleway" has been used for text in paragraphs, messages and smaller titles.

## **_Wireframes_**

Link to Wireframes folder: [Wireframes](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/wireframes/nonna_%20kitchen-%20wireframes.pdf)


During the planning stage I have created a log out page as seen in the Wireframes. After consulting with my mentor I was advise that it was a better user experience if the User logs out to be redirected to the main page as a users logged out. This is because if the user logs out has probably completed whats intended and can leave the website. If the user logged out by mistake the log in link is present in the navbar. I agree with the point made and I have modified the Wireframes.  
The wireframe for the  single page is not the same as the finished page because during the development of the page I prefered to have a bigger picture of the recipe instead of a small one with the writings floating on the right.

## **_User Story_**

* As a User not registered I want to be able to Register my account.
* As a User not registered I want to be able to view all recipes created in the website.
* As a User not registered I want to be able to contact the developer by usign the contact page form.
* As a User registered I want to be able to log in to the website.
* As a User logged in I want to be able to add recipes.
* As a User logged in I want to be able to view my recipe and others.
* As a User logged in I want to be able to edit my recipe.
* As a User logged in I want to be able to delete my recipe.
* As a User logged in I want to be able to delete my account.
* As a User logged in I want to be able to log out.
* As a User logged in I want to be able to contact the developer by usign the contact page form.
* As the Developer I want to be able to view all Users recipes.
* As the Admin I want to be able to delete recipes and accounts.

## **_Features_**

### **_Existing Features_**

* The navbar has a logo on the left hand corner and the "Home" link that when clicked will direct the User to the main page showing all recipe present in the website. The navbar will show different links depending if the user is logged in or not.  
If the user is logged in the links available will be:
"Home", "My Profile", "Add Recipe", "Log Out", "Contact Us".  
If the user is not logged in the links visible will be:
"Home", "Log In", "Register", "Contact Us".
On the mobile view the navbar will be showing the logo on the left hand side but the links will be hold in a burger menu rapresented by an arrow pointing down.

* The website is visible in all screen sizes.
* The footer will only hold the contact page link via a letter icon and two icons redirect the Users to the developer LinkedIn acoount and GitHub account.
* The unregistered Users can register an account via the "Register" page.
* The register User can log in via the log in link in the navbar.
* The User can log out via the log out link in the navbar.
* Any visitor to the website can contact the developer via the contact form in the "Contact us" page which uses [EailJS](https://www.emailjs.com/) .
* Any visitor to the website can search recipes via the search functionality in the "Index" page.
* The logged in User can add his own recipe via the "Add recipe" page. 
* The logged in User will be able to edit and delete his own recipes from "My profile" page and "Index" page.
* The logged in User will be able to edit and delete his own recipes from "Index" page only if lodded in.
* The logged in User will be able to edit his own recipes when recipe view via "Single recipe" page.
* The logged in User will be able to delete his own account from "My profile" page.
* The logged in User will be able to search recipes via the search functionality in the "My profile" page.
* All the information for the recipes and users will be stored by using [MongoDB](https://www.mongodb.com/). The informations will be retrieve and send with the use of [Python3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/).
* Pagination from [Flask](https://flask.palletsprojects.com/en/1.1.x/) is also implemented.



### **_Features to be implemented_**



## **_Bugs_**

* When adding the modal from Materialize I had a problem when deleting the recipe. The recipe deleted wasn't the one intended. I then discover that the modal needs a unique ID. By applying the `recipe._Id` to the id required by the modal, the recipe that gets deleted is now the correct one.

* When looking at the main page with all the recipes displayed, the second column doesn't have a recipe.  Click [here](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/media/bug_display_index_html.jpg) to view a screenshot of the recipes collection. When I have added pagination to the index.html page this issue has been solved.