from enum import unique
from application import db
from flask import Flask, render_template, request


# schema for database
class Results(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(25),nullable=False)
    patt = db.Column(db.Integer,nullable=False)
    pdef = db.Column(db.Integer,nullable=False)
    ename = db.Column(db.String(25),nullable=False)
    eatt = db.Column(db.Integer,nullable=False)
    edef = db.Column(db.Integer,nullable=False)
    outcome = db.Column(db.String(10),nullable=False)