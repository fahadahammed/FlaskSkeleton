from flask import request, render_template, url_for
from flask import redirect, session

from {PROJECT_NAME} import app



@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return "Welcome to {PROJECT_NAME} !!!"
