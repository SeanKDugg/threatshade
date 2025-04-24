// Sending email through email.js

function sendMail(contactForm) {
    // Preventing default form submission
    event.preventDefault();

    // Sending form data (replace EmailJS service and template IDs if needed)
    emailjs.send("service_dvw7otg", "template_4e4n1g7", {
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
