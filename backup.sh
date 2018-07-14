#!/bin/bash

DATE=`date +%Y-%m-%d`

#MOTION_DIR="/home/pi/motion" #/home/pi/hydro/data"
DATA_DIR="/home/pi/hydro/data"
DROPBOX_UPLOADER="/home/pi/Dropbox-Uploader/dropbox_uploader.sh"
UPLOADER="/home/pi/.dropbox_uploader"
TARGET_DIR="/Projects/Hydro_3/"

#TIME_FILE="$MOTION_DIR/$DATE-timelapse.mpg"
DATA_FILE="$DATA_DIR/data_$DATE.csv"


$DROPBOX_UPLOADER -f "$UPLOADER" upload "$DATA_FILE" "$TARGET_DIR/data/"
#$DROPBOX_UPLOADER -f "$UPLOADER" upload "$TIME_FILE" "$TARGET_DIR/motion/"
#$DROPBOX_UPLOADER -s -f "$UPLOADER" upload "$MOTION_DIR/$DATE"* "$TARGET_DIR/motion/"

