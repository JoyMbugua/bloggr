import os
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from flask_mail import Mail
import math

db = SQLAlchemy()
simple = SimpleMDE()
bootstrap = Bootstrap()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def countr(blog):
    words = blog.split(" ")
    word_count = 0
    for word in words:
        word_count += 1
    read_time = math.ceil(word_count // 200)
    msg = None
    if read_time == 1 or read_time < 1:
        msg = "1 Minute Read"
    else:
        msg = f"{read_time} Minutes Read"
    return msg

def create_app(config_name):

    app = Flask(__name__, static_url_path='/static')

    app.config.from_object(config_options[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.jinja_env.globals.update(countr=countr)

    return app
