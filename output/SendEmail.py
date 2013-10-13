"""The first step is to create an SMTP object, each object is used for connection
with one server."""
import smtplib
from email.mime.text import MIMEText

def sendMail(email_address, email_body):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	#Next, log in to the server
	server.login("languagelistcreator@gmail.com", "Kangaroo66")
	msg = MIMEText(email_body.encode("utf-8"), 'html', "utf-8")
	msg['Content-Type'] = "text/html; charset=utf-8"
	#Send the mail
	server.sendmail("languagelistcreator@gmail.com", email_address, msg.as_string())
	server.quit()

