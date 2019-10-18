from flask import Flask

app = Flask(__name__)

from program import routes   # do not understand why this has to be after initializing app?