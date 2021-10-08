import base64
from socket import *
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# username and password for later
username = "temp4softwareeng@gmail.com"
password = "Asdf@0523"

# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
# using gmail as mail client
mailserver = "smtp.gmail.com"
# 465 for ssl connection
serverport = 465
# TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# wrap socket in SSL security
clientSocket = ssl.wrap_socket(clientSocket)
# connect with server
clientSocket.connect((mailserver, serverport))

#Fill in end

# testing to see if server is connected
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response. heloCommand = 'HELO Alice\r\n' clientSocket.send(heloCommand.encode())
# sending EHLO command to test what security authorization is allowed
heloCommand = 'EHLO Saumya\r\n'
clientSocket.send(heloCommand.encode())
# receiving response from server
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.

# Fill in start
# using AUTH LOGIN to sign in to gmail
clientSocket.send("AUTH LOGIN\r\n".encode())
# checking for response asking for username
recv = clientSocket.recv(1024).decode()
print(recv)

# converting username to base64 and sending to server
bytes = username.encode("ascii")
base64_bytes = base64.b64encode(bytes)
base64_msg = base64_bytes.decode("ascii")
clientSocket.send(f"{base64_msg}\r\n".encode())
# checking response asking for password
recv = clientSocket.recv(1024).decode()
print(recv)

# converting password to base64 and sending to server
bytes = password.encode("ascii")
base64_bytes = base64.b64encode(bytes)
base64_msg = base64_bytes.decode("ascii")
clientSocket.send(f"{base64_msg}\r\n".encode())
# checking for accepted sign in
recv = clientSocket.recv(1024).decode()
print(recv)

# writing from message to server
clientSocket.send('MAIL FROM: <temp4softwareeng@gmail.com>\r\n'.encode())
# checking for ok response
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
# writing sending to message to server
clientSocket.send("RCPT TO: <saumya.buch@gmail.com>\r\n".encode())
# checking response
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in end


# Send DATA command and print server response.

# Fill in start
# sending DATA message to server
clientSocket.send("DATA\r\n".encode())
recv3 = clientSocket.recv(1024).decode()
# checking for go ahead to write message
print(recv3)
if recv3[:3] != '354':
    print('354 reply not received from server.')

# Fill in end


# Send message data.

# Fill in start
# sending message to server
clientSocket.send("HI SAUMYA\r\n".encode())
clientSocket.send("THIS IS A TEST\r\n".encode())
clientSocket.send(msg.encode())

# Fill in end

# Message ends with a single period.

# Fill in start
# letting server know message is over
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
# checking for ok message
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send QUIT command and get server response.

# Fill in start
# quiting connection to mail server
clientSocket.send("QUIT\r\n".encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '221':
    print('221 reply not received from server.')
# closing port
clientSocket.close()
# Fill in end
