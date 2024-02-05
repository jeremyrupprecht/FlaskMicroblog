from flask import Flask

app = Flask(__name__)

from app import routes


# View Functions:
#   In Flask each route is handled with a Python function --> View functions
#   --> each one is mapped to one or more routes--> Flask executes a view function
#   when a user requests that specific URL (when a user visits that "route")