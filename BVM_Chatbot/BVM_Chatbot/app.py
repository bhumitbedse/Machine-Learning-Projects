from chatbot import chatbot
from flask import Flask, render_template, request,session,logging,url_for,redirect,flash
from flask_recaptcha import ReCaptcha
import mysql.connector
import os
from flask_mail import *  
from random import * 

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.secret_key=os.urandom(24)
app.static_folder = 'static'


app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY = "6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
))

recaptcha=ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'

mail = Mail(app)  

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = "ripperjohn535@gmail.com"  
app.config['MAIL_PASSWORD'] = "johnripper12"  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)  
otp = randint(000000,999999)  
#database connectivity
conn=mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='register')
cur= conn.cursor()

# Google recaptcha - site key : 6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L
# Google recaptcha - secret key : 6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cur.fetchall()
    if len(users)>0:
        session['id']=users[0][0]
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')
    # return "The Email is {} and the Password is {}".format(email,password)
    # return render_template('register.html')

@app.route('/validation',methods=['GET','POST'])
def validate():
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        # flash("Successfully Registered")
        return redirect('/add_users')
    else:   
        flash(u'Invalid OTP', 'error')
        return render_template('verify.html',error="Invalid OTP")


@app.route('/verify',methods=['GET','POST'])
def verify():
    email = request.form["uemail"]
    session['name'] =  request.form.get('name') 
    session['email']=request.form.get('uemail')
    session['password']=request.form.get('upassword') 
    msg = Message('OTP',sender = 'ripperjohn535@gmail.com', recipients = [email])  
    msg.body = "Your Verification Code is : " + str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
    
@app.route('/add_users',methods=['GET','POST'])
def add_user():
    name=session['name']
    email=session['email']
    password=session['password']

    #cur.execute("UPDATE users SET password='{}'WHERE name = '{}'".format(password, name))
    cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cur.fetchall()
    flash('You have successfully registered!')
    session['id']=myuser[0][0]
    return redirect('/index')

@app.route('/suggestion',methods=['POST'])
def suggestion():
    email=request.form.get('uemail')
    suggesMess=request.form.get('message')

    cur.execute("""INSERT INTO  suggestion(email,message) VALUES('{}','{}')""".format(email,suggesMess))
    conn.commit()
    flash('You suggestion is succesfully sent!')
    return redirect('/index')

@app.route('/add_user',methods=['POST'])
def register():
    if recaptcha.verify():
        flash('New User Added Successfully')
        return redirect('/register')
    else:
        flash('Error Recaptcha') 
        return redirect('/register')


@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    # app.secret_key=""
    app.run() 
