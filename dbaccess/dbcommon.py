from flask import Flask, redirect, url_for, request, render_template, json, Response
from flask import jsonify
import os
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

POSTGRES = {
    'user': 'SHANKY',
    'pw': 'root123',
    'db': 'SHANKY',
    'host': 'localhost',
    'port': '5432',
}

ents = [
    [1,'Enterprise-1', 'Los Angeles', 'West', 'USA', '10001'],
    [2,'Enterprise-2', 'Dallas', 'Central', 'USA', '10002'],
    [3,'Enterprise-3', 'Munich', 'North', 'Germany', '20001'],
    [4,'Enterprise-4', 'Berlin', 'South', 'Germany', '20001'],
    [5,'Enterprise-5', 'Mumbai', 'West', 'India', '30001']
]

sites = [
    [1001, 1,'Site-1-Ent-1', 'USA', 'Seattle', 'Area-1', '10101'],
    [1002, 1,'Site-2-Ent-1', 'USA', 'Las Vegas', 'Area-2', '10102'],
    [1003, 1,'Site-3-Ent-1', 'USA', 'San Diego', 'Area-3', '10103'],
    [2001, 2,'Site-1-Ent-2', 'USA', 'Austin', 'Area-1', '10104'],
    [2002, 2,'Site-2-Ent-2', 'USA', 'Houston', 'Area-2', '10105'],
    [2003, 2,'Site-3-Ent-2', 'USA', 'Chicago', 'Area-3', '10106'],
    [3001, 3,'Site-1-Ent-3', 'Germany', 'Bavaria', 'Area-1', '20101'],
    [3002, 3,'Site-2-Ent-3', 'Germany', 'Hessey', 'Area-2', '20102'],
    [3003, 3,'Site-3-Ent-3', 'Germany', 'Saxony', 'Area-3', '20103'],
    [4001, 4,'Site-1-Ent-4', 'Germany', 'Bremen', 'Area-1', '20104'],
    [4002, 4,'Site-2-Ent-4', 'Germany', 'Hamburg', 'Area-2', '20105'],
    [4003, 4,'Site-3-Ent-4', 'Germany', 'Sarland', 'Area-3', '20106'],
    [5001, 5,'Site-1-Ent-5', 'India', 'Ahmedabad', 'Area-1', '30101'],
    [5002, 5,'Site-2-Ent-5', 'India', 'Pune', 'Area-2', '30102'],
    [5003, 5,'Site-3-Ent-5', 'India', 'Udaipur', 'Area-3', '30103'],
]

users = [
    [1001, 'john','john@yahoo.com',    '111111'],
    [1002, 'david','david@google.com', '222222'],
    [1003, 'russel','russel@wipro.com','333333'],
    [1004, 'mary','mary@hotmail.com',  '444444'],
    [1005, 'joe','joe@msft.com',       '555555']
]

#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)
#db.create_all()

@app.route('/api/v1/add/user', methods=["GET","POST"] )
def add_user_db():
    print("In add_user_db()")
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    user1 = EUser(EntUserName=username, EntUserEmail=email)
    user1.set_password(password)
    user1.EntUserID = 1010
    db.session.add(user1)
    db.session.commit()
    return("User added succesfully")

@app.route('/api/v1/validate/user', methods=["GET","POST"] )
def validate_user():
    print("In validate_user()")
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    user1 = EUser.query.filter_by(EntUserName=username).first()
    if user1 is None or not user1.check_password(password):
        print ('Authentication failed!')
        return Response("Authentication failed!", 401)
    print ('Authentication Success!')
    return Response("Authentication Success!!!", 200)

@app.route('/api/v1/get/enterprise/all', methods=["GET"] )
def query_enterprise_all():
    print("In query_enterprise_all()")
    ents = db.session.query(Enterprise).all()
    ent_list = Enterprise.serialize_list(ents)
    print(ent_list)
    return(jsonify(ent_list))

@app.route('/api/v1/db/create', methods=["GET"] )
def create_tables():
    print("In create_tables()")
    db.create_all()
    return("Created tables")

@app.route('/api/v1/db/clear', methods=["GET"] )
def clear_tables():
    db.session.query(Site).delete()
    db.session.query(Enterprise).delete()
    db.session.query(EntUser1).delete()
    db.session.commit()
    return("Cleared tables")

@app.route('/api/v1/db/init', methods=["GET"] )
def populate_tables_all():
    print("In populate_tables_all()")
    populate_tables_enterprises()
    populate_tables_sites()
    populate_tables_users()
    return("Initialised tables")

def populate_tables_enterprises():
    print("In populate_tables_enterprises()")
    for ent in ents:
        ent1 = Enterprise(ent[0],ent[1],ent[2],ent[3],ent[4], ent[5])
        db.session.add(ent1)
        db.session.commit()

def populate_tables_sites():
    print("In populate_tables_sites()")
    for site in sites:
        site1 = Site(site[0],site[1],site[2],site[3],site[4], site[5], site[6])
        db.session.add(site1)
        db.session.commit()

def populate_tables_users():
    print("In populate_tables_users()")
    for user in users:
        print(user[0],user[1],user[2],user[3])
        user1 = EUser(user[0],user[1],user[2],user[3])
        db.session.add(user1)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    #with app.app_context():
    #    query_enterprise_all()
