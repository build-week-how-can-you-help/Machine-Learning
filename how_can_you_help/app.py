""" main application and routing logic for BW skeleton """

from flask import Flask, render_template, request
from .models import DB, Organization
from .process import find_organizations





def create_app():
    """ create and configure instance of flask app """

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    DB.init_app(app)

    @app.route("/")
    def root():
        return render_template("layout.html", title="CharityBW")

    @app.route("/find", methods=["POST"])
    def find():
        
        description_text = request.values['description_text']
        finder = find_organizations(description_text)
        return render_template("find.html", finder=finder)
    


    return app



