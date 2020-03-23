# First Assignment 
This project is the my solution for the [First Assignment](http://ichatz.me/Site/InternetOfThings2020-Assignment1) of the IoT course in Sapienza University. It consist to create a cloud-based IoT system that collects information from a set of virtual environmental sensors using the MQTT protocol displaying the data collected from the sensors on a public web site.

# Python Script
To simulate the virtual environment stations, which represents the MQTT client, a python script has been created. to develop the script you need to install the [ paho-mqtt library](https://pypi.org/project/paho-mqtt/), it provides a client class which enable applications to connect to an [MQTT](http://mqtt.org/) broker to publish messages, and to subscribe to topics and receive published messages.
The virtual environment stations, at regular intervals, sends the following data to the broker:
> 1.  temperature (-50 ... 50 Celsius)
>2.  humidity (0 ... 100%)
>3.  wind direction (0 ... 360 degrees)
>4.  wind intensity (0 ... 100 m/s)
>5.  rain height (0 ... 50 mm / h)

## ThingsBoard

[ThingsBoard](https://thingsboard.io) is an open-source IoT platform for data collection, processing, visualization, and device management. MQTT is a lightweight publish-subscribe messaging protocol which probably makes it the most suitable for various IoT devices. ThingsBoard server nodes act as an MQTT Broker that supports QoS levels 0 (at most once) and 1 (at least once) and a set of predefined topics.

For the completion of the asssignament is sufficient the use of demo thingsboard that offers the use of a MQTT broker, the creation of public devices and public dashboards for the visualization of the data .

##  Web-based Dashboard
https://demo.thingsboard.io/dashboard/ea77c970-6c6f-11ea-8e0a-7d0ef2a682d3?publicId=8ff07230-6a27-11ea-ad02-b3576b7d39f1
## Hands-on Tutorial

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Video Demonstration

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

