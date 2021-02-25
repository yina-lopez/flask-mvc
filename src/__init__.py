from flask import Flask

app = Flask(__name__, template_folder='views')

#importando controles todo
from src.controllers import *


def create_app():
    app.run(debug=True) #arrancar la aplicacion