#!/bin/sh

# WIP
# TODO: Add libraries used
# TODO: Test on blank system

sudo cp /home/pi/doorbell-pi/doorbell.service /lib/systemd/system/doorbell.service
sudo chmod 644 /lib/systemd/system/doorbell.service
sudo systemctl daemon-reload
sudo systemctl enable doorbell.service
sudo systemctl start doorbell.service
sudo systemctl status doorbell.service