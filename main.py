from flask import Flask, request, redirect, render_template
import cgi
import urllib
import jinja2


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")                 
def form():
    return render_template('index_homepage.html')

@app.route("/add", methods=['POST'])                
def form_evaluation():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    # email = request.form['email']

    error_user = ''
    error_pass = ''
    error_ver = ''

    if not username:
        error_user = "That's not a valid username"
    elif ' ' in username:
            error_user = "Please no white spaces"
    elif len(username) < 3: 
            error_user = "Please make username between 3 - 20 characters"
    else:
        if len(username) > 20:
            error_user = "Please make username between 3 - 20 characters"

    if not password:
        error_pass = "That's not a valid password"
    elif ' ' in password:
        error_pass = "Please no spaces within passwords"
    elif len(password) < 3:
        error_pass = "Please make password between 3 - 20 characters"
    else:
        if len(password) > 20:
            error_pass = "Please make password between 3 - 20 characters"

    if not verify_password:
        error_ver = "That's not a valid password"
    elif ' ' in verify_password:
        error_ver = "Please no spaces within passwords"
    elif len(verify_password) < 3:
        error_ver = "Please make password between 3 - 20 characters"
    elif len(verify_password) > 20:
        error_ver = "Please make password between 3 - 20 characters"
    else:
        if verify_password != password:
            error_ver = "Passwords do not match"

    if not error_user and not error_pass and not error_ver:
        return redirect ('/welcome?username={0}'.format(username))
    else:
        return render_template('index_homepage.html', error_username=error_user, error_password=error_pass, error_verify_password=error_ver )


@app.route("/welcome")
def form_welcome():

    user_name = request.args.get('username')

    return render_template('welcome.html', userinput=user_name)

app.run()

