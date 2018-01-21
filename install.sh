#!/bin/sh

sudo cp /home/pi/doorbell-pi/doorbell.service /lib/systemd/system/doorbell.service
sudo chmod 644 /lib/systemd/system/doorbell.service
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
sudo systemctl start myscript.service
sudo systemctl status myscript.service