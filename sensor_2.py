# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import random untuk mendapatkan angka acak
from random import SystemRandom

# buat callback on_publish untuk publish data
########################################
def on_publish(client,userdata,result):
    print("Data sensor 2  dikirim\n")
    
########################################

# definisikan nama broker yang akan digunakan
broker_name = "localhost"

# buat client baru bernama Suhu_2
print("membuat instance baru")
client = mqtt.Client("Suhu_2")

# kaitkan callback on_publish ke client
client.on_publish = on_publish

# koneksi ke broker
print("menghubungkan broker")
client.connect(broker_name,port=3333)

# mulai loop client
client.loop_start()

# lakukan 20x publish topik "sensor-2"
for i in range (20):
    # sleep 1 detik
    time.sleep(10)
    # publish suhu sensor 2 dengan topik "sensor-2" (nilai suhu di acak dengan angka 0 - 30)
    srand = SystemRandom()
    randDegree = srand.choice(range(40))    
    client.publish("sensor-2",randDegree)
    print("Sensor ke-2: " + str(randDegree) + " Celcius")

#stop loop
client.loop_stop()