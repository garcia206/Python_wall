from flask import Flask, redirect, request, render_template, flash, session
import re
from connect import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')

app = Flask(__name__)
app.secret_key = 'RObBoss'
db = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
	return render_template('index.html')

app.run(debug=True)
