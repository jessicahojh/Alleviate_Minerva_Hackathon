from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
import os
from flask_sqlalchemy import SQLAlchemy
from model import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


@app.route('/', methods=['GET'])
def homepage():



    return render_template("homepage.html")

@app.route('/', methods=['POST'])
def get_form_data():

    email = request.form["email"]
    password = request.form["password"]


    return redirect("/portal")


@app.route('/portal')
def show_portal():

    # patient_id = session.get("patient_id")

    # patient = Patient.query.filter_by(name="Jane Doe").name

    # visit = Visit.query.filter_by(patient_id=patient_id).first()
    # date = visit.date 
    # note = visit.note

    # doctor_id = visit.doctor_id
    # doctor = Doctor.query.get(doctor_id).name

    # stat = Stat.query.filter_by(patient_id=patient_id).first()
    # height = stat.height
    # weight = stat.weight
    # heart_rate = stat.heart_rate

    # prescription = Prescription.query.filter_by(patient_id=patient_id).first()
    # prescription_name = prescription.name
    # prescription_dosage = prescription.dosage 

    # immunization = Immunization.query.filter_by(pateint_id=patient_id).first()
    # immunization_name = immunization.name

    # referral = Referral.query.filter_by(patient_id=patient_id).first()
    # referred_doctor = referral.referred_doctor
    # specialty = referral.specialty



    return render_template("portal.html", 
                           )




if __name__ == '__main__':

    app.run(port=5000, host='0.0.0.0', debug=True)