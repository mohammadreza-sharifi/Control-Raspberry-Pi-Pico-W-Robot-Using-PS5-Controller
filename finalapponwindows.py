from pydualsense import pydualsense
import socket
from time import sleep

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.233', 80))  # Connect to the server

def button_pressed(cmd):
    #print(f"{cmd} button pressed")
    client_socket.sendall(cmd.encode('utf-8'))

def button_released(cmd):
    #print(f"{cmd} button released")
    client_socket.sendall(cmd.encode('utf-8'))

def main():
    # Initialize the DualSense controller
    ds = pydualsense()
    ds.init()

    # Set up event handlers for buttons
    ds.cross_pressed += lambda state: button_pressed("back") if state else button_released("stop")
    ds.circle_pressed += lambda state: button_pressed("right") if state else button_released("stop")
    ds.square_pressed += lambda state: button_pressed("left") if state else button_released("stop")
    ds.triangle_pressed += lambda state: button_pressed("forward") if state else button_released("stop")

    try:
        print("Press any button to see the output...")
        while True:
            pass  # Keep the script running to listen for events
    except KeyboardInterrupt:
        pass
    finally:
        ds.close()  # Close the controller connection

if __name__ == "__main__":
    main()
