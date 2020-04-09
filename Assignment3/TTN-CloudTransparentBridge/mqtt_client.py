import paho.mqtt.client as paho  		    									#Import of paho-mqtt library	

#Defining the MQTT_client class that will be able to connect to the ThingsBoard broker
class MQTT_client:
	def __init__(self,ACCESS_TOKEN1='m4tTwRDNRpt3tWy7yokT', ACCESS_TOKEN2="j2QZULfsKWRMIlVsO9Ni",broker="demo.thingsboard.io",port=1883):
		print("Connecting to MQTT Thingsboard Broker:")
		self.client1= paho.Client(client_id="control1")							#Create client1 object
		self.client2= paho.Client(client_id="control1")							#Create client2 object
		print("#")                    			
		self.client1.on_publish = self.on_publish 								#Assign function to callback of client1
		self.client2.on_publish = self.on_publish 								#Assign function to callback of client2
		print("#")                     					
		self.client1.username_pw_set(ACCESS_TOKEN1)		#Assaign to client1 the access token of  Virtual Environment Station 1 in ThingsBoard
		self.client2.username_pw_set(ACCESS_TOKEN2) 	#Assaign to client1 the access token of  Virtual Environment Station 2 in ThingsBoard
		print("#")              						
		self.client1.connect(broker,port,keepalive=60)  			#Establish connection between client1 and ThingsBoard
		self.client2.connect(broker,port,keepalive=60) 				#using the func connect from the class client
		print("#")          					
		print("#CONNECTED MQTT THINGSBOARD BROKER#")

	def on_publish(client,userdata,result):													#Callback Function
		print("data published to MQTT Thingsboard Broker \n")
		pass
    	
	def publish1(self,payload): 															#Send the payload 1 to client1 topic
		ret= self.client1.publish("v1/devices/me/telemetry",payload) 
		print(payload)		
		print("Please check LATEST TELEMETRY field of Station1\n")
	
	def publish2(self,payload): 															#Send the payload 2 to client2 topic
		ret= self.client2.publish("v1/devices/me/telemetry",payload) 
		print(payload)		
		print("Please check LATEST TELEMETRY field of Station2\n")
		
   	def disconnect(self):																	#Disconnect from the ThingsBoard Broker
   		self.client.disconnect()
   		print("disconnected from MQTT broker")
