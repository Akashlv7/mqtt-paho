import paho.mqtt.client as mqtt
from Connection import Connection


broker = "192.168.21.43"
topic = "test02"
name = "py3"
message = "-----------Hello Peeps This is Akash-----------"

#Creating a unique client name
client = mqtt.Client(name)
conn = Connection(client)

#Initialising the callback functions
client.on_connect = conn.on_connect
client.on_log = conn.on_log
client.on_disconnect = conn.on_disconnect

#Making Connection with client and publishing a message on a topic 
conn.client_connect(name, broker, topic, message)