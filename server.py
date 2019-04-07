@app.route('/portal')
def show_portal():

    patient_id = session.get("patient_id")

    patient = Patient.query.get(patient_id)

    date = Visit.query.filter_by(patient_id=patient_id).first()





    return render_template("portal.html") 