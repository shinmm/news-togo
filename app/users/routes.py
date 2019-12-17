from flask import render_template, url_for, redirect, request, Blueprint, current_app
from flask_login import login_user, current_user, logout_user, login_required

from app import db, bcrypt
from app.models import User
from app.users.forms import RegistrationForm, LoginForm, UpdateForm

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    name= current_user.name
    logout_user()
    current_app.logger.info('%s logged out successfully', name)
    return redirect(url_for('main.index'))



@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #join together as string and set
        news_pref = ",".join(list(form.news_preferences.data))
        user = User(name=form.name.data, email=form.email.data, password=hashed, news_preferences= news_pref)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()

    if form.validate_on_submit():
        print("worrked")
        news_pref = ",".join(list(form.news_preferences.data))
        current_user.news_preferences = news_pref

        db.session.commit()

        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        pass# form.username.data = current_user.username
    return render_template('account.html', title='Account', form=form)
