import os

class Config:
    SECRET_KEY = '6f44d15ffe00180d3d09fb4ee120cb97'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'abybino50018@gmail.com'
    MAIL_PASSWORD = 'bijeabja50018'
    MAIL_DEFAULT_SENDER = 'abybino50018@gmail.com'