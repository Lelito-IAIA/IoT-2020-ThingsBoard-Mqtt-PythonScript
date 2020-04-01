# Second Assignment
This project is the my solution for the [Second Assignment](http://ichatz.me/Site/InternetOfThings2020-Assignment2) of the IoT course in Sapienza University. It consist to replace the virtual environmental stations developed using Python in the First Assignment with new ones built using the RIOT-OS and MQTT-SN protocol.
## RIOT-OS
To simulate the virtual environment stations, which represents the MQTT-SN client, a RIOT-OS APPLICATION has been created. 


The virtual environment stations, at regular intervals, sends the following data to the broker:
> 1.  temperature (-50 ... 50 Celsius)
>2.  humidity (0 ... 100%)
>3.  wind direction (0 ... 360 degrees)
>4.  wind intensity (0 ... 100 m/s)
>5.  rain height (0 ... 50 mm / h)


## RBSM by mosquitto


## MQTT-SN/MQTT transparent bridge


## ThingsBoard

[ThingsBoard](https://thingsboard.io) is an open-source IoT platform for data collection, processing, visualization, and device management. MQTT is a lightweight publish-subscribe messaging protocol which probably makes it the most suitable for various IoT devices. ThingsBoard server nodes act as an MQTT Broker that supports QoS levels 0 (at most once) and 1 (at least once) and a set of predefined topics.

For the completion of the asssignament is sufficient the use of demo thingsboard that offers the use of a MQTT broker, the creation of public devices and public dashboards for the visualization of the data .

##  Web-based Dashboard

Link to Public Dashboard
>https://demo.thingsboard.io/dashboard/ea77c970-6c6f-11ea-8e0a-7d0ef2a682d3?publicId=8ff07230-6a27-11ea-ad02-b3576b7d39f1

## Hands-on Tutorial

Link to Blog Post in Linkedin: 
>link

## Video Demonstration

Link to video demonstration on Youtube:
>link




