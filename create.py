from flask import Flask, redirect, url_for, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)

POSTGRES = {
    'user': 'Shruthi',
    'pw': 'root123',
    'db': 'demo',
    'host': 'localhost',
    'port': '5432',
}
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
