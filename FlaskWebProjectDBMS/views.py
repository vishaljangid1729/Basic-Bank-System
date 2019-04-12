"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, session
from FlaskWebProjectDBMS import app
import sqlite3 as sql
from flask_wtf import Form
from wtforms import StringField, PasswordField
import os
app.secret_key = os.urandom(25)



conn = sql.connect('database.db')
cur = conn.cursor()
#cur.execute("DELETE FROM users")
#conn.commit()
#cur.execute("DELETE FROM transition")
#conn.commit()
#cur.execute("DELETE FROM balance ")
#conn.commit()

#cur.execute(" ALTER TABLE transition ADD total_bal ")
#conn.commit()
#cur.execute("SELECT * FROM transition")
#conn.commit()
#print(cur.fetchall())

#cur.execute(''' DROP TABLE users ''')

#conn.commit()
#cur.execute(''' CREATE TABLE users (f_name TEXT, l_name TEXT, acc_id TEXT PRIMARY KEY, 
 #                                      mobile TEXT, email TEXT, password TEXT, con_password TEXT) ''')
#conn.commit()

#cur.execute(''' DROP TABLE curr ''')
#conn.commit()


#cur.execute('''CREATE TABLE curr ( s_id TEXT )''')
#conn.commit()

#cur.execute(''' CREATE TABLE transition (acc_id TEXT, mode_id TEXT, debit NUMBER, credit NUMBER) ''')
#conn.commit()
#cur.execute(''' CREATE TABLE mode (mode_id NUMBER, transfer_to TEXT, transfer_from TEXT, withdrawal NUMBER, deposit NUMBER ) ''')
#conn.commit()
#cur.execute("DROP TABLE balance")
#conn.commit()
#cur.execute(''' CREATE TABLE balance (acc_id TEXT PRIMARY KEY, balance NUMBER) ''')
#conn.commit()
#cur.execute(''' CREATE TABLE current (curr_acc_id TEXT)  ''')
#conn.commit()

#cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
#conn.commit()
#print(cur.fetchall())

#cur.execute("DROP TABLE current")
#conn.commit()

#cur.execute(''' CREATE TABLE current (curr_acc_id TEXT)  ''')
#conn.commit()
#cur.execute("DELETE FROM transition")
#conn.commit()
#cur.execute(''' INSERT INTO transition (debit, credit) VALUES(?,?) ''', (200000, 10000))
#conn.commit()
#cur.execute(''' SELECT * FROM transition ''')
#conn.commit()
#print(cur.fetchall())
#cur.execute("SELECT acc_id FROM users")
#conn.commit()
#user_list = cur.fetchall()
#print(user_list)
#for user in user_list:
#    cur.execute("INSERT INTO balance (acc_id, balance ) VALUES(?, ?)", (user[0], 0))
#    conn.commit()


#cur.execute("SELECT * FROM balance")
#conn.commit()
#print(cur.fetchall())
#cur.execute("SELECT * FROM balance")
#print(cur.fetchall())












print('tabel create successfully')

print ("opened database sucessful")


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/new_user')
def new_user():
    return render_template('new_user.html')





