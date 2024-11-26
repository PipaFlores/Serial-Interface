try:
    import serial
except ImportError:
    print("The 'pyserial' package is not installed. Please install it using 'pip install pyserial'")
    raise
import time
import threading

# This code is for the Biosemi trigger interface.
# The class inherits from the serial.Serial class, and so has all the same methods and attributes.
# All methods are documented below for clarity, but these are not extrictly required to be used. 
# Same functionality can be achieved by using the built in methods of the serial.Serial class.
# Besides the methods' documentation, check https://www.biosemi.com/faq/USB%20Trigger%20interface%20cable.htm for additional details.


class BiosemiTrigger(serial.Serial):
    """
    Initialize the serial port.
    """
    def __init__(self, Serial_Port, initial_delay = 3):
        """
        Initialize the serial port. Set ups a delay of 3 seconds to allow the device to boot.
        If no signals are sent shortly after initialization (e.g. within 3 seconds), then it can be
        set to 0. Otherwise, the signal will not be sent.

        Args:
            Serial_Port (string) - the port to initialize the serial port on.
            
            initial_delay (float) - the delay to wait after initializing the serial port.

        Returns:
            serialport (serial.Serial) - the initialized serial port object.

        To find your device's serial port, run `ls /dev/tty*` in the terminal, or `python -m serial.tools.list_ports` in python.
        """
        super().__init__(Serial_Port, baudrate=115200)
        time.sleep(initial_delay)

    def send_trigger(self, signal_byte = 0b00000001):
        """
        Send a 8 ms trigger pulse of 3.3V to a trigger output on the Biosemi trigger interface.

        Args:
            signal_byte (int) - the byte (in binary, or int) to send to the Biosemi trigger interface. Defaults to 0b00000001, 
            which is the binary representation of 1, activating trigger 1. 
            Valid values are `0b00000001` (trigger 1), `0b00000010` (trigger 2), `0b00000100` (trigger 3), `0b00001000` (trigger 4), etc.
            or in decimal, 1, 2, 4, 8, etc (powers of 2). Other values will activate multiple triggers. e.g. `0b00000011` will activate
            trigger 1 and 2.

        The BiosemiTrigger object needs to be initialized first,
        i.e.
        ```python

        serialport = BiosemiTrigger('COM8')
        serialport.send_trigger(True) # send a signal (5 V) to trigger 1
        ```
        """
        if not isinstance(signal_byte, int):
            raise ValueError("signal_byte must be an integer or binary representation of an integer")
        if signal_byte < 0 or signal_byte > 255:  # 8-bit limit
            raise ValueError("signal_byte must be between 0 and 255")
        
        signal = bytes([signal_byte]) # use the binary representation of 1, for better analogy with the circuit settings
        self.write(signal)


    def thread_trigger(self, signal_byte = 0b00000001):
        """
        Send a trigger pulse to the Biosemi trigger interface in a separate thread (does not block the main thread).

        Args:
            signal_byte (int) - the byte (in binary, or int) to send to the Biosemi trigger interface. Defaults to 0b00000001, 
            which is the binary representation of 1, activating trigger 1. 

        Returns:
            pulse_thread (threading.Thread) - the thread object for the trigger pulse.

        Usage:
        ```python
        pulse_thread = serialport.thread_trigger(signal_byte)
        # do other things while the pulse is being sent

        # If needed, wait for the pulse to finish before continuing
        pulse_thread.join()
        ```
        """
        pulse_thread = threading.Thread(target=self.send_trigger, args=(signal_byte))
        pulse_thread.start()
        return pulse_thread

    def test_trigger(self, signal_byte = 0b00000001):
        """Test if the connection is working by sending a quick pulse and printing a message."""
        try:
            self.send_trigger(signal_byte=signal_byte)
            print(f"Pulse sent to trigger {signal_byte} at serial port {self.name}")
            return True
        except Exception as e:
            print(f"Connection test failed: {str(e)}")
            return False
