#import paho mqtt
import paho.mqtt.client as mqtt
from random import randrange, uniform
#import time untuk sleep()
import time 

#definisi nama broker
broker = "broker.emqx.io"

#client bernama sensor
client = mqtt.Client("130119_sensor1")

#koneksi ke broker 
client.connect(broker, 1883, 8883)

client.loop_start()
#perulangan publish
while True:
	#random number 
	randNumber = randrange(30)
	#publish data dengan topik "sensor1"
	client.publish("130119_sensor1", randNumber)
	#menampilkan data
	print(f"Suhu Sensor 1 = {str(randNumber)} celcius")
	#sleep delay 10 second
	time.sleep(10)
client.stop_loop()