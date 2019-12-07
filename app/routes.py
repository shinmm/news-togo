from app import app,db, bcrypt
from flask import render_template, url_for, redirect, request, current_app
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm, RegistrationForm


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
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    name= current_user.name
    logout_user()
    current_app.logger.info('%s logged out successfully', name)
    return redirect(url_for('index'))



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #join together as string and set
        news_pref = ",".join(list(form.news_preferences.data))
        user = User(name=form.name.data, email=form.email.data, password=hashed, news_preferences= news_pref)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)
