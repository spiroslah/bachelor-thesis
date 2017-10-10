# -*- coding: utf-8 -*-
import sys


line_number = 0

data = raw_input()

s = int(data)
prr = s/float(200)
prr_str = str(prr)
#print "to PRR einai: " + prr_str + '\n'

print "Irthe apo ton Dest: " + prr_str +'\n'

prr_pers = prr

file1 = open("prr.txt","r")
for line in file1:
  #print line
  line_number = line_number + 1
#print line_number

file1.seek(-5, 2)
s = file1.read(5)
prr_bef = float(s)
file1.close()

print "Η προηγούμενη τιμή είναι: " + s +'\n'

#grafoume thn kainouria timh tou prr
#sto arxeio prr.txt
file2 = open("prr.txt","a")
file2.write("\n"+str(prr_pers))
file2.close()

prr_pers_fl = float(prr_pers)
#An thelisoume na to kanoume % einai:
#prr_pers_fl = prr_pers_fl * 100

#elegxoume an to pososto tou prr gia tin kinisi
#tou robot
if (prr_pers_fl >= 0.95):
    print "Το σήμα είναι άνω του 95%"
elif (prr_pers_fl <= 0.95 and line_number == 1 ):
    print "pigene pros ton destination 1 vima"
    pass
elif (prr_pers_fl <= prr_bef ):
    print "allakse kateuthinsi kata 2 vimata"
elif (prr_pers_fl> prr_bef ):
    print "kane ena vima pros tin idia kateuthinsi"
