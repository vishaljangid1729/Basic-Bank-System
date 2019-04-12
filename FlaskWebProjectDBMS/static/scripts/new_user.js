var l_name = document.getElementById("l_name");
var acc_id = document.getElementById("acc_id");
var mobile = document.getElementById("mobile");
var email = document.getElementById("email");
var password = document.getElementById("password");
var con_password = document.getElementById("con_password");
var sumbit = document.getElementById("sumbit");

l_name.style.display = "none";
acc_id.style.display = "none";
mobile.style.display = "none";
email.style.display = "none";
password.style.display = "none";
con_password.style.display = "none";
sumbit.style.display = "none";


var next = document.getElementById("next");
next.addEventListener("click", function () {
    if (l_name.style.display == "none") {
        l_name.style.display = "block";
        l_name.setAttribute = "requried";
        return;
    }
    else if (acc_id.style.display == "none") {
        acc_id.style.display = "block";
    }
    else if (mobile.style.display == "none") {
        mobile.style.display = "block";
    }
    else if (email.style.display == "none") {
        email.style.display = "block";
    }
    else if (password.style.display == "none") {
        password.style.display = "block";
    }
    else if (con_password.style.display == "none") {
        con_password.style.display = "block";
        next.style.display = "none";
        sumbit.style.display = "block";

    }

})