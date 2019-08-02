""" main application and routing logic for BW skeleton """

from flask import Flask, render_template, request
from .models import DB, Organization
from .process import find_organizations
from flask_cors import CORS, cross_origin




def create_app():
    """ create and configure instance of flask app """

    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config['ENV'] = 'prod'
    DB.init_app(app)



    @app.route("/")
    @cross_origin()
    def root():
        return render_template("layout.html", title="CharityBW")

    @app.route("/find", methods=["POST"])
    @cross_origin()
    def find():

        description_text = request.values['description_text']
        finder = find_organizations(description_text)
        return finder



    return app



