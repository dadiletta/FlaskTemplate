"""
WELCOME
"""
from flask import render_template

# our objects
from . import views


######################
#### STATIC PAGES ####
######################
# Displays the home page.
@views.route('/')
@views.route('/index')
@views.route('/index.html')
# Users must be authenticated to view the home page, but they don't have to have any particular role.
# Flask-Security will display a login form if the user isn't already authenticated.
def index():
    return render_template('pages/index.html')