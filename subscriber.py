#import paho mqtt
import paho.mqtt.client as mqtt

#time for sleep
import time

#array var data
data = []

#buat callback on_message jika ada pesan
# fungsi akan dipanggil secara asyncronus 
def on_message(client, userdata, message):
	
	#menambahkan data yg dipublish oleh cliet ke dalam array 
	data.append(int(message.payload))
	#menampilkan data namatopik = random number
	print(message.topic, " = ", message.payload)

# nama broker yang digunakan
broker = "broker.emqx.io"

#buat client baru yaitu subscriber
client = mqtt.Client("subscriber")

#koneksi ke broker 
client.connect(broker, 1883, 8883)

#menjalankan loop client
client.loop_start()
#melakukan loop forever
while True:
	time.sleep(10) #delay 10 s

	#client melakukan subscribe ke sensor 1 dan 2
	client.subscribe("130119_sensor1")
	client.subscribe("130119_sensor2")
	client.subscribe("130119_sensor3")
	#melakukan callback on_message
	client.on_message = on_message
	#menjumlahkan isi data yang terpublish dari semua sensor 
	data2 = sum(data)
	#jumlah data dlm array, hasil jmlh value data dibagi jumlah sensor
	hasil = data2 / 3

	print("Suhu Bandung Saat Ini: ", hasil,"Celcius")

	data.clear()
client.loop_stop()