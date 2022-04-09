# RaspberryPi_temp_logger
A temparature and humidity logger using a Raspberry Pi and a DHT22 sensor.

## Simple setup with logging to a local CSV file

I wanted to be able to quickly set up a temperature and humidity logger using a fresh Raspberry Pi Zero and a DHT22 sensor. For this reason, the repository holds two files. The first file is the installation script and the second one is a python script that writes the temperature and humidity measured by the sensor to a local CSV file.

### Preparation
Starting point is a fresh installation of Raspberry Pi OS Lite on a Raspberry Pi Zero. If you do not know how to do this, there a plenty of descriptions out there, like [this one](https://www.raspberrypi.com/software/). When you choose the "Lite" version of the OS like I did, you need to do some preparations like [enabling SSH](https://howchoo.com/g/ote0ywmzywj/how-to-enable-ssh-on-raspbian-without-a-screen) and [seting up a Wifi without a monitor](https://howchoo.com/g/ndy1zte2yjn/how-to-set-up-wifi-on-your-raspberry-pi-without-ethernet) before putting the micro SD card in your Raspberry Pi Zero so that you can SSH into it. In case you choose the version "with desktop", you can connect a screen and a keyboard to your Raspberry Pi Zero and directly begin. 

If you are not shure how to connect the sensor to your Raspberry Pi Zero, you might find some help [here](https://medium.com/initial-state/build-an-inexpensive-network-of-web-connected-temperature-sensors-using-pi-zeros-730a40f1fb60).

### Installation
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

## Setup with database logging and a dashboard

After realising several temperature/humidity sensors I wanted to be able to easily get an overview of all the measurements in a dashboard. In this context, it makes sense to log all measurement data to a central database rather than storing it on each Raspberry Pi locally. Therefore, I had to set up a database and adjust the already existing python script to log the data to that data base instead of logging it to a local CSV file. 

### Setting up the database
Since we are logging time series data, I decided to go with InfluxDB. In a first step you need to install the database. I used my standard package manager. If you want the newest version, you can add the repository to your package manager. I went with the stable version in the standard repository `sudo apt install influxdb influxdb-client`. 

After the successfull installation, you should check if the service is already running using `service influxdb status` and in case it is not already running start it using `sudo service influxdb start`. Next we need to create the database since I did not include that into the Python script. Open the InfluxDB shell with `influx`. You can create the database using the following command `CREATE DATABASE temp_logger_db`. I recommend to use the same name. Otherwise you need to adust it in the Python script described in the next section. You can check, if the database was successfully created using `SHOW DATABASES`.

### Scripts for logging temperature/humidity to the database
Before you can use the `temp_humidity_logger_db.py` script in this repository, you first need to install the required Python libraries using the following command `python3 -m pip install influxdb`. I assume that you already installed the librarys for the DHT sensor at this point. After copying the script to your preferred folder it is time to make sure that the script automatically starts after each reboot. There are several ways but I prefer the one using a cron job. Just open the crontab `crontab -e` and add the following line to the file: `@reboot /path/to/python3 /path/to/temp_humidity_logger_db.py`.

### Setting up the dashboard
First you need to install Grafana. You can do this using the usual package manager. For me it makes sense to install it on the same computer where the database runs. Since I am installing it on my Raspberry Pi with its Debian based RaspianOS I use `sudo apt install grafana`. 

Sart the Grafana service with `sudo systemctl daemon-reload` and `sudo systemctl start grafana-server` and 
enable the service to automatically start after each system boot using `sudo systemctl enable grafana-server.service`.

