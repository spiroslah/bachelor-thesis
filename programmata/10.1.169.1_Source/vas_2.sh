#! /bin/bash

#dinoume onoma sto txt
#echo Dwse onoma sto txt:
#read NAME

#dinoume epanalipseis
#echo Dwse arithmo epanalipsewn metrisis:
#read COUNT

value=`cat timeline.txt`
#echo "$value"

COUNT_1=$value
#pernoume ta link quality kai signal level
#COUNT=8
while [ $value -gt 0 ]; do
	iwlist wlan0 scan | egrep ESSID\|Quality | grep -B 1 wifibot >> default.txt
	#echo Value of count is: $COUNT
	let value=value-1
	sleep 6s
done

#emfanizoume ta periexomena tou txt pou ftiaksame
echo =========================================== >> default.txt
cat default.txt
sleep 2s

#kratame mono tous arithmous sto dump.txt
grep -Eo '[0-9]{1,4}' default.txt > dump.txt 

#petame ta link quality sto link_dump.txt
sed -n '1~3p' dump.txt > link_dump.txt

#COUNT=8
#prosthetoume ta apotelesmata tou link_dump.txt
sum_link=0
while read -r line
do
	((sum_link += line))
done < link_dump.txt
echo "scale=2 ; $sum_link/ $COUNT_1" | bc

#petame ta signal level sto signal_dump.txt
sed -n '3~3p' dump.txt > signal_dump.txt

#prosthetoume ta apotelesmata tou signal_dump.txt
sum_signal=0
while read -r line
do
	((sum_signal -= line))
done < signal_dump.txt
echo "scale=2 ; $sum_signal/ $COUNT_1" | bc
