#!/bin/sh

curl -o /dev/null \
	-X POST -H "Content-Type: application/json" \
 	-d "{\"id\": \"e-pc\", \"ip\": \"$(piactl get vpnip)\", \"port\": \"$(piactl get portforward)\"}" \
	http://localhost:5000/ip
