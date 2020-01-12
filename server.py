
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify, Markup
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# required to run Flask sessions and debug toolbar
app.secret_key = os.environ['WEDDING_SECRET_KEY']

# gives an error in jinga template if undefined variable rather than failing silently
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_login_form():
	"""Displays the login form"""

	return render_template('home.html')


if __name__ == '__main__':

    # app.debug = True

    # make sure templates, etc. are not cached in debug mode
    # app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')