
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from sendemail import sendmail
import smtplib

app = Flask(__name__)

app.secret_key = 'a'

  
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '9zWgPLb2Rp'
app.config['MYSQL_PASSWORD'] = '1mK6N4mc36'
app.config['MYSQL_DB'] = '9zWgPLb2Rp'
mysql = MySQL(app)
@app.route('/')

def homer():
    return render_template('home.html')
@app.route('/usr')

def ho():
    return render_template('userdashboard.html')

@app.route('/test')

def test():
    return render_template('test.html')

@app.route('/dashboard')

def dash():
    return render_template('dashboard.html')

@app.route('/admin',methods =['GET', 'POST'])
def admin():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'you havent registered yet!'
    return render_template('admin.html', msg = msg)
@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('userdashboard.html', msg = msg)
        else:
            msg = 'you havent registered yet!'
    return render_template('login.html', msg = msg)

@app.route('/adregister', methods =['GET', 'POST'])
def registet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
       
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
       
        else:
            cursor.execute('INSERT INTO admin VALUES (NULL, % s, % s, % s)', (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            TEXT = "Hello "+username + ",\n\n"+ """Thanks for  registring as admin at smartinterns """ 
            subject="digital book confirmed"
            message  = 'Subject: {}\n\n{}'.format("smartinterns Carrers", TEXT)
            sendmail(TEXT,email,subject)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('adregister.html', msg = msg)

@app.route('/custregister', methods =['GET', 'POST'])
def cusregistet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
       
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
       
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s,"0")', (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            TEXT = "Hello "+username + ",\n\n"+ """Thanks for applying registring at smartinterns """ 
            subject="digital book confirmed"
            message  = 'Subject: {}\n\n{}'.format("text", TEXT)
            sendmail(TEXT,email,subject)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('custregister.html', msg = msg)

@app.route('/display')
def display():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM user WHERE id = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('display.html',account = account)

@app.route('/payment')
def payment():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM user WHERE id = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('payment.html',account = account)


@app.route('/apayment')
def apayment():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM user WHERE id = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('apayment.html',account = account)

@app.route('/ahis',methods =['GET', 'POST'])
def ahist():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s AND email = % s', (username, email ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('/test.html', msg = msg)
        else:
            msg = 'you havent registered yet!'
    return render_template('ahis.html', msg = msg)



@app.route('/adpur', methods =['GET', 'POST'])
def adpur():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        item = request.form['item']
       
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO purchase VALUES ( % s, % s)', (username, item))
        mysql.connection.commit()
        msg = 'You have successfully entered !'
        TEXT = "Hello "+username + ",\n\n"+ """Thanks for applying registring at smartinterns """ 
        message  = 'Subject: {}\n\n{}'.format("smartinterns Carrers", TEXT)
            #sendmail(TEXT,email)
            #sendgridmail(email,TEXT)
            
    return render_template('adpur.html', msg = msg)



@app.route('/uspur')
def uspur():
      print(session["username"])
      
      cursor = mysql.connection.cursor()
      cursor.execute('SELECT * FROM purchase WHERE username = % s', (session['username'],))
      details = cursor.fetchall()
      colnames = ['Username','item']
     
      print("uspur")
      return render_template('uspur.html',colnames = colnames,details = details) 
     
      
@app.route('/update', methods =['GET', 'POST'])
def update():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        due = request.form['due']
       
        
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE  user  SET due = % s WHERE username = % s ', (due, username))
        mysql.connection.commit()
        msg = 'You have successfully updated !'
        TEXT = "Hello "+username + ",\n\n"+ """""" 
        subject="your due"+due
        message  = 'Subject: {}\n\n{}'.format("text", TEXT)
        sendmail(TEXT,email,subject)
       
            
    return render_template('update.html', msg = msg)

@app.route('/email', methods =['GET', 'POST'])
def email():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        tes = request.form['tes']
        sub = request.form['sub']
        
        
        mysql.connection.commit()
        msg = 'You have send successfully!'
        TEXT = tes+ ",\n\n"+ """"""+"from="+email+",\n\n"+ """"""+"username="+username
        subject= sub
        message  = 'Subject: {}\n\n{}'.format("text", TEXT)
        sendmail(TEXT,"mdhvsnair@gmail.com",subject)
       
            
    return render_template('email.html', msg = msg)

   

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True,port = 8080)