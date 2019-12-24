import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SECURITY_PASSWORD_SALT = 'phasanukiProject'
    DEBUG = False
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MASTERNAME = "ptsang"
    PASSWORD = "695930599"
    DATABASE_NAME = "postgres"
    ENDPOINT = "homnayangidb.cemjothahgv9.ap-southeast-1.rds.amazonaws.com"
    PORT = "5432"

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + MASTERNAME + ':' \
                              + PASSWORD + '@' + ENDPOINT + ':' + PORT + '/' \
                              + DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'homnayangi.se@gmail.com'
