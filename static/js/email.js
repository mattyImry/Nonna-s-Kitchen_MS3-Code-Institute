// CODE WAS WRITTEN BY FOLLOWING COURSE MATERIAL AND DOCUMENTATION FROM EMAIL.JS WEBSITE.
/**
 * 
 * @param {object} contactForm 
 */
function sendMail(contactForm) {
    emailjs.send("ms3_project", "template_recipe",{
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "more_info": contactForm.textarea1.value,
        
    })
    .then(alert(`Thank you! Your message was sent`));
}