@app.route('/login', methods = ['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST':
           conn = sql.connect('database.db')
           cur = conn.cursor()
           f_name = request.form['f_name']
           l_name = request.form['l_name']
           acc_id = request.form['acc_id']
           mobile = request.form['mobile']
           email = request.form['email']
           password = request.form['password']
           con_password = request.form['con_password']
           cur.execute(''' SELECT acc_id FROM users WHERE acc_id = ? ''', [acc_id])
           conn.commit()

           data = cur.fetchall()
           print(data)
           if data !=[]:
               msg = "You account exist."
               return render_template('login.html', msg = msg)
           if password != con_password:
               msg = "Password don't match."
               return render_template("login.html", msg = msg)

           else:
              cur.execute('''INSERT INTO users (f_name, l_name, acc_id, mobile, email, password, con_password) VALUES  (?,?,?,?,?,?,?)''', (f_name, l_name, acc_id, mobile, email, password, con_password))
             
              conn.commit()
              cur.execute(''' INSERT INTO balance (acc_id, balance) VALUES (?,?) ''', (acc_id, 0))
              conn.commit()
              msg = "Account successfully created"
              return render_template('login.html', msg = msg)
    return render_template('login.html', msg = msg)

@app.route('/your_acc', methods = ['POST', 'GET'])
def bank():
    if request.method == 'POST':
        acc_id = request.form['acc_id']
        password = request.form['password']

        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT acc_id, f_name FROM users WHERE acc_id = ? AND password = ?", [acc_id, password])
        data = cur.fetchall()
        print(data)
        

        if data != []:
            name = data[0][1]
            cur.execute("DELETE FROM current")
            con.commit()
            cur.execute("INSERT INTO current (curr_acc_id) VALUES(?)", [acc_id])
            con.commit()
            cur.execute("SELECT * FROM current")
            con.commit()
            print(cur.fetchall())
            
            bal = total_balance(data[0][0])
            con = sql.connect("database.db")
            con.row_factory = sql.Row
   
            cur = con.cursor()
            cur.execute("SELECT * FROM transition WHERE acc_id = ?", [acc_id])
   
            rows = cur.fetchall();
            
            
            
            
            return render_template('bank.html', name = name, bal = bal, rows = rows)
        else:
            error = "Account information is wrong."
            return render_template('login.html', msg = error)

@app.route('/your_acc/#', methods = ['POST', 'GET'])
def transfer():
    if request.method == 'POST':
        acc_id = request.form['acc_id']
        amount = request.form['amount']
        conn = sql.connect('database.db')
        cur = conn.cursor()

        cur.execute(''' SELECT f_name, acc_id FROM users, current WHERE acc_id = curr_acc_id  ''')
        conn.commit()
        data = cur.fetchall()
        name = data[0][0]
        bal = total_balance(data[0][1])
        print(data)
        cur.execute("SELECT acc_id FROM users WHERE acc_id = ?", [acc_id])
        conn.commit()
        data_ch = cur.fetchall()
        print('wha ti dkjai')
        print(data_ch)
        print('ionsafjan')
        if data_ch ==[]:
            msg = "Account does not exit."
            con = sql.connect("database.db")
            con.row_factory = sql.Row
   
            cur = con.cursor()
            cur.execute("SELECT * FROM transition WHERE acc_id = ?", [data[0][1]])
   
            rows = cur.fetchall();
            return render_template('bank.html', name = name, bal = bal, msg = msg, rows= rows)


        bal = total_balance(data[0][1])
        if int(bal)>=int(amount) and acc_id!= data[0][1]:
            mode1 = "Transfer to " + acc_id
            cur.execute("UPDATE balance SET balance = balance - (?) WHERE acc_id = (?)", (amount, data[0][1]))
            conn.commit()
            cur.execute("SELECT * FROM balance")
            conn.commit()
            print(cur.fetchall())
            total_bal = total_balance(data[0][1])
            cur.execute(''' INSERT INTO transition (acc_id , mode_id, debit, total_bal) VALUES (?, ?, ?,?)  ''', (data[0][1], mode1, amount, total_bal  ))
            conn.commit()
            cur.execute("SELECT * FROM transition")
            conn.commit()
            print(cur.fetchall())
            
            

            #add to other
            mode2 = "Transfer from "+ data[0][1]
            
            cur.execute("UPDATE balance SET balance = balance + (?) WHERE acc_id = (?)", (amount, acc_id))
            conn.commit()
            total_bal = total_balance(acc_id)
            cur.execute(''' INSERT INTO transition (acc_id , mode_id, credit, total_bal) VALUES (?, ?, ?,?)  ''', (acc_id, mode2, amount, total_bal  ))
            conn.commit()
            cur.execute("SELECT * FROM transition")
            conn.commit()
            print(cur.fetchall())
            
           
            
            msg = "Transfer success: " + amount
        
            bal = total_balance(data[0][1])
            con = sql.connect("database.db")
            con.row_factory = sql.Row
   
            cur = con.cursor()
            cur.execute("SELECT * FROM transition WHERE acc_id = ?", [data[0][1]])
   
            rows = cur.fetchall();
            return render_template('bank.html', name = name, bal = bal, msg = msg, rows= rows)
        elif acc_id == data[0][1]:
            msg = "Can't transfer to your accout."
            return render_template('bank.html', name = name, msg = msg, bal = bal)

        else:
            msg = "Balance Low"
            return render_template('bank.html', name = name, msg = msg, bal = bal)






        
@app.route('/your_acc/deposit', methods = ['POST', 'GET'])
def deposit():
    if request.method == 'POST':
        conn = sql.connect('database.db')
        cur = conn.cursor()
        amount = request.form['amount']
        print(amount)
        cur.execute(''' SELECT f_name, acc_id FROM users, current WHERE acc_id = curr_acc_id  ''')
        conn.commit()
        data = cur.fetchall()
        name = data[0][0]
        cur.execute("UPDATE balance SET balance = balance + (?) WHERE acc_id = (?)", (amount, data[0][1]))
        conn.commit()
        total_bal = total_balance(data[0][1])
        cur.execute(''' INSERT INTO transition (acc_id , mode_id, credit, total_bal) VALUES (?, ?, ?,?)  ''', (data[0][1], "Deposit", amount , total_bal ))
        conn.commit()
        cur.execute("SELECT * FROM transition")
        conn.commit()
        print(cur.fetchall())
        
        cur.execute("SELECT * FROM balance")
        conn.commit()
        print(cur.fetchall())
        msg = "Deposit Successful: " + amount
        
        bal = total_balance(data[0][1])
        con = sql.connect("database.db")
        con.row_factory = sql.Row
   
        cur = con.cursor()
        cur.execute("SELECT * FROM transition WHERE acc_id = ?", [data[0][1]])
   
        rows = cur.fetchall();

        return render_template('bank.html', name = name, msg = msg, bal = bal, rows = rows)

def total_balance(acc_id):
     conn = sql.connect('database.db')
     cur = conn.cursor()
     cur.execute("SELECT balance FROM balance WHERE acc_id = ?", [acc_id])
     conn.commit()
     data = cur.fetchall()
     
     return data[0][0]

@app.route('/your_acc/withdrawal', methods = ['POST', 'GET'])
def withdrawal():
    if request.method == 'POST':
        conn = sql.connect('database.db')
        cur = conn.cursor()
        amount = request.form['amount']
        cur.execute(''' SELECT f_name, acc_id FROM users, current WHERE acc_id = curr_acc_id  ''')
        conn.commit()
        data = cur.fetchall()
        name = data[0][0]
        bal = total_balance(data[0][1])
        print(amount)
        if int(amount)<= int(bal):
            cur.execute("UPDATE balance SET balance = balance - (?) WHERE acc_id = (?)", (amount, data[0][1]))
            conn.commit()
            total_bal = total_balance(data[0][1])
            
            cur.execute(''' INSERT INTO transition (acc_id , mode_id, debit, total_bal) VALUES (?, ?, ?,?)  ''', (data[0][1], "Withdrawal", amount ,total_bal ))
            conn.commit()
            cur.execute("SELECT * FROM transition")
            conn.commit()
            print(cur.fetchall())
            
            cur.execute("SELECT * FROM balance")
            conn.commit()
            print(cur.fetchall())
            bal = total_balance(data[0][1])
            msg = "Withdrawal Successful: " + amount
            con = sql.connect("database.db")
            con.row_factory = sql.Row
   
            cur = con.cursor()
            cur.execute("SELECT * FROM transition WHERE acc_id = ?", [data[0][1]])
   
            rows = cur.fetchall();
            return render_template('bank.html', name = name, msg = msg, bal = bal, rows = rows)
        else:
            
            msg = "Balance Low"
            return render_template('bank.html', name = name, msg = msg, bal = bal)





        
        
        

        

        
        





        








        
    

        






    







    


            





