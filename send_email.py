"""The first step is to create an SMTP object, each object is used for connection
with one server."""
import getpass
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
password = getpass.getpass("Password:")
#Next, log in to the server
server.login("peterf.meckiffe@gmail.com", password)

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("peterf.meckiffe@gmail.com", "peterf.meckiffe@gmail.com", msg)
