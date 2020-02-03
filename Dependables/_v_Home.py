from flask import request, render_template, url_for
from flask import redirect, session, jsonify

from PROJECTNAMEFSKLTN import app
from PROJECTNAMEFSKLTN.Model._m_Home import _m_Home


@app.route("/", methods=["GET"])
def _v_home():
    if request.method == "GET":
        to_return = _m_Home().get_data()
        return render_template(template_name_or_list="Home.html", to_return=to_return)


@app.route("/api", methods=["GET"])
@app.route("/api/", methods=["GET"])
def _v_home_api():
    if request.method == "GET":
        to_return = _m_Home().get_data()
        return jsonify(to_return)



