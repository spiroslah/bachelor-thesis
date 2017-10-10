import socket
import sys
import select

packets = 0
# A UDP server

# Set up a UDP server
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Listen on port 21567
# (to all IP addresses on this system)
#listen_addr = ("10.1.169.2",63100) #na allaxtei i ip
listen_addr = ("10.1.169.3",63100)
source_addr = ("10.1.169.1", 63100)
router_addr = ("10.1.169.2", 63100)
UDPSock.bind(listen_addr)

# Report on all data packets received and
# where they came from in each case (as this is
# UDP, each may be from a different source and it's
# up to the server to sort this out!)

while (True):
        data,addr = UDPSock.recvfrom(1024)
        if (data == 'aaa'):
	  break
        print addr
        packets= packets + 1
        #elapsed_time = time.time() - start_time

print packets  

UDPSock.sendto(bytes(packets), source_addr)