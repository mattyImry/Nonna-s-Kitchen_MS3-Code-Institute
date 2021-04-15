// CODE WAS WRITTEN BY FOLLOWING COURSE MATERIAL AND DOCUMENTATION FROM EMAIL.JS WEBSITE.
/**
 * 
 * @param {object} contactForm 
 */
function sendMail(contactForm) {
    emailjs.send("sri_lanka_prj", "template_srilanka",{
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "more_info": contactForm.message.value,
        
    })
    .then(alert(`Thank you! Your message was sent`));
}