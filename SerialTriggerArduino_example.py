import time
from SerialTriggerArduino import ArduinoTrigger

# Initialize the serial port
serialport = ArduinoTrigger("COM8")


# Use the send_signal method to send a signal to the Arduino
# Send 1, then 0, then 1, then 0
serialport.send_signal(True)
time.sleep(1)
serialport.send_signal(False)
time.sleep(1)

serialport.send_signal(True)
time.sleep(1)
serialport.send_signal(False)

# Close the serial port.
# The arduino will have the trigger pin set to HIGH or LOW depending on the last signal sent.
# Make sure your last signal is False (0) when the script is stopped.
serialport.close()
print("Signal stopped")