#! /bin/bash

/etc/init.d/network-manager stop
sleep 20s
ifconfig wlan0 down
sleep 1s
iwconfig wlan0 mode ad-hoc essid wifibot channel 1 txpower 15
sleep 1s
ifconfig wlan0 10.1.169.1
route add 10.1.169.2 gw 10.1.169.2 dev wlan0
route add 10.1.169.3 gw 10.1.169.2 dev wlan0
echo 1 > /proc/sys/net/ipv4/ip_forward


