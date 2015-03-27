import time, serial #Imports the serial for entering either 0 or 1 
import mosquitto
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1") #IP Address

client.subscribe("LED")

ser = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2) #9600 is the time in which it is being called - the time on the Arduino has to match this in order to work 

def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload) #This if statement converts 1 to ON and 0 to OFF
    if msg.payload == "ON": 
        ser.write("1")
    elif msg.payload == "OFF":
        ser.write("0")
  
client.on_message = messageReceived
    
while (client != None): client.loop() #Keeks the broker running 
    
