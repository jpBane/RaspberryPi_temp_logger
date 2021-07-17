#! /bin/sh

# Update all packages to their newest version:
sudo apt update && sudo apt upgrade

# Set the correct timezone for Germany:
sudo timedatectl set-timezone Europe/Berlin

# Install required python packages
sudo apt install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel

# Install the sensor package
sudo pip3 install Adafruit_DHT

# Get the script for the temperature/humidity logger
cd /home/pi
mkdir temp_humidity_logger
cd ./temp_humidity_logger
wget https://raw.githubusercontent.com/jpBane/RaspberryPi_temp_logger/main/temp_humidity_logger.py

# Make sure the script starts when the PiZero is booted.
(crontab -l; echo "@reboot /usr/bin/python3 /home/pi/temp_humidity_logger/temp_humidity_logger.py") | awk '!x[$0]++' | crontab -
