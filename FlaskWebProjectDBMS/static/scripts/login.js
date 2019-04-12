var sumbit = document.getElementById("sumbit");
var password = document.getElementById("password");
var next = document.getElementById("next");
sumbit.style.display = "none";
password.style.display = "none";
next.addEventListener("click", function () {
    if (password.style.display == "none") {
        password.style.display = "block";
        next.style.display = "none";
        sumbit.style.display = "block";
    }
})
