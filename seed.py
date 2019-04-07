from model import *
from sqlalchemy import func
from server import app

def load_data():

    Jane = Patient(name="Jane Doe", email="jane@gmail.com", password="irock", phone_number="4151234567", dob="1/1/1993")

    Dr_Octocat = Doctor(name="Dr. Octocat", doc_type="Primary")

    Dr_Rex = Doctor(name="Dr. Rex", doc_type="Specialist")

    patient_doc = Patient_doc_relationship(patient_id="1", doctor_id="1")

   #  referral1 = Referral(doctor_who_referred="1", specialty="Bones", referred_doctor="2", patient_id="1")

    amoxicillin = Prescription(name="amoxicillin", dosage="100mg", date="Jan 1, 2019", doctor_id="1", patient_id="1")

    visit1 = Visit(date="Jan 1, 2019", doctor_id="1", patient_id="1", notes="Prescribed medicine for ear infection.")

    stat1 = Stat(height="5 Feet 3 Inches", weight="115", heart_rate="65 BPM", patient_id="1")

    immunization1 = Immunization(date="January 1, 2019", name="Tetanus Shot")

    db.session.add(Jane)
    db.session.add(Dr_Octocat)
    db.session.add(Dr_Rex)
    db.session.add(patient_doc)
   #  db.session.add(referral1)
    db.session.add(amoxicillin)
    db.session.add(visit1)
    db.session.add(stat1)
    db.session.add(immunization1)
   
    db.session.commit()
    
if __name__ == "__main__":

   connect_to_db(app)
   db.create_all()
   load_data()

    