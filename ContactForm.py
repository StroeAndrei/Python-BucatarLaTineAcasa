from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

class Contact(FlaskForm):
	email = EmailField(label="email", id="email", 
		validators=[DataRequired(message="Trebuie completat."), Email(), Length(min=3, max=150, message="Adresa de email nu este corecta.")])

	subject = StringField(label="subject", id="subject",
		validators=[DataRequired(message="Trebuie completat."), Length(min=3, max=150, message="Subiectul nu are dimensiunea corecta.")])
	
	message = TextAreaField(label="message", id="message",
		validators=[DataRequired(message="Trebuie completat."), Length(min=3, max=1000, message="Mesajul nu are dimensiunea corecta.")])

	submit = SubmitField('Trimite')