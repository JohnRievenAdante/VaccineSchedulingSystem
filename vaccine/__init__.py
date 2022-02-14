from flask import Flask, render_template,redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root','123456','localhost' ,'vaccine_system')

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI']=conn
db=SQLAlchemy(app)
from vaccine import routes