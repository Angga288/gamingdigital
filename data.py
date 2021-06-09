import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def kirim(dari,kepada,judul,isi,pw):
	fromaddr = dari
	toaddr = kepada
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = judul
	body = isi
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, pw)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()


