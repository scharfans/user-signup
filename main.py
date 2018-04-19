from flask import Flask, request, redirect, render_template



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/", methods=['POST'])
def validate_form():
    user_name =  request.form['user-name']
    password = request.form['pass-word']
    password_v = request.form['verify pass-word']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    email_error = ''
    passwordv_error = ''


    if len(user_name) < 3 or len(user_name) >20 or ' ' in user_name:
        username_error = 'Not a valid username'
    
    if len(email) < 1 or "@" not in email or "." not in email:
        email_error = 'Not a valid email'

    if len(password) < 3 or len(password) >20 or ' ' in password:
        password_error = 'Not a valid password' 

    if len(password_v) < 1 or password != password_v:
        passwordv_error = 'password not verified'
        

    if not username_error and not password_error and not email_error and not passwordv_error:
        return redirect('/welcome?user_name={0}'.format(user_name))
    
    else:
        return render_template('homepage.html', username=user_name, username_error=username_error, email=email, email_error=email_error, password_error=password_error, passwordv_error=passwordv_error)
    
        

@app.route("/welcome")
def welcome():
    user_name = request.args.get('user_name')
    return render_template('welcome.html', username=user_name)  



app.run()