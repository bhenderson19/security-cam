import smtplib
from email.message import EmailMessage
from load_creds import load_creds

creds = load_creds()

def send_email(msg):
	user = creds[0]
	password = creds[1]

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()

	msg['from'] = user

	server.login(user,password)
	server.send_message(msg)

	del msg['from']
	server.quit()

if __name__ == '__main__':
	msg = EmailMessage()
	msg.set_content("Hello World")
	msg['subject'] = "Hello"
	msg['to'] = creds[2]
	sent = False
	while not sent:
		try:
			send_email(msg)
			sent = True
		except:
			pass
