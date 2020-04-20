#there are 2 type of procols used in this
#UDP - connection less
#tcp- connection oriented
#range of port number is - 0_-65535



import  socket   #importing the sockets

s=socket.socket()  # in this we can pass the ip adress ipv4 or ipv6 & type of protocol UDP , TCP

print("socket created")

s.bind(('localhost', 9999))   # binding the socket using bind function  in this we can pass ip  if server & client is on diffrerent machine & port no. if client & server is on same machine then pass local host

s.listen(3)
print("waiting for connection")

while True:
    c, addr= s.accept()
    name=c.recv(1024).decode()
    print("connect with: ",addr,name)

    c.send(bytes("welcome to new server",'Utf-8'))

    c.close()