import os
from flask import Flask
from dotenv import load_dotenv


# Initialization

## Set Environment Variables
load_dotenv()

## Set Flask
app = Flask(__name__)

# Routes

## Homepage

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World. It\'s ' + os.getenv("APP_NAME")
