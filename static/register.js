// Example: Password match validation
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form[action*='register']");
  const password = document.getElementById("registerPassword");
  const confirm = document.getElementById("confirmPassword");

  form.addEventListener("submit", function (e) {
    if (password.value !== confirm.value) {
      e.preventDefault();
      alert("Passwords do not match!");
    }
  });
});