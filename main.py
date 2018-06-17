from flask import Flask, request, redirect, render_template
import cgi
import urllib
import jinja2


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")                 # this is my index homepage where errors will show up
def form():
    return render_template('index_homepage.html')

@app.route("/add", methods=['POST'])                
def form_evaluation():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    # email = request.form['email']

    if not username:
        error_user = "That's not a valid username"
    
    if not password:
        error_pass = "That's not a valid password"

    if not verify_password:
        error_ver = "That's not a valid password"
    return render_template('index_homepage.html', error_username=error_user, error_password=error_pass, error_verify_password=error_ver )

    

    
    

@app.route("/welcome", methods=['POST'])
def form_welcome():
    edit_header = "<h2>Edit My Watchlist</h2>"

    new_movie = request.form['new-movie']

    blank_error = ''

    if is_blank(new_movie):
        error_message = 'Sorry, you did not type anything in. Please try again!'
        content = page_header + edit_header + add_form.format(blank_error=error_message) + crossoff_form + page_footer
        return content
    else:
        if new_movie in terrible_movies:
            return redirect('/?error=' + urllib.parse.quote( 
            "Trust me, you don't want to add '{}' to your list".format(new_movie)))
        else:
            new_movie_element = "<strong>" + cgi.escape(new_movie) + "</strong>"
            sentence = new_movie_element + " has been added to your Watchlist!"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            return content



app.run()

