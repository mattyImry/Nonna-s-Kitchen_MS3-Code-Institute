## **_Testing_**

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

    [mobile](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/a7601532416493f34caf8b53939a5c99aa3a6ce9/media/mobile_lighthouse.jpg) Screenshot  

    [desktop](https://github.com/mattyImry/Nonna-s-Kitchen_MS3-Code-Institute/blob/a7601532416493f34caf8b53939a5c99aa3a6ce9/media/desktop_lighthouse.jpg) Screenshot.


### **_Manual testing_**

#### **_Nav bar_**

action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking the "Logo" | Redirected to index | Yes  
Clicking the "Home" link | Redirected to index | Yes  
Clicking the "My profile" link | Redirected to "My profile" page | Yes  
Clicking the "Add Recipe" link | Redirected to "Add Recipe" page | Yes  
Clicking the "Log in" link | Redirected to "Log in" page  |Yes   
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
Writing in the search bar "Main" | Shows only recipes that are Main Course. The bottom number and pagination show relevant pages and numbers | Yes
Writing in the search bar "Potato" | Shows only recipes that have "Potato" on title or as ingredient. The bottom number and pagination show relevant pages and numbers | Yes
Writing in the search bar a word not present in recipes | Shows message "0 recipes No Recipe found" | Yes
Clicking the recipe's card | Redirected to recipe full page | Yes  
If User is not logged in | User can see recipes card not buttons | Yes
If User is not logged in Clicking the recipe's card | Single page recipe will open | Yes
If User is logged in Clicking the recipe's card | Single page recipe will open | Yes
If User is logged in | User can see recipes with buttons only for his own recipes | Yes
If User is logged in can delete recipe | Clicking the button delete confirmation via modal to delete | Yes
If User is logged in can edit recipe | Clicking the button edit | Yes
If Admin is not logged in Clicking the recipe's card | Single page recipe will open | Yes
If Admin is logged in | Admin can see recipes with buttons | Yes
If Admin is logged in Clicking the recipe's card | Single page recipe will open | Yes
If Admin is logged in can delete recipe | Clicking the button delete confirmation via modal to delete | Yes
If Admin is logged in can edit recipe | Clicking the button edit | Yes

#### **_Single recipe page_**

action taken | expected result | functional 
------------ | --------------- | ---------
If User is logged in  | User can see buttons "Edit" "Cancel" at end of the recipe's page | Yes
If User is logged in clicking "Edit" button | Page to edit recipe's page open | Yes
If User is logged in clicking cancel button | User redirected to index page | Yes
If Admin is logged in  | User can see buttons "Edit" "Cancel" at end of the recipe's page | Yes
If Admin is logged in clicking "Edit" button | Page to edit recipe's page open | Yes
If Admin is logged in clicking cancel button | Admin redirected to index page | Yes
If user is not logged in button wont' show | Buttons not showing |Yes