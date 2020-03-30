#Library import
import paho.mqtt.client as paho  		                 #Import of paho-mqtt library
import time                                                      #Import of time library
import random as rnd                                             #Import of random library
 
#Get_value function definitions
def on_publish(client,userdata,result):                          #Callback Function
    print("data published to thingsboard \n")
    pass
def get_temperature():                                           #Generate a random temperature
    return '%.2f'%rnd.uniform(-50,50) + " Celsius"

def get_humidity():                                              #Generate a random humidity
    return '%.2f'%rnd.uniform(0,100) + "%"

def get_wind_direction():                                        #Generate a random wind direction
    return str(rnd.randrange(0,360)) + " degrees"

def get_wind_intensity():                                        #Generate a random wind intesity
    return str(rnd.randrange(0,100)) + " m/s"
                
def get_rain_height():                                           #Generate a random rain height
    return str(rnd.randrange(0,50)) + " mm/h"   

def get_payload():                                               #Generate the payload to send
    payload = '{"Temperature":"'            
    payload += get_temperature()
    payload += '", "Humidity":"'
    payload += get_humidity()
    payload += '", "Wind direction":"'
    payload += get_wind_direction()
    payload += '", "Wind intensity":"'
    payload += get_wind_intensity()
    payload += '", "Rain height":"'
    payload += get_rain_height()
    payload += '"}'
    return payload

#MQTT client definition
ACCESS_TOKEN1='m4tTwRDNRpt3tWy7yokT'                             #AccessToken of Virtual Environment Station 1 in ThingsBoard
ACCESS_TOKEN2='j2QZULfsKWRMIlVsO9Ni'                             #AccessToken of Virtual Environment Station 2 in ThingsBoard
    
broker="demo.thingsboard.io"   			                 #Host Name
port=1883 					                 #Data Listening port

client1= paho.Client("control1")                                 #Create client1 object
client1.on_publish = on_publish                                  #Assign function to callback of client1
client1.username_pw_set(ACCESS_TOKEN1)                           #Assaign to client1 the access token of  Virtual Environment Station 1 in ThingsBoard
client1.connect(broker,port,keepalive=60)                        #Establish connection using the func connect from the class client

client2= paho.Client("control1")                                 #Create client2 object
client2.on_publish = on_publish                                  #Assign function to callback of client2
client2.username_pw_set(ACCESS_TOKEN2)                           #Assaign to client2 the access token of  Virtual Environment Station 2 in ThingsBoard
client2.connect(broker,port,keepalive=60)                        #Establish connection using the func connect from the class client

#Sending data
while True:
    payload1= get_payload()                                              #Get a new payload1
    payload2= get_payload()                                              #Get a new peyload2
    ret= client1.publish("v1/devices/me/telemetry",payload1)             #Send the payload 1 to client1 topic
    ret= client2.publish("v1/devices/me/telemetry",payload2)             #Send the payload 2 to client2 topic
    print("Please check LATEST TELEMETRY field of your devices")         
    print(payload1);
    print(payload2);
    time.sleep(5)                                                        #Wait 5 second to resend another payload to the devices
   
