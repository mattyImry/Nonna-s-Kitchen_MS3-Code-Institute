Python and Data Centric Development Milestone Project 3 - Code Institute

![Screenshotproject](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/2e5c67fc81a4db1b16a40d8e0b9e38d69461f289/media/ms3_screenshot.png)

# **_Nonna's Kitchen_**

This project is my third Milestone Project for the [Code Institute](https://codeinstitute.net/) Full Stack Software Developer Diploma. This project is created to demonstate my ability to design and implement back-end functionality with the use of [Python3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/). Data is stored in [MongoDB](https://www.mongodb.com/) a document-based database. I will be following the CRUD principles Create, Read, Update and Delete. With this priciples I can allow the User to store and manipulate his recipes in the database.
The deployed application can be accessed [here](https://nonna-kitchen-ms3.herokuapp.com/). 

## **_UX_**  
### **_Strategy / Site Owner story_**

I have designed this website to allow the User to create, read, update and delete recipes. The main Users will be people that love cooking and like to try new recipes. The Users can come to the website anytime to view the recipes written by themselves or by other users. Without registering, the casual User can only view other Users' recipes. If the User decides to register they will be able to create, store, modify and delete their own recipes, basically creating their own recipe book. There will be also an Admin functionality only for maintenance purposes. I have also created this website so that I can collect other Users' recipes and try them myself. The main type of recipes created by the Developer will be Italian but any other type of cuisine is welcome.  

#### **_Data schema_**
The data is stored by using [MongoDB](https://www.mongodb.com/). The documents stored in collections in MongoDB are more flexible than SQL databases. Documents can be modified also during the development. I have created two collections. The first one is collection "recipes". This collection holds all the information needed to prepare the recipes. Click [here](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/media/database_recipes.jpg) to view a screenshot of the recipes collection.  
The second one is collection "Users". This collection will hold the username of the User and a password. Click [here](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/master/media/database_users.jpg) to view a screenshot of the Users collection.  
The connection between the two collections is achived by the `key` "author" stored in the recipes collection which is the same as the `key` "username" in the users collection. This key will guarantee that every recipe created will be only connected to the user that created it.

#### **_Security_**
Due to the possibility on the website to register and being able to store information security features are implemented. By using [Flask](https://flask.palletsprojects.com/en/1.1.x/)  I will implement Password Hashing and salting with the use of Flask dependence called Werkzeug. Password hashing algorithm is supplied by Werkzeug  and the function is to mask the password inserted by the user during registration, so that can be stored safely in a database. Defensive programing will also be used during the production process.
To protect password and sensible information for MongoDB and Flask a file called env.py has been created and visible only to the Developer. 


### **_Scope_**

Features that I want to implement are:

*  CRUD operations to allow Users to interact with the application.  
*  Ability for the User and developer to create a recipe
*  Ability for the User and developer to read a recipe
*  Ability for the User and developer to update a recipe
*  Ability for the User and developer to delete a recipe
*  Ability for the Users and developer to register an account.
*  Ability for the Users and developer to search recipes.
*  Ability for the Users to contact the Developer with EmailJs functionality.
*  Ability for the Admin to delete recipes.
*  Easy design and navigation.
*  Mobile first design.

### **_Structure_**

* The recipes will be categorised and stored in three main courses type: first course, main course and dessert.  
 
* A list of all recipes stored in the website will be shown to all the Users in the main page. 

* The Users will be able to view all the recipes that they have created via "My profile" page.
* A search function will allow Users to search recipes. To create the search functionality I have created an index in the database. This index is permanent and I have used the following `key` from the recipes collection to allow user search effectively: "recipe_name", "ingredients", "difficulty" and "type" which is the type of course.




### **_Skeleton_**

* The recipes will be presented with all the informations needed for the preparation in a card style format for easy visualization. 

* To add the recipes to the website a minimalistic style form will be used.  

* A search function will be present for all the Users, logged in or not, in the main page to search the recipes database.

* The Users can use the Navigation bar to navigate the different sections within the website.

* The collection of all recipes will be visible in a card style format in the index page.

* In the User's profile page, the recipes created by the user will be visible in a card style format.

* On the footer a link for directing the Users to the contact page will always be present.

* On the footer two links will be present to redirect the Users to the developer LinkedIn account and GitHub account.

* The logo and "Home" link in the Navigation bar will redirect the Users to the main page and will always be present.

* The contact page will hold a form to contact the developer.


### **_Surface_**

The website uses [Materialize](https://materializecss.com/) as a framework. I have decided to use it because of the classic design that many users today are expecting from any website and I will be able to achive mobile first design.
The pages will looks like they are composed by cards. 
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


During the planning stage I have created a log out page as seen in the Wireframes. After consulting with my mentor I was advised that it was a better user experience if the User was redirected to the main page as they logged out. This is because if the user logs out, he has probably completed what's intended and can leave the website. If the user logs out by mistake the log in link is present in the navbar. I agree with the point made and I have modified the Wireframes.  
The wireframe for the  single page is not the same as the finished page because during the development of the page I preferred to have a bigger picture of the recipe instead of a small one with the writings floating on the right.

## **_User Story_**

1. As a User not registered I want to be able to Register my account.
2. As a User not registered I want to be able to view all recipes created in the website.
3. As a User not registered I want to be able to contact the developer by usign the contact page form.
4. As a User registered I want to be able to log in to the website.
5. As a User logged in I want to be able to add recipes.
6. As a User logged in I want to be able to view my recipes and other users' recipes.
7. As a User logged in I want to be able to edit my recipes.
8. As a User logged in I want to be able to delete my recipes.
9. As a User logged in I want to be able to delete my account.
10. As a User logged in I want to be able to log out.
11. As a User logged in I want to be able to contact the developer by using the contact page form.
12. As the Developer I want to be able to view all Users recipes.
13. As the Admin I want to be able to delete recipes.

## **_Features_**

### **_Existing Features_**

* The navbar has a logo on the left hand corner and the "Home" link that when clicked will direct the User to the main page showing all recipes present on the website. The navbar will show different links depending if the user is logged in or not.  
If the user is logged in the links available will be:
"Home", "My Profile", "Add Recipe", "Log Out", "Contact Us".  
If the user is not logged in the links visible will be:
"Home", "Log In", "Register", "Contact Us".
On the mobile view the navbar will be showing the logo on the left hand side but the links will be held in a burger menu represented by an arrow pointing down.

* The website is visible in all screen sizes.
* The footer will only hold the contact page link via a letter icon and two icons redirect the Users to the developer LinkedIn account and GitHub account.
* The unregistered Users can register an account via the "Register" page.
* The register User can log in via the log in link in the navbar.
* The User can log out via the log out link in the navbar.
* Any visitor to the website can contact the developer via the contact form in the "Contact us" page which uses [EmailJS](https://www.emailjs.com/) . A reply via email to the user, to confirm the message sent, will also be received.
* Any visitor to the website can search recipes via the search functionality in the "Index" page.
* The logged in User can add his own recipe via the "Add recipe" page. 
* The logged in User will be able to edit and delete his own recipes from "My profile" page and "Index" page.
* The logged in User will be able to edit and delete his own recipes from "Index" page only if logged in.
* The logged in User will be able to edit his own recipes when recipe view via "Single recipe" page.
* The logged in User will be able to delete his own account from "My profile" page.
* All the information for the recipes and users will be stored by using [MongoDB](https://www.mongodb.com/). The informations will be retrieve and send with the use of [Python3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/).




### **_Features to be implemented_**
In the future I would like to be able to let the user download, share the recipes via social media and via email.
Also I would like to have the functionality to confirm registration via email, reset password if forgotten.


## **_Technology Used_**  

* [HTML](https://en.wikipedia.org/wiki/HTML) has been used in this project because is the standard markup language for documents designed to be displayed in a web browser.

* [CSS](https://en.wikipedia.org/wiki/CSS)
is a style sheet language. It is used to style markup language such as HTML.

* [Gitpod](https://gitpod.io) has been used as an on-line IDE followed by [Heroku](https://www.heroku.com/) for deployment. IDE is a software application used by computer programmers for software development.
* [Github](https://github.com/) has been used to store the code.

* [Googlefonts](https://fonts.google.com/) has been used to style the fonts of the writing on the web site.  
* [Fontawesome](https://fontawesome.com/) has been used for the icons used in the forms and footer.
* [Materialize](https://materializecss.com/) version 1.0.0 has been used a modern responsive front-end framework.

* [jQuery](https://jquery.com/) has been used to initialize Materialize functionality and to add current year to footer.
* [JavaScript](https://www.javascript.com/) has been used to be able to add the functionality for email service in contact page.
* [EmailJS](https://www.emailjs.com/) Has been used to be able to receive an email from the User to the developer with a request/message by filling the form in  the contact page. 
* [Python3](https://www.python.org/) is the programming language used mainly in this project.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a microframework used in conjunction with Python3.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is a modern and designer-friendly templating language for Python3.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) Werkzeug is a comprehensive WSGI web application library.
* [Mongo DB Atlas](https://account.mongodb.com/) is a NoSQL database used to store data.
* [Pymongo](https://pypi.org/project/pymongo/) is used to be able to interact with [Mongo DB Atlas](https://account.mongodb.com/) database.
* [Heroku](https://www.heroku.com/) is used to deploy and host the project.

## **_Testing_**

For the testing section please refer to [TESTING.md](TESTING.md) file.

## **_Bugs and fixes_**

* When adding the modal from Materialize I had a problem when deleting the recipe. The recipe deleted wasn't the one intended. I then discovered that the modal needs a unique ID. By applying the `recipe._Id` to the id required by the modal, the recipe that gets deleted is now the correct one.

* While testing emialjs even though the code was correct and the cache was cleared the functionality wasn't working. After a few hours it worked. I do believe I had a problem with cache not clearing properly.

* When opening the "Edit" page, the layout in the Edit form comes back with spaces and sentences not aligned. But when viewing the recipe in full, the layout of the recipe is correct. I do think it may be how Flask reopens the form. I will try to fix it when I have more time.

* In the main page when logged in the recipe cards leave spaces empty. This is due to the buttons appearing when logged in causing the card to be longer. I will try to have a fixed size card when I will have more time. When no one is logged in the cards are the layed out the expected way.

## **_Deployment_**

### **_Local deployment_**
1. To clone this repository you can do it directly into your IDE by copying the following to your terminal:  
  `git clone https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute `  
Or you can save a copy of this repository by clicking "Clone or download", then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have created for your repository).
3. Set environment variables:
* Create `env.py` in the root directory
* In the `env.py` file at the top write `import os`
* In the `env.py` set up the connection to your MongoDB database and a "SECRET KEY":  
`os.environ.setdefault("MONGO_URI", "mongodb+srv":("your username and password")`
`os.environ.setdefault["SECRET_KEY"] = "YourSecretKey"`
4. From the file requirements.txt install the requirements. In your terminal type:  
`pip3 install -r requirements.txt`  
Please make sure to add `sudo` if you are not using GitPod  
`sudo pip3 install -r requirements.txt`

5. Create an account if needed and a database in [Mongo DB Atlas](https://account.mongodb.com/)   

6. In my cluster I have named the database `recipes_manager`
7. In `recipes_manager` database create 2 collections:  
 Users:  
 `_id: <ObjectId>`  
 `username : <String>`  
 `password : <String>`  
 Recipes  
 `_id: <ObjectId>`   
 `type: <String>`   
 `recipe_name: <String>`  
 `difficulty: <String>`  
 `prep_time: <String>`  
 `cook_time: <String>`
 `serving: <String>`  
 `ingredients : <Array>`  
 `preparation : <Array>`  
 `is_vegetarian: <String>`  
 `author: <String>`  
 `image: <String>`

 8. To run the application type in your terminal:  
 `python3 run.py`

 Now you can start deploying to [Heroku](https://www.heroku.com/).

### **_Heroku deployment_**

1. Create a requirement.txt file that is need to Heroku to confirm dependences. In your terminal please type:  
`pip3 freeze --local > requirements.txt`
2. Create a Procfile to confirm to heroku apps the commands that are executed by the app.  
`echo web: python run.py > Procfile`
3. Add, commit and push these files to GitHub.
4. In Heroku create a new app. The name has to be unique.
5. In Heroku you need to link Github to Heroku via the dashboard link "Deploy".  
 Go to "Deployment method" and choose "GitHub".  
 Below Deployment method find you repository name listed and select it.  
 6. Still in Heroku go to "Settings" and click "Reveal Config Vars"
 7. In this section you need to fill in the inputs field with the variables written in the env.py file.  
    - **IP** : 0.0.0.0
    - **PORT** : 5000
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **MONGO_DBNAME** :`<your collection name>`
    - **DEBUG**: **FALSE**    
8. Then enable "Automatic deploys".
9. In "Manual Deployment" click "Deploy Branch".
10. You should get the message "Your app is succesfully deployed".
11. Click "View" to lunch the app.
 

## **_Credits_**

The recipes written by user "Matty", the developer, are taken from [Giallo Zafferano](https://www.giallozafferano.com/)  

The picture for the recipe "Stuffed Egg plant" is taken from [Freepik](https://www.freepik.com/free-photo/turkish-stuffed-eggplants-with-ground-beef-vegetables-baked-with-tomato-sauce_6933486.htm#page=1&query=stuffed%20eggplant&position=1) User Timolina  

The picture for the recipe "Spaghetti Carbonara" is taken from [Freepik](https://www.freepik.com/premium-photo/pasta-carbonara-with-bacon-parmesan_4255033.htm#page=1&query=carbonara&position=35) User Yuliyafurman 

The picture for the recipe "Cotechino" is taken from [Italian Tradition](https://www.italian-traditions.com/cotechino-with-lentils-typical-new-years-eve-dish/) User "Melania R." 

The picture for the recipe "Piadina" is taken from  [Giallo Zafferano](https://www.giallozafferano.com/recipes/piadina-romagnola-romagna-style-flat-bread.html)

Logo for favicom created with https://www.freelogodesign.org/   

Code for Footer at bottom of page [link](https://stackoverflow.com/questions/643879/css-to-make-html-page-footer-stay-at-bottom-of-the-page-with-a-minimum-height-b) 

Idea for current year on footer [link](https://forum.jquery.com/topic/get-current-year)

Flask documentation has been used extesively.   

Flask documentation for Error Handling.
I have also consulted this page for further information into Flask [link](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

The code for using the video as a background is taken from Udemy course "Advanced css and sass" and the video file is taken from [link](https://coverr.co/videos/slices-of-pizza-GaN4FTL01N).

The code for zooming the images of recipes is taken from [link](https://w3bits.com/css-image-hover-zoom/)

A special thanks goes to the tutoring team and to my mentor for the support given during the project.
