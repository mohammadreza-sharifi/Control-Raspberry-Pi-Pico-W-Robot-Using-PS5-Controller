import socket
import network
from time import sleep
from machine import Pin as pin
 
ssid = 'Mrsh77'
password = '1m77n2299215r77#'
 
in1 = pin(16,pin.OUT)
in2 = pin(17,pin.OUT)
in3 = pin(18,pin.OUT)
in4 = pin(19,pin.OUT)

ENA = pin(20,pin.OUT)
ENB = pin(21,pin.OUT)

ENA.value(1)
ENB.value(1)


#This Function moves the Robot forward
def forward():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)

#This Function moves the Robot backward
def backward():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)

    
#This Function moves the Robot right
def right():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)

#This Function moves the Robot left
def left():
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)

#This Function stops the Robot
def stopfcn():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

 
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
 
def open_socket(ip):
    address = (ip,80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    #print(connection)
    return connection
 
 
try:
    ip = connect()
    connection = open_socket(ip)
    while True:
        # Accept a connection from a client
        client, addr = connection.accept()
        print(f'Connected to {addr}')
        while True:
            # Receive data from the client
            data = client.recv(1024)
            if data:
                # Print the data to the console
                #print(data)
                 
                if data == b'forward':
                    forward()
                     
                elif data == b'back':
                    backward()
                          
                elif data == b'right':
                    right()
                    
                elif data == b'left':
                    left()
                    
                elif data == b'stop':
                    stopfcn()
                    
except KeyboardInterrupt:
    # Close the server socket
    connection.close()