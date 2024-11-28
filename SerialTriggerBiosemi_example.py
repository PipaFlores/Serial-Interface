import time
import serial
from SerialTriggerBiosemi import BiosemiTrigger

## To be used with the BIOSEMI trigger interface.
## The BiosemiTrigger class is a wrapper around the serial.Serial object, adding a delay if needed.
## It also provides a method to send a trigger pulse in a separate thread, without blocking the main thread.
## Below, there is an example of how to achieve the same functionality using the serial.Serial object directly.


## First example using the BiosemiTrigger class
# Initialize serial port, add an initial delay if needed.
biosemi_trigger = BiosemiTrigger("COM7", initial_delay=0) # change to the correct port

# Test the connection by sending three 8 ms pulses to trigger 1 every one second
biosemi_trigger.test_trigger(signal_byte=0b00000001)
time.sleep(1)
biosemi_trigger.test_trigger(signal_byte=0b00000001)
time.sleep(1)
biosemi_trigger.send_trigger() # Since the signal is not specified, the default signal (1) is used
biosemi_trigger.close()

print("waiting 2 seconds, sending the trigger with function")
time.sleep(2)

## Second example using the serial.Serial object directly
# Same functionality can be achieved with this simple function, using the serial.Serial object
def send_trigger(serialport: serial.Serial, signal_byte: int):  
    signal = bytes([signal_byte]) 
    serialport.write(signal)

serialport = serial.Serial("COM7", 115200, timeout=1)
# If the first trigger is not sent, allowing the serial port to initialize
send_trigger(serialport, 1)
time.sleep(1)
send_trigger(serialport, 1)
time.sleep(1)
send_trigger(serialport, 1)

# Close the serial port
serialport.close()
