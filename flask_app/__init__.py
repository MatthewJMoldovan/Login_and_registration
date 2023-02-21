from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

DATABASE = "login_and_registration_db"
BCRPYT = Bcrypt(app)

app.secret_key = "password"