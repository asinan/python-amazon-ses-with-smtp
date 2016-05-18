#!/usr/bin/python
import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = 'send@mail.com'
toaddrs  = 'to@mail.com'
msg = """ From: From Person <send@mail.com>
To: To Person <to@mail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP Amozon SES test

This is a test e-mail message.

<b>Hello</b>.
"""

print ("Message length is " + repr(len(msg)))

#Change according to your settings
smtp_server = 'x'
smtp_username = 'x'
smtp_password = 'x
smtp_port = '587'
smtp_do_tls = True

server = smtplib.SMTP(
    host = smtp_server,
    port = smtp_port,
    timeout = 10
)
server.set_debuglevel(10)
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, msg)
print (server.quit())
