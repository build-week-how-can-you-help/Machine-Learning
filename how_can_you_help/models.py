""" SQL Alchemy models for the app """
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Organization(DB.Model):
    """ charity organization names """

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)
    text = DB.Column(DB.Unicode(1500), nullable=False)
    embedding = DB.Column(DB.PickleType, nullable=False)
    website = DB.Column(DB.String(50), nullable=False)
    address = DB.Column(DB.String(50), nullable=False)
    city = DB.Column(DB.String(20), nullable=False)
    zip_code = DB.Column(DB.Numeric, nullable=False)

    def __repr__(self):
        return "<Organization {}".format(self.name)
