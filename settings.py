import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'jason'
DB_PASSWORD = 'cyan4dawn'
MY_DATABASE_NAME = 'request_manager_db'
DB_HOST = os.getenv('IP', 'localhost')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, MY_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
