from flask import Flask
import re

app = Flask(__name__)

DATABASE = "login_and_registration_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "boogienights"
