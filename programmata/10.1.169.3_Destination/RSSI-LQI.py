# -*- coding: utf-8 -*-
import socket
import time
import subprocess
import sys
import datetime
import os


#UDPSock_0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("10.1.169.3",63100)
listen_addr = ("10.1.169.2",63100)
#send_addr = ("10.1.169.2",64100)
#UDPSock_0.bind(addr)

#rep_num = UDPSock_0.recv(1024)

#UDPSock_0.close()

#an 'int' variable specifying seconds for .sleep()
tm = 2
#a 'boolean' type variable for random use
check = False
#a list of all the characters that represent a numeric value
tup1 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')



#showing time and date
pf_t = ('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
print '\n' + pf_t + '\n'


#asking user for input
input = raw_input('Please give me the number of repetitions ' + '\n')
#print type(input)
#breaking user's input in single characters and storing them in a list 
list_1 = list(input)
#print list_1

while check != True :
    
    #finding the length of the list
    in_len = len(list_1)
    #print in_len
    
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
    elif int(input) > 100:
      
	print "Not so many sir, I am tired...less please"
	time.sleep(2)
	check = False
	input = raw_input('Please give me the number of repetitions again ' + '\n')
	list_1 = list(input)
    
    #if the input is 0 ask for input again
    elif int(input) == 0:
	
	print "At least one sir..."
	time.sleep(2)
	check = False
	input = raw_input('Please give me the number of repetitions again ' + '\n')
	list_1 = list(input)
	
#the input has been checked and the programm is ready to continue
rep_num = input
print "Got it...let's proceed " + rep_num + " times" 


time.sleep(tm)



#writing in timeline.txt the number of repetitions the user has given
file = open("timeline.txt", "a")
file.write(rep_num)
file.close()
time.sleep(tm)

print '============================='

#writing in rssi_snr.txt current time and date
file = open("rssi_lqi_lah.txt","a")
file.write('----- ' + pf_t + ' ----- ' + '\n' + '-------------------------------------------' + '\n' + '\n')
file.close()
time.sleep(tm)

#running konsole commands through a subprocess and storing the output in a .txt
cmd = "sudo bash iwlist.sh"
log = open('rssi_lqi_lah.txt', 'a')
p = subprocess.Popen(cmd, shell=True, stderr=log, stdout=log)
time.sleep(tm)

file = open("rssi_lqi_lah.txt","r")
file.seek(-2, 2)
last_digit = file.read(1)
#print last_digit

check = False
#while last != '0' and last != '1' and last != '2' and last != '3' and last != '4' and last != '5' and last != '6' and last != '7' and last != '8' and last != '9':
time.sleep(tm)

while check != True :
    file.seek(-2, 2)
    last_digit = file.read(1)
    #print last_digit
    
    dot = '.'
    sys.stdout.write('Calculating RSSI and LQI')
    
    for i in range(0,5):
	
	sys.stdout.write( dot )
	sys.stdout.flush()
	time.sleep(1)
	
    sys.stdout.flush()
    print ' '
    
    time.sleep(tm)
    check = last_digit in tup1
    
file.close()
print 'Summing the results...'

p.terminate()
log.close()
time.sleep(tm)
print 'Deleting dump files...'

#deleting dump files
file_path_tup = ['/home/spiros/ptixiaki/rssi-lqi/dump.txt', '/home/spiros/ptixiaki/rssi-lqi/link_dump.txt', '/home/spiros/ptixiaki/rssi-lqi/signal_dump.txt', '/home/spiros/ptixiaki/rssi-lqi/default.txt', '/home/spiros/ptixiaki/rssi-lqi/timeline.txt', '_']

i = 0
for i in range(0,5):
  
  myfile = file_path_tup[i]
  
  if os.path.isfile(myfile):
	
	os.remove(myfile)
	time.sleep(tm)
	
  elif file_path_tup[5] == '_':
    
	print 'Not waiting'
	pass
      
  else:
	
	print ('Error: %s file not found' % myfile)
	
	
print 'job done'
time.sleep(tm)

#reading rssi and snr from rssi_snr.txt
file = open("rssi_lqi_lah.txt","r")

lines = file.readlines()

bef_last_line_1 = lines[-1]
rssi_li = bef_last_line_1.split()
bef_last_line_2 = lines[-2]
lqi_li = bef_last_line_2.split()

#keeping only the arithmetic values
rssi_sum = rssi_li[0]
lqi_sum = lqi_li[0]

#concatenating the two values in one string in order to be sent 
final = lqi_sum + '/' + rssi_sum + 'b'

print 'LQI and RSSI are %s'%(final)  

file.close() 
#final = str(final)
UDPSock_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDPSock_1.sendto(bytes(final), listen_addr)
UDPSock_1.sendto("Connection Close", listen_addr)

UDPSock_1.close()

