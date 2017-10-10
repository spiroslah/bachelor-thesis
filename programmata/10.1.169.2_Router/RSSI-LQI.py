import socket
import time
import subprocess
import sys
import datetime

#an 'int' variable specifying seconds for .sleep()
#tm = 2
#a 'boolean' type variable for random use
#check = False
#a list of all the characters that represent a numeric value
#tup1 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )
tup2 = ('a', 'b')

#showing time and date
pf_t = ('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
print '\n' + pf_t + '\n'

'''
#asking user for input

input = raw_input('Please give me the number of repetitions ' + '\n')
#print type(input)
#breaking user's input in single characters and storing them in a list 
list_1 = list(input)
#print list_1

while check != True :
    
    #finding the length of the list
    in_len = len(list_1)
    
    #printing dots while waiting
    dot = '.'
    sys.stdout.write('Checking your input')
    
    for i in range(0,3):
	sys.stdout.write( dot )
	sys.stdout.flush()
	time.sleep(1)
	
    sys.stdout.flush()
    print ' '
    
    #checking if every element of the list is a character from 0 to 9
    i = 0
    for i in range(0, in_len):
	
	check = list_1[i] in tup1
	if check == False:
	    break
	#print type(input)
	#print list_1 = list(input)
    
    #if the input is not numeric ask for input again
    if check == False:
      
	print 'Sorry, I only accept numbers sir'
	time.sleep(2)
	input = raw_input('Please give me the number of repetitions again ' + '\n')
	#print type(input)
	list_1 = list(input)
	
    #if the input is numeric but larger than a certain threshold ask for input again
    elif int(input) > 20:
      
	print "Not so many sir, I am tired...less please"
	time.sleep(2)
	check = False
	input = raw_input('Please give me the number of repetitions again ' + '\n')
	list_1 = list(input)

#the input has been checked and the programm is ready to continue
print "Got it...let's proceed"

rep_num = input
time.sleep(tm)
'''




#Anoigoume socket
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

listen_addr = ("10.1.169.2",63100)
source_addr = ("10.1.169.1",63100)
dest_addr = ("10.1.169.3",63100)
UDPSock.bind(listen_addr)
'''
UDPSock.sendto(bytes(rep_num), source_addr)
UDPSock.sendto(bytes(rep_num), dest_addr)
'''


i = []
while True:
    data = UDPSock.recv(1024)
    i.append(data)
    if len(i)>=4:
	break

for item in i: 
	if item[-1] in tup2:
	    if item[-1] == 'a':
		#item.replace('a', '')
		s1 = item.split("/")
		LQI_source = s1[0]
		RSSI_source = s1[1] 
	    if item[-1] == 'b':
		#item.replace('b', '')
		s2 = item.split("/")
		LQI_dest = s2[0]
		RSSI_dest = s2[1]

print "Ta apotelesmata tou source einai LQI: " + LQI_source + " kai RSSI: " + RSSI_source
print "Ta apotelesmata tou destination einai LQI: " + LQI_dest + " kai RSSI: " + RSSI_dest

rs = RSSI_source.replace('a', '')
rd = RSSI_dest.replace('b', '')
LQI_source = float(LQI_source)
RSSI_source = float(rs)
LQI_dest = float(LQI_dest)
RSSI_dest = float(rd)


while True:
    metric = raw_input("Dwse RSSI i LQI gia ton antistoixo elegxo: ")
    if metric == 'LQI' or metric == 'RSSI':
      break
    else: print "Parakalw dwste LQI i RSSI"
##########################################################
#################### TOUS ELEGXOUS #######################
##########################################################


if metric == 'LQI':
    if LQI_dest >= 40 and LQI_source >= 40:
	print 'To robot einai se oikanopoiitiki thesi'
    elif LQI_dest <40 and LQI_source < 40:
	print "H metrisi prepei na ksanaginei. Ypirksan polles paremvoles."
	pass
    elif LQI_dest < 40:
	print "Kane ena vima ston Destination"
    elif LQI_source < 40:
	print "kane ena vima ston source"
elif metric == 'RSSI':
    if RSSI_dest >= -85 and RSSI_source >= -85:
	print 'To robot einai se oikanopoiitiki thesi'
    elif RSSI_dest < -85 and RSSI_source < -85:
	print "H metrisi prepei na ksanaginei. Ypirksan polles paremvoles."
	pass
    elif RSSI_dest < -85:
	print 'Kane ena vima ston Destination'
    elif RSSI_source < -85:
	print 'Kane ena vima ston Source' 