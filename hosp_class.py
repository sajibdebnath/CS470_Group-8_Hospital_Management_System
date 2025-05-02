# Updated hosp_class.py to include required 6+ entities
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://S25_mzhz100:ga35zZSm@oracle2.wiu.edu:1521/?service_name=orclpdb1'
db = SQLAlchemy(app)

# PATIENT ENTITY 
class Patient(db.Model):
    pno = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), nullable=False)
    pgender = db.Column(db.String(10), nullable=False)
    page = db.Column(db.Integer, nullable=False)
    pward = db.Column(db.String(20), nullable=False)
    pstatus = db.Column(db.String(20))

# DOCTOR ENTITY
class Doctor(db.Model):
    dno = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(20))

# DEPARTMENT ENTITY
class Department(db.Model):
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)
    floor = db.Column(db.String(20))
    head = db.Column(db.String(50))

# APPOINTMENT ENTITY
class Appointment(db.Model):
    appt_id = db.Column(db.Integer, primary_key=True)
    pno = db.Column(db.Integer, db.ForeignKey('patient.pno'))
    dno = db.Column(db.Integer, db.ForeignKey('doctor.dno'))
    appt_date = db.Column(db.Date, nullable=False)
    appt_time = db.Column(db.String(20), nullable=False)

# ROOM ENTITY
class Room(db.Model):
    room_no = db.Column(db.String(10), primary_key=True)
    room_type = db.Column(db.String(20), nullable=False)
    is_occupied = db.Column(db.String(5))  # Yes/No

# BILLING ENTITY
class Billing(db.Model):
    __tablename__ = 'billing'
    bill_id = db.Column(db.Integer, primary_key=True)
    pno = db.Column(db.Integer)
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(20))
    paid_status = db.Column(db.String(10))
    status = db.Column(db.String(20))


