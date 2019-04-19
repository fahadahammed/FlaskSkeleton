from flask import request, render_template, url_for
from flask import redirect, session, jsonify

from {PROJECT_NAME} import app



@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        to_return = {
                "msg": "Welcome to {PROJECT_NAME} !!!"
        }
        return jsonify(to_return)
