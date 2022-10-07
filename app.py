import os
from flask import Flask, render_template
from dotenv import load_dotenv


# Initialization

## Set Environment Variables
load_dotenv()

## Set Flask
app = Flask(__name__)

# Routes

## Homepage

@app.route('/', methods=['GET'])
def home():
    appName = os.getenv("APP_NAME")
    welcomeText = "Hello, World. It's " + appName

    return render_template('home.html', appName=appName, textFromBackend=welcomeText)
