from email import message
import smtplib
import ssl

# message to be sent
msg = """\
Subject: Hi there


HI SAUMYA
THIS IS A TEST
I love computer networks!."""

# username and password for later
username = "temp4softwareeng@gmail.com"
password = "Asdf@0523"

# using gmail as mail client
mailserver = "smtp.gmail.com"
# 587 for tls connection
serverport = 587

# create ssl context
context = ssl.create_default_context()

# establish connection to server
with smtplib.SMTP(mailserver, serverport) as server:
    server = smtplib.SMTP(mailserver, serverport)
    # test connection
    server.ehlo()
    # secure connection with TLS
    server.starttls(context=context)
    # login to server
    server.login(username, password)
    # message to send
    server.sendmail(username, "saumya.buch@gmail.com", msg)
    # end server connection
    server.quit()
