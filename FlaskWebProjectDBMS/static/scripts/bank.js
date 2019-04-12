var transfer = document.getElementById("transfer");
var withdrawal = document.getElementById("withdrawal");
var balance = document.getElementById("balance");
var logout = document.getElementById("logout");
var deposit = document.getElementById("deposit");
var statement = document.getElementById("statement");
var ok = document.getElementById("ok");
var balance_menu = document.getElementById("balnace_menu");
var trans_menu = document.getElementById("transfer_menu");
var deposit_menu = document.getElementById("deposit_menu");
var wit_menu = document.getElementById("wit_menu");
var statement_menu = document.getElementById('statement_menu');






balance.addEventListener("click", function () {
    statement_menu.style.display = 'none';
    balance_menu.style.display = "block";
    balance_menu.style.left = "35%";
    balance_menu.style.top = "20%";
    
});
statement.addEventListener('click', function () {
    statement_menu.style.display = 'block';
    console.log('hey');
});

ok.addEventListener("click", function () {
    balance_menu.style.display = "none";
    statement_menu.style.display = 'none';
});

transfer.addEventListener("click", function () {
    trans_menu.style.display = "block";
    statement_menu.style.display = 'none';

});
deposit.addEventListener("click", function () {
    deposit_menu.style.display = "block";
    statement_menu.style.display = 'none';
});
withdrawal.addEventListener("click", function () {
    wit_menu.style.display = "block";
    statement_menu.style.display = 'none';
});

document.getElementById('cancel_deposit').addEventListener('click', function () {
    deposit_menu.style.display = 'none';
    console.log('work');
});
document.getElementById('cancel_transfer').addEventListener('click', function () {
    trans_menu.style.display = 'none';
});
document.getElementById('cancel_wid').addEventListener('click', function () {
    wit_menu.style.display = 'none';
});