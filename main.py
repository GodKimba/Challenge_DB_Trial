from flask import Flask, Response, Request
from flask_sqlalchemy import SQLAlchemy
from connection import create_connection, close_connection
import mysql.connector
import json

def main():
    con = create_connection("localhost", "root", "masterkey", "SntAgstDB")


    close_connection(con)

if __name__ == "__main__":
    main()


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:8080/santoAgostinho'

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(200))

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(200))
    acronym = db.Column(db.String(2))

class Students_Courses(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    school_year = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    class_id = db.Column(db.String(1))
    number = db.Column(db.Integer)

