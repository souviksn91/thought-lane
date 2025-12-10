document.addEventListener("DOMContentLoaded", function() {
    const togglePasswordIcons = document.querySelectorAll(".togglePassword");

    togglePasswordIcons.forEach(function(toggleIcon) {
        toggleIcon.addEventListener("click", function() {
            // Assuming the input field is the previous sibling of the toggle icon
            const passwordField = this.previousElementSibling;
            const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
            passwordField.setAttribute("type", type);
            // Toggle the eye icon (if using FontAwesome)
            this.classList.toggle("fa-eye-slash");
        });
    });
});