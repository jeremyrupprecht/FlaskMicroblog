from flask import render_template
from app import app

# @app.route is a python decorator --> these modify the functions that follow
# them 
#   --> common use case: use them to register callback functions for certain events
#   --> in this case (@app.route) crates an association between the URL and the function
#       --> When the user visits either of these urls, this function is called AND IT'S
#           RETURN VALUE IS PASSED BACK TO THE BROWSER AS A RESPONSE

# Define the base/index view function 
@app.route('/')             # When the user goes to either of these routes
@app.route('/index')        
def index():                # This function is called and the browser it passed whatever is returned
    user = {'username': 'Jeremy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful  day in Portland'
        }, 
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'suuuuuh dude'
        },
        {
            'author': {'username': 'Jones'},
            'body': 'wazzzzzzup'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)