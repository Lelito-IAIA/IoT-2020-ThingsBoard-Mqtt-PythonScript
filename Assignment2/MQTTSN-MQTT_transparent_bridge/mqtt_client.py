import paho.mqtt.client as paho  		    				

class MQTT_client:
	def __init__(self,ACCESS_TOKEN1='m4tTwRDNRpt3tWy7yokT', ACCESS_TOKEN2="j2QZULfsKWRMIlVsO9Ni",broker="demo.thingsboard.io",port=1883):
		print("Connecting to MQTT Thingsboard Broker:")
		self.client1= paho.Client(client_id="control1")
		self.client2= paho.Client(client_id="control1")
		print("#")                    			
		self.client1.on_publish = self.on_publish 
		self.client2.on_publish = self.on_publish 
		print("#")                     					
		self.client1.username_pw_set(ACCESS_TOKEN1)
		self.client2.username_pw_set(ACCESS_TOKEN2) 
		print("#")              						
		self.client1.connect(broker,port,keepalive=60)  
		self.client2.connect(broker,port,keepalive=60) 
		print("#")          					
		print("#CONNECTED MQTT THINGSBOARD BROKER#")

	def on_publish(client,userdata,result):
		print("data published to MQTT Thingsboard Broker \n")
		pass
    	
	def publish1(self,payload): 
		ret= self.client1.publish("v1/devices/me/telemetry",payload) 
		print(payload)		
		print("Please check LATEST TELEMETRY field of Station1\n")
	
	def publish2(self,payload): 
		ret= self.client2.publish("v1/devices/me/telemetry",payload) 
		print(payload)		
		print("Please check LATEST TELEMETRY field of Station2\n")
		
   	def disconnect(self):
   		self.client.disconnect()
   		print("disconnected from MQTT broker")
