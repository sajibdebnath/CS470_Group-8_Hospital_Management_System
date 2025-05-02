from oracledb.exceptions import IntegrityError

from flask import render_template, request, redirect, url_for
from hosp_class import *
from datetime import datetime

@app.route("/")
def about():
    return render_template("FLStack.html")

@app.route("/doctor", methods=["GET", "POST"])
def manage_doctor():
    if request.method == "POST":
        dno = request.form.get("dno")
        dname = request.form.get("dname")
        specialization = request.form.get("specialization")
        contact = request.form.get("contact")
        doctor = Doctor(dno=dno, dname=dname, specialization=specialization, contact=contact)
        db.session.add(doctor)
        db.session.commit()
    doctors = Doctor.query.all()
    return render_template("doctor.html", doctors=doctors)

@app.route("/doctor/edit/<int:id>", methods=["GET", "POST"])
def edit_doctor(id):
    doctor = Doctor.query.get(id)
    if request.method == "POST":
        doctor.dname = request.form.get("dname")
        doctor.specialization = request.form.get("specialization")
        doctor.contact = request.form.get("contact")
        db.session.commit()
        return redirect(url_for("manage_doctor"))
    return render_template("doctor_edit.html", doctor=doctor)

@app.route("/doctor/delete/<int:id>")
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
    return redirect(url_for("manage_doctor"))

@app.route("/patient", methods=["GET", "POST"])
def manage_patient():
    if request.method == "POST":
        pno = request.form.get("pno")
        pname = request.form.get("pname")
        pgender = request.form.get("pgender")
        page = request.form.get("page")
        pward = request.form.get("pward")
        pstatus = request.form.get("pstatus")
        patient = Patient(pno=pno, pname=pname, pgender=pgender, page=page, pward=pward, pstatus=pstatus)
        db.session.add(patient)
        db.session.commit()

    search_query = request.args.get("search", "")
    if search_query:
        patients = Patient.query.filter(Patient.pname.ilike(f"%{search_query}%")).all()
    else:
        patients = Patient.query.all()
    return render_template("patient.html", patients=patients, search=search_query)

@app.route("/patient/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):
    patient = Patient.query.get(id)
    if request.method == "POST":
        patient.pname = request.form.get("pname")
        patient.pgender = request.form.get("pgender")
        patient.page = request.form.get("page")
        patient.pward = request.form.get("pward")
        patient.pstatus = request.form.get("pstatus")
        db.session.commit()
        return redirect(url_for("manage_patient"))
    return render_template("patient_edit.html", patient=patient)

@app.route("/patient/delete/<int:id>")
def delete_patient(id):
    patient = Patient.query.get(id)
    if patient:
        db.session.delete(patient)
        db.session.commit()
    return redirect(url_for("manage_patient"))

@app.route("/department", methods=["GET", "POST"])
def manage_department():
    if request.method == "POST":
        dept_id = request.form.get("dept_id")
        dept_name = request.form.get("dept_name")
        floor = request.form.get("floor")
        head = request.form.get("head")
        department = Department(dept_id=dept_id, dept_name=dept_name, floor=floor, head=head)
        db.session.add(department)
        db.session.commit()
    departments = Department.query.all()
    return render_template("department.html", departments=departments)

@app.route("/department/edit/<int:id>", methods=["GET", "POST"])
def edit_department(id):
    department = Department.query.get(id)
    if request.method == "POST":
        department.dept_name = request.form.get("dept_name")
        department.floor = request.form.get("floor")
        department.head = request.form.get("head")
        db.session.commit()
        return redirect(url_for("manage_department"))
    return render_template("department_edit.html", department=department)

@app.route("/department/delete/<int:id>")
def delete_department(id):
    department = Department.query.get(id)
    if department:
        db.session.delete(department)
        db.session.commit()
    return redirect(url_for("manage_department"))

@app.route("/appointment", methods=["GET", "POST"])
def manage_appointment():
    if request.method == "POST":
        appt_id = request.form.get("appt_id")
        pno = request.form.get("pno")
        dno = request.form.get("dno")
        appt_date = datetime.strptime(request.form.get("appt_date"), "%Y-%m-%d")
        appt_time = request.form.get("appt_time")
        appointment = Appointment(appt_id=appt_id, pno=pno, dno=dno, appt_date=appt_date, appt_time=appt_time)
        db.session.add(appointment)
        db.session.commit()
    appointments = Appointment.query.all()
    return render_template("appointment.html", appointments=appointments)

@app.route("/appointment/edit/<int:id>", methods=["GET", "POST"])
def edit_appointment(id):
    appointment = Appointment.query.get(id)
    if request.method == "POST":
        appointment.pno = request.form.get("pno")
        appointment.dno = request.form.get("dno")
        appointment.appt_date = datetime.strptime(request.form.get("appt_date"), "%Y-%m-%d")
        appointment.appt_time = request.form.get("appt_time")
        db.session.commit()
        return redirect(url_for("manage_appointment"))
    return render_template("appointment_edit.html", appointment=appointment)

@app.route("/appointment/delete/<int:id>")
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
    return redirect(url_for("manage_appointment"))

@app.route("/room", methods=["GET", "POST"])
def manage_room():
    if request.method == "POST":
        room_no = request.form.get("room_no")
        room_type = request.form.get("room_type")
        is_occupied = request.form.get("is_occupied")
        room = Room(room_no=room_no, room_type=room_type, is_occupied=is_occupied)
        db.session.add(room)
        db.session.commit()
    rooms = Room.query.all()
    return render_template("room.html", rooms=rooms)

@app.route("/room/edit/<string:id>", methods=["GET", "POST"])
def edit_room(id):
    room = Room.query.get(id)
    if request.method == "POST":
        room.room_type = request.form.get("room_type")
        room.is_occupied = request.form.get("is_occupied")
        db.session.commit()
        return redirect(url_for("manage_room"))
    return render_template("room_edit.html", room=room)

@app.route("/room/delete/<string:id>")
def delete_room(id):
    room = Room.query.get(id)
    if room:
        db.session.delete(room)
        db.session.commit()
    return redirect(url_for("manage_room"))

@app.route("/billing", methods=["GET", "POST"])
def manage_billing():
    if request.method == "POST":
        bill_id = request.form.get("bill_id")
        pno = request.form.get("pno")
        amount = request.form.get("amount")
        payment_method = request.form.get("payment_method")
        paid_status = request.form.get("paid_status")
        status = request.form.get("status")
        billing = Billing(bill_id=bill_id, pno=pno, amount=amount, payment_method=payment_method, paid_status=paid_status, status=status)
        db.session.add(billing)
        db.session.commit()
    billings = Billing.query.all()
    return render_template("billing.html", billings=billings)

@app.route("/billing/edit/<int:id>", methods=["GET", "POST"])
def edit_billing(id):
    billing = Billing.query.get(id)
    if request.method == "POST":
        billing.pno = request.form.get("pno")
        billing.amount = request.form.get("amount")
        billing.payment_method = request.form.get("payment_method")
        billing.paid_status = request.form.get("paid_status")
        billing.status = request.form.get("status")
        db.session.commit()
        return redirect(url_for("manage_billing"))
    return render_template("billing_edit.html", billing=billing)

@app.route("/billing/delete/<int:id>")
def delete_billing(id):
    billing = Billing.query.get(id)
    if billing:
        db.session.delete(billing)
        db.session.commit()
    return redirect(url_for("manage_billing"))
