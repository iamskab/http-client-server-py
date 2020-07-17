import socket
from Crypto.PublicKey import RSA
from Crypto import Random

#Generate private and public keys
random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

#Declartion
mysocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# host = socket.gethostbyname(socket.getfqdn())
host = socket.gethostname()
port = 7777
encrypt_str = "encrypted_message="

'''
if host == "127.0.1.1":
    import commands
    host = commands.getoutput("hostname -I")
'''   

print "host = " + host

#Prevent socket.error: [Errno 98] Address already in use
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mysocket.bind((host, port))

mysocket.listen(5)

c, addr = mysocket.accept()

while True:

    #Wait until data is received.
    data = c.recv(1024)
    data = data.replace("\r\n", '') #remove new line character

    if data == "Client: OK":
        c.send("public_key=" + public_key.exportKey() + "\n")
        print "\nPublic key sent to client."

    elif encrypt_str in data: #Reveive encrypted message and decrypt it.
        data = data.replace(encrypt_str, '')
        print "Received:\n\nEncrypted message = "+str(data)
        encrypted = eval(data)
        decrypted = private_key.decrypt(encrypted)
        c.send("Server: OK")
        print "\nDecrypted message = " + decrypted

    elif data == "Quit": break

#Server to stop
c.send("Server stopped\n")
print "\nServer stopped"
c.close()










'''
import socket 

s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
HOST = socket.gethostname() 
PORT = 1024

s.bind((HOST , PORT))
s.listen(5) 
print "This is Python Programming "

while True:
    conn , adr = s.accept()
    print "Connection to {adr} established"
    conn.sendall("Client-Server-Crypto" )
    conn.close()

'''    
