from flask import render_template, flash, redirect, url_for, json
from flask import jsonify
import requests

from ui import app
from ui.forms import LoginForm
from ui.forms import RegistrationForm

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/logout')
def logout():
	flash('Logout Successful!!!')
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print("Login :" + form.username.data + form.password.data)
		flash('Login requested by user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		json_reg_form ={
					'username':form.username.data,
					'password':form.password.data
				   }
		resp = requests.post('http://127.0.0.1:5000/api/v1/validate/user', data=json_reg_form)
		print(resp.status_code)
		if resp.status_code < 300:
			flash('Login is Successful!!!')
			return render_template('start.html', title='Main Application')
		flash('Login Failed: Error in Username or Password !!!')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		#user = User(username=form.username.data, email=form.email.data)
		#user.set_password(form.password.data)
		#db.session.add(user)
		#db.session.commit()
		print("UserName :" + form.username.data)
		print("Email:    " + form.email.data)
		print("Password: " + form.password.data)
		json_reg_form ={
							'username':form.username.data,
					  		'email'   :form.email.data,
							'password':form.password.data
					   }
		print (json.dumps(json_reg_form))
		#headers = {'content-type': 'application/json'}
		resp = requests.post('http://127.0.0.1:5000/api/v1/add/user', data=json_reg_form)
		#resp = requests.request('POST', 'http://127.0.0.1:5000/add/user')
		flash('Congratulations, you are now a registered user!!!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Regsiter', form=form)
