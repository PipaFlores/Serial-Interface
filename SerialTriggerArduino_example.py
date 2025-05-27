import time
from SerialTriggerArduino import ArduinoTrigger

# Initialize the serial port
serialport = ArduinoTrigger("COM8", initial_delay=3)


# Use the send_signal method to send a signal to the Arduino
# Send 1, then 0, then 1, then 0
print("sent")
serialport.send_signal(True,sleep=1)
time.sleep(1)
serialport.send_signal(False)
time.sleep(1)

print("sent")
serialport.send_signal(True,sleep=1)
time.sleep(1)
serialport.send_signal(False)

# Close the serial port.
# The arduino will have the trigger pin set to HIGH or LOW depending on the last signal sent.
# Make sure your last signal is False (0) when the script is stopped.
serialport.close()
print("Signal stopped")