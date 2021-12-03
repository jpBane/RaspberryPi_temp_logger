# RaspberryPi_temp_logger
A temparature and humidity logger using a Raspberry Pi Zero and a DHT22 sensor.

I wanted to be able to quickly set up a temperature and humidity logger using a fresh Raspberry Pi Zero and a DHT22 sensor. For this reason, the repository holds two files. The first file is the installation script and the second one is a python script that writes the temperature and humidity measured by the sensor to a local CSV file.

## Preparation
Starting point is a fresh installation of Raspberry Pi OS Lite on a Raspberry Pi Zero. If you do not know how to do this, there a plenty of descriptions out there, like [this one](https://www.raspberrypi.com/software/). When you choose the "Lite" version of the OS like I did, you need to do some preparations like [enabling SSH](https://howchoo.com/g/ote0ywmzywj/how-to-enable-ssh-on-raspbian-without-a-screen) and [seting up a Wifi without a monitor](https://howchoo.com/g/ndy1zte2yjn/how-to-set-up-wifi-on-your-raspberry-pi-without-ethernet) before putting the micro SD card in your Raspberry Pi Zero so that you can SSH into it. In case you choose the version "with desktop", you can connect a screen and a keyboard to your Raspberry Pi Zero and directly begin. 

If you are not shure how to connect the sensor to your Raspberry Pi Zero, you might find some help [here](https://medium.com/initial-state/build-an-inexpensive-network-of-web-connected-temperature-sensors-using-pi-zeros-730a40f1fb60).

## Installation
The "temp_logger_installation.sh" does the following things automatically: 
* updating all packages via the advanced package tool (APT)
* setting the timezone to the central european time (CET) or UTC+1
* installing the required python packages
* installing the python package for the DHT22 sensor
* downloading a python script that runs the temperature/humidity logger
* creating a cron job that starts the python script as soon as you boot up your Raspberry Pi

You can get the installation script by navigating to the folder you prefer and typing the following code in your terminal:

`wget https://raw.githubusercontent.com/jpBane/RaspberryPi_temp_logger/main/temp_logger_instalation.sh`

After that you can run the script using the following code. Feel free to modify the timezone to your needs first. 

`bash temp_logger_installation.sh`

During the installation you need to confirm some things, so you should not expect the installation to run completely by itself. This way, you can also watch out for errors during the installation. 

The installation script also downloads the second file of this repository, which is a python script that runs the temperature/humidity logger. After the installation finishes without errors, you can reboot your Raspberry Pi Zero and the python script will automatically start logging the temperature and humidity every minute into a CSV file that is located at /home/pi/temp_humidity_logger. 
