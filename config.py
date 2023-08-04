from flask import Flask
# pip install SQLAlchemy
# from sqlalchemy import create_engine,text
# import pymysql
import pickle
import os


app = Flask(__name__)

# crating db connection
# engine = create_engine("mysql+pymysql://root:Kunal_root1@localhost/ati_flask_db")

model_path = r'artifact/pipe.pkl'
predict_pipe = pickle.load(open(model_path,'rb'))

PORT_NUMBER = 8080
HOST_NAME = "0.0.0.0"

