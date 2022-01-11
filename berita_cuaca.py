# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

#list untuk menampung data sensor
data_sensor = []

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client,userdata,message):
    #menambahkan data sensor yang dikirim oleh server-server sensor ke dalam list 
    data_sensor.append(int(message.payload.decode("utf-8")))
    #menampilkan data nama dari topik beserta nilai datanya
    print(message.topic, " = ", str(message.payload.decode("utf-8")))

########################################
    
# buat definisi nama broker yang akan digunakan
broker_name = "localhost"

# buat client baru bernama berita_cuaca
print("membuat instance baru")
client = mqtt.Client("berita_cuaca")

# buat koneksi ke broker
print("menghubungkan broker")
client.connect(broker_name,port=3333)

# jalankan loop client
client.loop_start()

# print topik yang disubscribe (dalam konteks ini, "sensor-1", "sensor-2" dan "sensor-3" )
print("Subscribe ke sensor-1, sensor-2 dan sensor-3")

# loop sampai 60x
for i in range (60):
    # berikan waktu tunggu 10 detik
    time.sleep(10)
    # client melakukan subscribe ke sensor 1, sensor 2 dan sensor 3
    client.subscribe("sensor-1")
    client.subscribe("sensor-2")
    client.subscribe("sensor-3")
    # kaitkan callback on_message ke client
    client.on_message = on_message
    #menjumlahkan seluruh suhu yang telah dikirim dari 3 sensor
    # kemudian dibagi 3 untuk mendapatkan rata-rata suhu
    hasil = sum(data_sensor) / 3
    # menampilkan rata-rata suhu bandung saat ini
    print("Suhu Bandung untuk saat ini: " + str(hasil) + " Celcius")
    # menghapus nilai list
    data_sensor.clear()
    
#stop loop
client.loop_stop()