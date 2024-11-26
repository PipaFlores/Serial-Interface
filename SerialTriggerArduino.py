try:
    import serial
except ImportError:
    print("The 'pyserial' package is not installed. Please install it using 'pip install pyserial'")
    raise
import time


class ArduinoTrigger(serial.Serial):
    """
    A class to send signals to an Arduino via serial.
    """

    def __init__(self, Serial_Port, initial_delay=2):
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
        super().__init__(Serial_Port, baudrate=9600, timeout=.1)
        time.sleep(initial_delay)

    def send_signal(self, signal, sleep = 0):
        """
        Send a signal to the Arduino
        
        Args:
            signal (bool) - True or False. True will send a '1' to the Arduino, False will send a '0'.
            
            sleep (float) - the delay (seconds)to wait after sending the signal, set to 0 if no delay is desired, check
            that no values are being sent too quickly.

        The SerialTriggerArduino object needs to be initialized first, 
        i.e.
        ```python

        serialport = SerialTriggerArduino('COM8')
        serialport.send_signal(True)
        ```
        """
        if isinstance(signal, bool):
            if signal == True:
                signal = bytes([1])
            else:
                signal = bytes([0])
        else:
            raise ValueError("Signal must be a boolean")
        self.write(signal)
        time.sleep(sleep)


