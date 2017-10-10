import socket
import time
import sys
import binascii
from subprocess import call
#from time import sleep
import select

start_time = time.time()
# your code
elapsed_time = 0

UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("10.1.169.1",63100)
listen_addr = ("10.1.169.2",63100)
UDPSock.bind(addr)
#UDPSock.settimeout(10)

call (["sudo","hping3","-V","-c","200","--udp","-p","63100","10.1.169.2"])

UDPSock.sendto("aaa",listen_addr)

while (elapsed_time < 30):
  
  data = UDPSock.recv(1024)
  UDPSock.sendto(data,addr)
  elapsed_time = time.time() - start_time

print data
s = int(data)
prr = s/float(200)
print prr

#time.sleep = 1
