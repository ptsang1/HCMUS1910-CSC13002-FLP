import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MASTERNAME = "ptsang"
    PASSWORD = "695930599"
    DATABASE_NAME = "postgres"
    ENDPOINT = "homnayanlondatabase.cemjothahgv9.ap-southeast-1.rds.amazonaws.com"
    PORT = "5432"

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + MASTERNAME + ':' \
                              + PASSWORD + '@' + ENDPOINT + ':' + PORT + '/' \
                              + DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False