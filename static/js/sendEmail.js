/* Sending email through email.js */

function sendMail(contactForm) {
    // Prevent default form submission
    event.preventDefault();

    emailjs.send("service_374z12e", "template_ofnkbd8", {
        "from_name": contactForm.name.value,
        "from_business": contactForm.business.value,
        "start_date": contactForm.startdate.value,
        "from_email": contactForm.emailaddress.value,
        "assessment_type": contactForm.assesmenttype.value
    })
    .then(
        function(response) {
            console.log("MESSAGE SENT SUCCESSFULLY", response);
            alert("Message has been sent!");
            contactForm.reset(); // reset form after success
        },
        function(error) {
            console.log("MESSAGE SENDING FAILED", error);
            alert("Oops! Something went wrong. Try again later.");
        }
    );
}
