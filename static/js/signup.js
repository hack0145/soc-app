let signupBtn = document.getElementById("signupBtn");
let signupNameInput = document.getElementById("signupName");
let signupEmailInput = document.getElementById("signupEmail");
let signupPasswordInput = document.getElementById("signupPassword");
let loginAnchor = document.getElementById("loginAnchor");

function signUp() {
  let userName = signupNameInput.value;
  let userEmail = signupEmailInput.value;
  let userPassword = signupPasswordInput.value;

  if (userName === "" || userEmail === "" || userPassword === "") {
    swal({
      text: "Please fill in all fields",
      icon: "warning",
    });
    return;
  }

  fetch("/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: userName,
      email: userEmail,
      password: userPassword,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        return response.json().then((data) => {
          throw new Error(data.message || "Unknown error");
        });
      }
      return response.json();
    })
    .then((data) => {
      swal({
        text: data.message,
        icon: "success",
      }).then(() => {
        window.location.href = "/index.html";
      });
    })
    .catch((error) => {
      console.error("Error during signup:", error);
      swal({
        text: error.message || "Something went wrong. Please try again later.",
        icon: "error",
      });
    });
}

signupBtn.addEventListener("click", function () {
  signUp();
});

loginAnchor.addEventListener("click", function () {
  window.location.href = "/index.html";
});
