import paho.mqtt.publish as publish
import time

class Connection:

    def __init__(self, client):
        self.client = client

    def on_log(self, client, userdata, level, buf):
        print("log :" + buf)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected OK")
        else:
            print("Bad Connection returned code = ", rc)

    def on_disconnect(self, client, userdata, flags, rc=0):
        print("Disconnected result code is " + str(rc))

    def client_connect(self, name, broker, topic, message):

        print("Connecting to broker", broker)
        self.client.connect(broker)

        self.client.loop_start()

        self.client.publish(topic, message)

        time.sleep(5)
        self.client.loop_stop()

        self.client.disconnect()