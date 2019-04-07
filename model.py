from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy.sql import func
from flask import Flask



db = SQLAlchemy()


class Patient(db.Model):

    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
   
 
    def __repr__(self):

        return f"<Patient patient_id={self.patient_id} name={self.name} email={self.email} password={self.password} phone_number={self.phone_number} dob={self.dob}>"


class Doctor(db.Model):

    __tablename__ = "doctors"

    doctor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    doc_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):

        return f"<Doctor doctor_id={self.doctor_id} name={self.name} doc_type={self.doc_type}>"

class Patient_doc_relationship(db.Model):

    __tablename__ = "patient_doc_relationships"

    relationship_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'))

    patient = db.relationship("Patient", backref="patient_doc_relationships")
    doctor = db.relationship("Doctor", backref="patient_doc_relationships")

    def __repr__(self):

        return f"<Patient_doc_relationship relationship_id={self.relationship_id} patient_id={self.patient_id} doctor_id={self.doctor_id}>"

# class Referral(db.Model): 

#     __tablename__ = "referrals"

#     referral_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     doctor_who_referred = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'))
#     specialty = db.Column(db.String(50), nullable=False)
#     referred_doctor = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'))
#     patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))

#     patient = db.relationship("Patient", backref="referrals")
#     doctor = db.relationship("Doctor", backref="referrals")
#     doctor_who_referred = db.relationship("Doctor", backref="referrals")

#     def __repr__(self):

#         return f"<Referral referral_id={self.referral_id} name={self.doctor_who_referred} specialty={self.specialty} referred_doctor={self.referred_doctor}>"

class Prescription(db.Model):

    __tablename__ = "prescriptions"

    prescription_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    date = db.Column(db.TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))

    patient = db.relationship("Patient", backref="prescriptions")
    doctor = db.relationship("Doctor", backref="prescriptions")

    def __repr__(self):

        return f"<Prescription {self.prescription_id} for {self.name}, Dose={self.dosage}, Date={self.date}, doctor={self.doctor_id}>"


class Visit(db.Model):

    __tablename__ = "visits"

    visit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))
    notes = db.Column(db.String(1000), nullable=True)

    patient = db.relationship("Patient", backref="visits")
    doctor = db.relationship("Doctor", backref="visits")

    def __repr__(self):

        return f"<Visit {self.visit_id}, user={self.user_id}, {self.date}, doctor={self.doctor_id}, notes={self.notes}>" 



class Stat(db.Model):  

    __tablename__ = "stats"

    stats_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    height = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    heart_rate = db.Column(db.String(5000), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))


    patient = db.relationship("Patient", backref="stats")


    def __repr__(self):

        return f"<Stat stats_id={self.stats_id} height={self.height} weight={self.weight} heart_rate={self.heart_rate} patient_id={self.patient_id}>"

class Immunization(db.Model):

    __tablename__ = "immunizations"

    immunization_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    name = db.Column(db.String(50))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))

    patient = db.relationship("Patient", backref="immunizations")


    def __repr__(self):

        return f"<Immunization immunization_id={self.immunization_id} date={self.date} immunization_name={self.immunization_name}>"


##############################################################################

def connect_to_db(app):
  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///health'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
  
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
    