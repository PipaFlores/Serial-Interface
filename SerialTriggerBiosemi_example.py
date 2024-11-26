import time
from SerialTriggerBiosemi import BiosemiTrigger

## To be used with the BIOSEMI trigger interface

# Initialize serial port, with an initial delay of 3 seconds
biosemi_trigger = BiosemiTrigger("COM7", initial_delay=3) # change to the correct port


# Test the connection by sending three 8 ms pulses to trigger 1 every one second
biosemi_trigger.test_trigger(signal_byte=0b00000001)
time.sleep(1)
biosemi_trigger.test_trigger(signal_byte=0b00000001)
time.sleep(1)
biosemi_trigger.test_trigger() # Since the signal is not specified, the default signal (1) is used


# Close the serial port
biosemi_trigger.close()
