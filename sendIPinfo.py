from socket import *
import time

IPString = "192.155.21.1"
Host = '192.168.50.229'
Port = 8848

def SendIP(HOST,PORT,IPString):
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect((HOST, PORT))
    logMessage = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "##" + IPString
    s.sendall(logMessage)
    with open('sendIPinfo.log', 'a+') as f:
        f.write(logMessage)
        f.write("\n")
    print logMessage
    s.close()


if __name__ == "__main__":
    SendIP(Host,Port,IPString)