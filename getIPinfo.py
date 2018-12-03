from socket import *

HOST = '192.168.50.229'
PORT = 8848

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
print '...waiting for message..'

while True:
    data, address = s.recvfrom(1024)
    dataType = type(data)
    print data, address
    print dataType

s.close()
