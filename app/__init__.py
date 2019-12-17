from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_talisman import Talisman

app = Flask(__name__)

# Talisman configuration
# CSP config
csp = {
    'default-src': [
        "'self'",
    ],
    'script-src': [
        'https://code.jquery.com/',
        'https://cdnjs.cloudflare.com/ajax/libs/popper.js/',
        'https://stackpath.bootstrapcdn.com/bootstrap/'
    ],
    'style-src': [
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
        "'self'"
    ],
}

talisman = Talisman(app, content_security_policy=csp)

talisman.content_security_policy = csp
talisman.content_security_policy_report_uri = "/csp_error_handling"

app.config['SECRET_KEY'] = b'/\xaa1\x16%\xe4\x81\x86\xb18RJ\xab\x92M\xee'

#sql-alchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Login
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

#create the database
db.create_all()

from app import routes
from app.models import *
