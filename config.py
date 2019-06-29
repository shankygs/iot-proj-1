import os

DEBUG = True # Turns on debugging features in Flask

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
