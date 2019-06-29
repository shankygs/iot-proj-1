from flask import Flask, redirect, url_for, request, render_template
import requests
import os

from models import *

app = Flask(__name__)

POSTGRES = {
    'user': 'SHANKY',
    'pw': 'root123',
    'db': 'SHANKY',
    'host': 'localhost',
    'port': '5432',
}
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)
#db.create_all()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process_ent_data', methods=["POST"] )
def process_ent_data():
	EntID=request.form.get('EntID')
	EntName=request.form.get('EntName')
	EntCity=request.form.get('EntCity')
	EntRegion=request.form.get('EntRegion')
	EntCountry=request.form.get('EntCountry')
	EntZip=request.form.get('EntZip')
	print("Enterprise ID:      " + EntID)
	print("Enterprise Name:    " + EntName)
	print("Enterprise City:    " + EntCity)
	print("Enterprise Region:  " + EntRegion)
	print("Enterprise Country: " + EntCountry)
	print("Enterprise ZIP:     " + EntZip)
	return "Received Enterprise from page"

@app.route('/get_enterprises_data', methods=["GET"] )
def get_enterprises_data():
    resp = requests.request('GET', 'http://127.0.0.1:5000/get/enterprise')
    print(resp.status_code)
    return(resp.json())
    #return "Received request from page"

@app.route('/process_site_data', methods=["POST"] )
def process_site_data():
	SiteID=request.form.get('SiteID')
	SiteName=request.form.get('SiteName')
	SiteCity=request.form.get('SiteCity')
	SiteCountry=request.form.get('SiteCountry')
	SiteArea=request.form.get('SiteArea')
	SiteZip=request.form.get('SiteZip')
	print("Site ID:      " + SiteID)
	print("Site Name:    " + SiteName)
	print("Site Country: " + SiteCountry)
	print("Site City:    " + SiteCity)
	print("Site Area:    " + SiteArea)
	print("Site ZIP:     " + SiteZip)
	return "Received Site data from page"

@app.route('/process_devType_data', methods=["POST"] )
def process_devType_data():
	TypeID=request.form.get('devTypeID')
	TypeName=request.form.get('devTypeName')
	GroupID=request.form.get('GroupID')
	GroupName=request.form.get('GroupName')
	HLevel=request.form.get('HLevel')
	ParName1=request.form.get('ParName1')
	ParName2=request.form.get('ParName2')
	ParName3=request.form.get('ParName3')
	ParName4=request.form.get('ParName4')
	ParName5=request.form.get('ParName5')
	ParName6=request.form.get('ParName6')
	ParName7=request.form.get('ParName7')
	ParName8=request.form.get('ParName8')
	ParName9=request.form.get('ParName9')
	ParName10=request.form.get('ParName10')
	print("Device Type:     " + TypeName)
	print("Device ID:       " + TypeID)
	print("Device Group:    " + GroupName)
	print("Device Group ID: " + GroupID)
	print("Hierarchy Level: " + HLevel)
	print("Parameter #1:    " + ParName1)
	print("Parameter #2:    " + ParName2)
	print("Parameter #3:    " + ParName3)
	print("Parameter #4:    " + ParName4)
	print("Parameter #5:    " + ParName5)
	print("Parameter #6:    " + ParName6)
	print("Parameter #7:    " + ParName7)
	print("Parameter #8:    " + ParName8)
	print("Parameter #9:    " + ParName9)
	print("Parameter #10:   " + ParName10)
	return "Received Device Type from page"


@app.route('/process_dev_data', methods=["POST"] )
def process_dev_data():
	DeviceID=request.form.get('devID')
	DevName=request.form.get('devName')
	DevEntID=request.form.get('EntName')
	DevSiteID=request.form.get('SiteName')
	DevTypeID=request.form.get('TypeName')
	DevParentID=request.form.get('devParentName')
	print("Device Name:     " + DevName)
	print("Device ID:       " + DeviceID)
	print("Enterprise ID:    " + DevEntID)
	print("Site ID: " + DevSiteID)
	print("Device Type ID: " + DevTypeID)
	print("Device Parent ID:    " + DevParentID)
	return "Received Device Data from page"
#@app.route('/success/<name>')
#def success(name):
#	return "Success: Welcome %s" %name

#@app.route('/login', methods=['GET','POST'])
#def login():
#	if request.method == 'POST':
#		user = request.form['nm']
#		return redirect(url_for('success', name=user))
#	else:
#		user = request.args.get('nm')
#		return redirect(url_for('success', name=user))

if __name__ == '__main__':
	app.run()
