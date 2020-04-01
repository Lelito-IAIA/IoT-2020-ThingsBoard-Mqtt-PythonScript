import MQTTSNclient as mqttsn												#Import of MQTTSNclient
import mqtt_client as mqtt													#Import of mqtt_client
import time																	#Import of time
    									
class RecivingCallback1:													#Callback that allows to publish the payload of the first
	def messageArrived(self, topicName, payload, qos, retained, msgid):		#virtual environment station to the Thingsboard Broker
	 print "Payload arrived for Station1"
	 ret= mclient.publish1(payload) 			
	 return True
    									
class RecivingCallback2:													#Callback that allows to publish the payload of the second
	def messageArrived(self, topicName, payload, qos, retained, msgid):		#virtual environment station to the Thingsboard Broker
	 print "Payload arrived for Station2"
	 ret= mclient.publish2(payload) 			
	 return True

mclient = mqtt.MQTT_client()												#Defining of a new mqtt_client object

aclient1 = mqttsn.Client("linh1", port=1885)								#Defining of the first MQTTSNclient listening on 1885 port  
aclient1.registerCallback(RecivingCallback1())								#and assigning to it the first callback function
aclient2 = mqttsn.Client("linh2", port=1885)								#Defining of the second MQTTSNclient listening on 1885 port
aclient2.registerCallback(RecivingCallback2())								#and assigning to it the second callback function
print("Connecting to MQTT-SN Broker:")
aclient1.connect()															#Connecting the first MQTTSNclient
aclient2.connect()															#Connecting the second MQTTSNclient
aclient1.subscribe("devices/vs1")											#Subscribing the first MQTTSNclient to the VS1's topic
aclient2.subscribe("devices/vs2")											#Subscribing the first MQTTSNclient to the VS2's topic
print("#CONNECTED TO MQTT-SN BROKER#\n")	
print("# READY TO BRIDGE #\n")


try:																		#Loop to keep the bridge listening until a keyinterrupt
	while(1):																# is inserted
		time.sleep(2)
except KeyboardInterrupt:
	print("Closing the client")
	aclient.disconnect()
	mclient.disconnect()


