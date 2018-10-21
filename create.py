from flask import Flask, redirect, url_for, request, render_template, json
from flask import jsonify
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


#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

def create_tables():
    print("In create_tables()")
    db.create_all()
    #for ent in ents:

def clear_tables():
    db.session.query(Site).delete()
    db.session.query(Enterprise).delete()
    db.session.commit()
    #for ent in ents:

def populate_tables_all():
    print("In populate_tables_all()")
    populate_tables_enterprises()
    populate_tables_sites()

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

def query_enterprise_all():
    print("In query_enterprise_all()")
    ents = db.session.query(Enterprise).all()
    for ent in ents:
        print (ent.EntID, ent.EntName, ent.EntCity, ent.EntRegion, ent.EntCountry, ent.EntZip)
        e = jsonify({
        "entID"     : ent.EntID,
        "entName"   : ent.EntName,
        "entCity"   : ent.EntCity,
        "entRegion" : ent.EntRegion,
        "entCountry": ent.EntCountry,
        "entZip"    : ent.EntZip
        }
        )
        print(e)

        #ent.to_json();
        #print(json.dumps([dict(e) for e in ent])
        #print (jsonify(ent))

if __name__ == "__main__":
    with app.app_context():
        query_enterprise_all()
