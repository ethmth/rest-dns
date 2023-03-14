#!/bin/sh

# GET ABSOLUTE PATH
SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $SCRIPT_RELATIVE_DIR
ABSOLUTE_PATH=$(pwd)

source "${ABSOLUTE_PATH}/.env"
LOCAL_IP="192.168.86.55"

curl -o /dev/null \
	-X POST -H "Content-Type: application/json" \
 	-d "{\"id\": \"$(cat /etc/hostname)\", \"ip\": \"$(piactl get vpnip)\", \"port\": \"$(piactl get portforward)\", \"local\":\"${LOCAL_IP}\"}" \
	$API_URL/ip
