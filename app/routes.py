from app import app,db, bcrypt
from flask import render_template, url_for, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Me')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        print('In here')
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    print('ass')
    return render_template('login.html', title='Login', form=form)
