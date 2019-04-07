What is Alleviate?

Alleviate is a platform and model for a standardized health record system. Based in SQL, the primary advantage is to offer doctors and patients quick, easy, and secure access and transfer of health records. 
The platform consists of a:
-SQL backend
-Webapp for patient access to personal info
-JavaFX/Java Application for medical staff

Inspiration
Sharing and accessing personal medical records in 2019 is still a complicated process, implementing outdated security measures and lacking uniform, easy record access. Sibel is a military spouse and knows the troubles of moving every few years, having to personally maintain her own medical history and sharing with each new doctor when she moves. Ashley experienced the difficultly of accessing medical records herself recently as well when her boyfriend was in the emergency room for an injury and was asked about his immunization history. Unsure, they stayed on the line with their PCP for an hour before finally acquiring the information they needed. There is a clear need for a better system.

What it does
Alleviate is a platform, but it also provides a model/standard for data that allows other similar platforms to develop and implement the same standard data structures in the back end, enabling easy transfer/migration of data between systems.

Physicians side allows medical staff to log in the application, enter the DOB and phone number of a patient, and access their records. For security, the application only allows modification/ viewing of one patient's records at a time. Medical staff can access a returning patient's records or create a new user in their system, gain patient approval to access medical records by verifying personal information and having them fill out an electronic form. The staff can then implement a threaded record pull, searching other hospital's linked databases for the user's prior history, pulling it, and moving its primary host to the new hospital's server (and beginning decentralized storage process based on the new primary hospital). Creating a completely new user (never been to the hospital before/ no records found) is possible as well, and a registration link will be sent to the patient's email upon record creation at the hospital to sign up and view their records online at will if desired.

Patients side will offer the patient's medical records online after a patient agrees to a consent form. The patient can easily access their medical information if needed, however they cannot modify anything other than contact information. The portal will use two factor authentication each time.

How I built it
We used Java and JavaFX for the Physician's side application. Python, Bootstrap, HTML, and CSS were used for the web app. The backend was implemented in SQL and Flask.

Challenges I ran into
Our biggest challenges were overcoming typical bugs, lack of time, and lack of experience.

Accomplishments that I'm proud of
We're proud of implementing this app on a time crunch after changing projects at 6PM the day before. Our app isn't fully functional yet but we have a stable, growing skeleton that we are proud of.

What I learned
We learned how to implement CSS on a Javafx file, set up a local SQL database, and create a login form for a webapp.

What's next for Alleviate Health Record System
Large scale implementation, better security, and an integrated schedule project.

Built With
java
sql
python
html
css
bootstrap
flask
