from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

#@app.route('/hello/<name>')
#def hello(name):
#	return "Hello from %s!" %name

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
