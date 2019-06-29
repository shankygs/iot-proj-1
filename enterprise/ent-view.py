from flask import Flask, redirect, url_for, request, render_template
from flask import jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/v1/get/enterprise/all', methods=["GET"] )
def get_enterprises_data():
    resp = requests.request('GET', 'http://127.0.0.1:5000/api/v1/get/enterprise/all')
    print(resp.status_code)
    return(jsonify(resp.json()))

if __name__ == '__main__':
	app.run(debug=True, port=5001)
