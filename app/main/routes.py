from flask import render_template, Blueprint

from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Me')
