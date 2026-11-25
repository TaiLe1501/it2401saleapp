from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
app = Flask(__name__)
app.secret_key = 'JKHGIUGYUF(*&^&*^*YTTDYFJHGH*T^&T*T&GHKJHJGH'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 4

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(cloud_name='ucjihovm',
api_key='687836418475798',
api_secret='GAf-QpoIJ_ssxAHp-wQYENOlBKY')