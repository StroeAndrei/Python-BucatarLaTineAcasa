from flask import Flask, render_template, redirect, flash, url_for, \
request
from ContactForm import Contact
from helpers import write_to_contactCSV
import os
from flask_mail import Mail
from flask_mail import Message

# Instanta aplicatiei Flask
app = Flask(__name__)

# Hash folosit pentru securitatea sesiunii
app.config['SECRET_KEY'] = "9854429361c321ea308e302bec05db58"

# Constante folosite pentru a trimite email-uri
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('GMAIL_ADDR_AFU')
app.config['MAIL_PASSWORD'] = os.environ.get('GMAIL_PASS_AFU')

# Instanta extensiei Mail
mail = Mail(app)

@app.route("/")
@app.route("/index")
@app.route("/homepage")
def homepage():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
	contact_form = Contact()

	if contact_form.validate_on_submit():
		# Salvam datele de contact in format .csv
		write_to_contactCSV(request.form.to_dict())
  
		msg = Message(
			'Mesaj - Contact',
			sender=os.environ.get('GMAIL_ADDR_AFU'),
			recipients=['andreistroe1988@gmail.com']
		)

		msg.html = f'''
		<p><b>Mesaj primit de la:</b> {contact_form.email.data}</p>
  		<p><b>Subiect:</b> <b>{contact_form.subject.data}</b></p>
  		<p><b>Mesaj:</b> <b>{contact_form.message.data}</b></p>
		'''
 
		mail.send(msg)
  
		flash("Mesajul a fost transmis.", "success")
		return redirect(url_for('contact'))

	return render_template(
		"contact.html", 
		contact_form=contact_form
	)

@app.route("/project")
def project():
	return render_template("project.html")

@app.route("/services")
def services():
	return render_template("services.html")


