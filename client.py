import socket
from Crypto.PublicKey import RSA

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# socket.getaddrinfo('127.0.0.1', 8080)
host = socket.gethostname()
port = 7777

server.connect((host, port))

#Tell server that connection is OK
server.sendall("Client: OK")

#Receive public key string from server
server_string = server.recv(1024)

#Remove extra characters
server_string = server_string.replace("public_key=", '')
server_string = server_string.replace("\r\n", '')

#Convert string to key
server_public_key = RSA.importKey(server_string)

#Encrypt message and send to server
message = "This is my secret ENCRYPTED message."
encrypted = server_public_key.encrypt(message, 32)
server.sendall("encrypted_message="+str(encrypted))

#Server's response
server_response = server.recv(1024)
server_response = server_response.replace("\r\n", '')
if server_response == "Server: OK":
    print "Server decrypted message successfully"

#Tell server to finish connection
server.sendall("Quit")
print(server.recv(1024)) #Quit server response
server.close()







'''
import socket 

s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
HOST = socket.gethostname() 
PORT = 1024
s.connect((HOST , PORT))

msg = s.recv(1024)
data = msg

print data
'''