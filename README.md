# **Bandung Weather News**
We made a simulation program for measuring the average temperature of 3 temperature sensors in Bandung. Each sensor sends the temperature to the server in a span of every 10 seconds. Subscribers calculate and display the average temperature each time they receive information. The number of divisors is adjusted to the amount of incoming information, for example: if the incoming data is still from 2 sensors, then the divisor is 2.

## **Solution Selection**
The method used is Indirect Communication, publish and subscribe. A message in the form of temperature to subscribers is carried out by the sensor every 10 seconds. Subscriber calculates and displays the average temperature every time it receives an information message from the sensor.

## **System Model**
The system model we use is Publish-Subscribe. Publish – Subscribe is a system where the publisher (publisher) publishes or creates an event to an event service (Broker) and the subscriber (subscriber) subscribes to the event. The main task of the system is to match customer interests with existing events and ensure delivery notifications to customers.

## **System and Network Architecture**
![image](https://user-images.githubusercontent.com/55073908/150103005-93a84596-ae3b-45b3-805f-ceb280185d72.png)
Publish - Subscribe uses a Broker as a bridge to communicate so that there is no direct communication between the client and server.

## **Application Process Flow**
![image](https://user-images.githubusercontent.com/55073908/150103207-4ab49e67-8d6b-4563-9e15-96f8434053ef.png)

# **Reference**
- https://www.youtube.com/watch?v=qwiaWD6JKaY 
- https://www.youtube.com/watch?v=UTLx2ThNh28 
