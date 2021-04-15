// CODE WAS WRITTEN BY FOLLOWING COURSE MATERIAL AND DOCUMENTATION FROM EMAIL.JS WEBSITE.
/**
 * 
 * @param {object} contactForm 
 */

function sendMail(contactForm) {
    emailjs.send("ms3_project", "template_recipe",{
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "more_info": contactForm.message.value,
    })
    .then(alert(`Thank you! Your message was sent`));
}