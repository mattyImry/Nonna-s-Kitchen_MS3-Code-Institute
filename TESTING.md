## **_Testing_**


### **_Browser compatibility_**
  
The project ahd been tested in the following browsers without any compatibility issue:  
* Google Chrome    
* Microsoft Edge  
* Firefox  
* Opera  

The project has also been tested on different screen sizes. 15" and 14" inch laptop, 24" screen and 20" screen.

### **_Responsiveness_**

As already specified in the "Surface" part in README file, the project has been developed with mobile first approach.

The project has been tested in mobile view in the following devices without any compatibility issue: 

* Motorola G5, G8 and G9
* Iphone 6
* Ipad 2

### **_Automated testing_**

* HTML pages tested with [W3C HTML Validator](https://validator.w3.org). I Had warning on regards sections that needed heading. Due to the fact that the heading was outside the section for layout reasons. Modified the position of the section nwarning removed.

* CSS file has been tested with [W3C CSS validator](https://jigsaw.w3.org/css-validator/). No errors.  

* JavaScript files has been tested with [Jshint](https://jshint.com/). No errors.  

    The followings warning has been shown for email.js file:

    One undefined variable : 8	emailjs

    One unused variable : 7	sendMail


    The followings warning has been shown for script.js file:  

    11	Missing '()' invoking a constructor.

* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools).  
I have tested the mobile and desktop versions of my project with Google Lighthouse. With good results.
Please refer to screen shots.  

    [mobile](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/a46dcd2e62d7a6bc2bd82621b4a956740bab8ea9/media/mobile_lighthouse.jpg) Screenshot  

    [desktop](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/a46dcd2e62d7a6bc2bd82621b4a956740bab8ea9/media/desktop_lighthouse.jpg) Screenshot.


### **_Manual testing_**

#### **_Nav bar_**

action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking the "Logo" | Redirected to index | Yes  
Clicking the "Home" link | Redirected to index | Yes  
Clicking the "My profile" link | Redirected to "My profile" page | Yes  
Clicking the "Add Recipe" link | Redirected to "Add Recipe" page | Yes  
Clicking the "Log in" link | Redirected to "Log in" page  |Yes  
Clicking the "Log out" link visible if user logged in| Redirected to "Index" page as user logged out |Yes  
Clicking the "Register" link | Redirected to "Register" page | Yes  
Clicking the "Contact us" link | Redirected to "Contact us" page | Yes  

#### **_Footer_**

action taken | expected result | functional 
------------ | --------------- | ---------
Clicking the icon "LinkedIn" | Redirected to developer LinkedIn profile| Yes  
Clicking the icon "GitHub" | Redirected to developer GitHub profile | Yes  
Clicking the icon "Evelope" | Redirected to "Contact us" page | Yes  

#### **_Home page_**

action taken | expected result | functional 
------------ | --------------- | ---------
Writing in the search bar "Main" | Shows only recipes that are Main Course. The bottom number and pagination show relevant pages and number of recipes | Yes
Writing in the search bar "Potato" | Shows only recipes that have "Potato" on title or as ingredient. The bottom number and pagination show relevant pages and numbers of recipes | Yes
Writing in the search bar "Sugar" | Shows only recipes that have "Sugar" on title or as ingredient. The bottom number and pagination show relevant pages and numbers of recipes | Yes
Writing in the search bar a word not present in recipes | Shows message "0 recipes No Recipe found" | Yes
Clicking the recipe's card | Redirected to recipe full page | Yes  
If User is not logged in | User can see recipes card not buttons | Yes
If User is not logged in clicking the recipe's card | Single page recipe will open | Yes
If User is logged in clicking the recipe's card | Single page recipe will open | Yes
If User is logged in | User can see recipes with buttons only for his own recipes | Yes
If User is logged in can delete recipe | Clicking the button delete confirmation via modal to delete | Yes
If User is logged in can edit recipe | Clicking the button edit | Yes
If Admin is not logged in clicking the recipe's card | Single page recipe will open | Yes
If Admin is logged in | Admin can see recipes with buttons | Yes
If Admin is logged in clicking the recipe's card | Single page recipe will open | Yes
If Admin is logged in can delete recipe | Clicking the button delete confirmation via modal to delete | Yes
If Admin is logged in can edit recipe | Clicking the button edit open edit recipe page| Yes

#### **_Single recipe page_**

action taken | expected result | functional 
------------ | --------------- | ---------
If User is logged in  | User can see buttons "Edit" "Cancel" at end of the recipe's page | Yes
If User is logged in clicking "Edit" button | Page to edit recipe's open | Yes
If User is logged in clicking cancel button | User redirected to index page | Yes
If Admin is logged in  | Admin can see buttons "Edit" "Cancel" at end of the recipe's page | Yes
If Admin is logged in clicking "Edit" button | Page to edit recipe's open | Yes
If Admin is logged in clicking cancel button | Admin redirected to index page | Yes
If User is not logged in buttons wont show | Buttons not showing |Yes

#### **_Register page_**

action taken | expected result | functional 
------------ | --------------- | ----------
If User is not register clicking "Register" link in navbar | Register page will open |Yes
User filling the register form "Username" section with not enough characters | Error message "wrong" appear | Yes
User filling the register form "Password" section with not enough/wrong characters | Error message "wrong" appear | Yes
User filling the register form "Username" correctly | Message "right" appear | Yes
User filling the register form "Password" correctly | Message "right" appear | Yes
User clicking register buttons after filling form correctly | Message confirmation appear/ redirecting to "my profile" page |Yes
If user already register clicking link "log in" next to "Already Registered?" | redirect User to "Log in" page | Yes

#### **_Log In page_**

action taken | expected result | functional 
------------ | --------------- | ----------
If User is registered by clicking "Log in" link in navbar | "Log in" page will open |Yes
User filling the log in form "Username" section with not enough characters | Error message "wrong" appear | Yes
User filling the log in form "Password" section with not enough characters | Error message "wrong" appear | Yes
User filling the log in form "Username" section correctly | Message "right" appear | Yes
User filling the log in form "Password" section correctly | Message "right" appear | Yes
User clicking log in buttons after filling form correctly | Message confirmation appear/ redirecting to "my profile" page |Yes

#### **_Log Out link_**

action taken | expected result | functional 
------------ | --------------- | ----------
If User logged in click "Log out" link | Confirmation log out modal message appear | Yes
If User logged in click "Cancel" button in modal message | User redirected to "My profile" page | Yes
If User logged in click "Agree" button in modal message | User redirected to "Index" page | Yes

#### **_My Profile page_**

action taken | expected result | functional 
------------ | --------------- | ----------
User logged in at "my profile" page | Can view its Username and number of recipes created | Yes
User logged in at "my profile" page | Can view its recipes as cards with "Edit" and "Delete" buttons | Yes
User clicking the recipe's card | Single page recipe will open | Yes
User can delete recipe from card view| Clicking the button "Delete", confirmation via modal to delete | Yes
User can edit recipe | Clicking the "Edit" button edit page opens | Yes
User can delete its own account | Clicking the button "Delete account", confirmation via modal to delete | Yes


#### **_Add recipe page_**

action taken | expected result | functional 
------------ | --------------- | ----------
User logged in at "add recipe" page, by filling the form in full and click "Add Recipe" button | Recipe added to account user | Yes
User not filling the input field "Recipe name" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Course" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Serving" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Difficulty" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Vegetarian" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Cooking time" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Preparation time" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Ingredients" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Preparation" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Please Insert picture's URL" | Message "Please fill in this field" appear in input field | Yes
User clicking "Cancel" button | User redirected to "Index" page | Yes


#### **_Edit recipe page_**

action taken | expected result | functional 
------------ | --------------- | ----------
User clicking "Edit" button on recipe card  | User redirected to "Edit recipe" page | Yes
User clicking "Edit" button on "Single recipe" page  | User redirected to "Edit recipe" page | Yes
User by filling the form in full and click "Submit" button | Recipe edited added to account user | Yes
User not filling the input field "Recipe name" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Course" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Serving" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Difficulty" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Vegetarian" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Cooking time" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Preparation time" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Ingredients" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Preparation" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Please Insert picture's URL" | Message "Please fill in this field" appear in input field | Yes
User clicking "Cancel" button | User redirected to "Index" page | Yes

#### **_Contact us page_**
action taken | expected result | functional 
------------ | --------------- | ----------
User by filling the form in full and click "Send" button | Modal message "Thank you! Your message was sent"  | Yes
User by filling the form in full and click "Send" button | Confirmation email for message sent to User via email  | Yes
User by filling the form in full and click "Send" button | Confirmation email to Developer received  | Yes
User not filling the input field "Name" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "E-mail address" | Message "Please fill in this field" appear in input field | Yes
User not filling the input field "Your message" | Message "Please fill in this field" appear in input field | Yes


#### **_User story_**
user story | action taken | expected result | functional 
-----------|------------ | --------------- | ----------
1 | As a User not register clicking "Register" link in navbar | Register page will open |Yes
2 | As a User not register | User can see recipes via "index" page | Yes
2 | As a User not register clicking the recipe's card | "Single recipe" page will open | Yes
3 | As a User not register by filling in full and correctly the contact form | User can contact Developer | Yes
4 | As a User registered, by filling in full and correctly the log in form | User logged in |Yes
5| As a User logged in can add recipe, by filling the form in full and click "Add Recipe" button | Recipe added to account user | Yes
6 | As a User logged in | User can see all recipes | Yes
7 | As a User logged in filling the form edit recipe in full and click "Submit" button | Recipe edited added to account user | Yes
8 | As a User logged in can delete recipe from card view| Clicking the button "Delete", confirmation via modal to delete | Yes
9 | As a User logged in can delete its own account | Clicking the button "Delete account", confirmation via modal to delete | Yes
10 | As a User logged in click "Log out" link | Confirmation log out modal message appear | Yes
11 | As a User logged in by filling the form contact us in full and click "Send" button | Modal message "Thank you! Your message was sent"  | Yes
12 | As a Developer I can view all User recipe | By logging in or not via "index" page | Yes
13 | As the Admin can delete recpes | Via "Delete" button in recipes cards | Yes


#### **_Database_**
action taken | expected result | functional 
------------ | --------------- | ----------
Deleting recipe via Admin log in | Only Recipe deleted from recipe collection User author of recipe not deleted | Yes
Deleting recipe via User log in | Only Recipe deleted from recipe collection User author of recipe not deleted | Yes
Deleting account via User log in | Only account deleted from user collection recipes not deleted | Yes
Add recipe via User or Admin | Recipe added recipe collection correctly | Yes
Register account | User added to User collection | Yes

