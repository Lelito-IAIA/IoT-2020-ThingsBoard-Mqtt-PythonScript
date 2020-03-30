import MQTTSNclient as mqttsn
import mqtt_client as mqtt
import time
    									
class RecivingCallback1:								
	def messageArrived(self, topicName, payload, qos, retained, msgid):		
	 print "Payload arrived for Station1"
	 ret= mclient.publish1(payload) 			
	 return True
    									
class RecivingCallback2:							
	def messageArrived(self, topicName, payload, qos, retained, msgid):		
	 print "Payload arrived for Station2"
	 ret= mclient.publish2(payload) 			
	 return True

mclient = mqtt.MQTT_client()

aclient1 = mqttsn.Client("linh1", port=1885)
aclient1.registerCallback(RecivingCallback1())
aclient2 = mqttsn.Client("linh2", port=1885)
aclient2.registerCallback(RecivingCallback2())
print("Connecting to MQTT-SN Broker:")
aclient1.connect()
aclient2.connect()
aclient1.subscribe("devices/vs1")
aclient2.subscribe("devices/vs2")
print("#CONNECTED TO MQTT-SN BROKER#\n")
print("# READY TO BRIDGE #\n")


try:
	while(1):
		time.sleep(2)
except KeyboardInterrupt:
	print("Closing the client")
	aclient.disconnect()
	mclient.disconnect()


