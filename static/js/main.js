let loginEmailInput = document.getElementById("loginEmail");
let loginPasswordInput = document.getElementById("loginPassword");
let loginBtn = document.getElementById("loginBtn");
let signupAnchor = document.getElementById("signupAnchor");

function signIn() {
  let loginEmail = loginEmailInput.value;
  let loginPassword = loginPasswordInput.value;

  if (loginEmail === "" || loginPassword === "") {
    swal({
      text: "Please fill in all fields",
      icon: "warning",
    });
    return;
  }

  // Send login request to backend
  fetch("http://127.0.0.1:5000/signin", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: loginEmail,
      password: loginPassword,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.message === "Login successful") {
        localStorage.setItem("userName", data.name); // Save username to localStorage
        window.location.href = "/home.html"; // Redirect to home page
      } else {
        swal({
          text: data.message,
          icon: "error",
        });
      }
    })
    .catch((error) => {
      console.error("Error during login:", error);
      swal({
        text: "Something went wrong. Please try again later.",
        icon: "error",
      });
    });
}

loginBtn.addEventListener("click", function () {
  signIn();
});

signupAnchor.addEventListener("click", function () {
  window.location.href = "signup";
});
