from app import app

# Define the base/index view function 
@app.route('/')             # When the user goes to either of these routes
@app.route('/index')        
def index():                # This function is called and the browser it passed whatever is returned
    return "Hello, World!"


# @app.route is a python decorator --> these modify the functions that follow
# them 
#   --> common use case: use them to register callback functions for certain events
#   --> in this case (@app.route) crates an association between the URL and the function
#       --> When the user visits either of these urls, this function is called AND IT'S
#           RETURN VALUE IS PASSED BACK TO THE BROWSER AS A RESPONSE