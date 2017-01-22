from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

import json
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def constructMsg(content, from_addr, password, to_addr, smtp_server):
	msg = MIMEText("%s is available right now" % content, "plain", "utf-8")
	msg["From"] = _format_addr("Cornell Class <%s>" % from_addr)
	msg["To"] = _format_addr('%s <%s>' % (to_addr, to_addr))
	msg["Subject"] = Header("%s status" % content, "utf-8").encode()
	return msg

def sendEmail(content):
	data = {}
	with open("config2.json") as f:
		data = json.load(f)
	from_addr = data["sender"]["email_addr"]
	password = data["sender"]["password"]
	to_addr = data["receiver"]["email_addr"]
	smtp_server = data["sender"]["smtp_server"]
	smtp_port = data["sender"]["smtp_port"]
	msg = constructMsg(content, from_addr, password, to_addr, smtp_server)
	server = smtplib.SMTP_SSL(smtp_server, smtp_port)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
	

def main():
	data = {}
	with open("config.json") as f:
		data = json.load(f)
	sendEmail("CS 3410 is available right now")


if __name__ == '__main__':
	main()