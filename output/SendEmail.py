"""The first step is to create an SMTP object, each object is used for connection
with one server."""
import getpass
import smtplib

def sendMail(email_address, email_body):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	#Next, log in to the server
	server.login("languagelistcreator@gmail.com", "Kangaroo66")

	#Send the mail
	msg = "\n"+email_body # The /n separates the message from the headers
	server.sendmail("languagelistcreator@gmail.com", email_address, msg)

