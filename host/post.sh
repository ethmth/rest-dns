#!/bin/sh

LOCAL_IP="192.168.86.57"

curl -o /dev/null \
	-X POST -H "Content-Type: application/json" \
 	-d "{\"id\": \"$(cat /etc/hostname)\", \"ip\": \"$(piactl get vpnip)\", \"port\": \"$(piactl get portforward)\", \"local\":\"${LOCAL_IP}\"}" \
	http://localhost:5000/ip
