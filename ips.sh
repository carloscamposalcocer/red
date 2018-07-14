#!/bin/bash

IP=$(curl icanhazip.com) 
FILE="ip_$(hostname).txt"
DIR="/home/pi/ip/"
DROPBOX_UPLOADER="/home/pi/Dropbox-Uploader/dropbox_uploader.sh"
UPLOADER="/home/pi/.dropbox_uploader"
TARGET_DIR="/Projects/HYDRO/IPs/"


echo $IP > $DIR$FILE

$DROPBOX_UPLOADER -f $UPLOADER upload $DIR$FILE $TARGET_DIR


