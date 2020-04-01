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


## RBSM by Mosquitto
The Really Small Message Broker is a server implementation of the MQTT and MQTT-SN protocols. Any client that implements this protocol properly can use this server for sending and receiving messages.

The main reason for using RSMB over the main Mosquitto codebase is that Mosquitto doesn't currently have support for the MQTT-SN protocol.


## MQTT-SN/MQTT transparent bridge
For each connected MQTT-SN client a transparent bridge will setup and maintain an MQTT connection to the MQTT server. The transparent bridge will perform a “syntax” translation between the two protocols.

In this case, the transparent bridge is represented by a python script connected to the RSMB on port 1885 and listening on the topic of the virtual environment stations and to the ThingsBoard broker using the paho_mqtt library. When a virtual environment publishes sensor data on its topic in the RSMB, the bridge captures the message and sends it to the ThingsBoard broker.


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
