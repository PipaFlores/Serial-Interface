# Serial Trigger Interface

This repository contains guiding examples for sending trigger signals via serial communication to [Biosemi trigger interface](https://www.biosemi.com/faq/USB%20Trigger%20interface%20cable.htm) and [Arduino](https://www.arduino.cc/) devices. While an utility class is provided for each device, it's also possible to achieve the same functionality using the serial.Serial object directly, in a simpler way. (See last example in `SerialTriggerBiosemi_example.py`)

It's particularly useful for experimental setups requiring precise timing and trigger signals. Some examples on how to send bytes to the interfaces are provided in the `how_to_byte_python.ipynb` notebook.

The setup and scripts were tested with an oscilloscope. Biosemi trigger interface results in a 3.3V pulse of 8ms duration, and the Arduino trigger interface can be modified as desired (see `trigger_pulse_5ms_arduino/` for example code).

## What is in here?

- Utility classes for Biosemi and Arduino trigger interfaces, based on the [pyserial](https://pyserial.readthedocs.io/en/latest/shortintro.html) library.
- Example scripts for sending trigger signals.
- Thread-safe operations
- Comprehensive examples and documentation.

## Installation

1. Install the required Python package:

```bash
pip install serial
```
2. For Arduino setup:
   - Connect your Arduino to your computer via USB
   - Upload the `trigger_pulse_5ms_arduino.ino` sketch to your Arduino via the Arduino IDE.

## Usage

### Finding Your Serial Port

- On Linux/Mac: Run `ls /dev/tty*` in terminal
- On Windows: Check Device Manager or run `python -m serial.tools.list_ports` in terminal

### Biosemi Trigger Interface (Check `SerialTriggerBiosemi.py` for more details)

```python
from SerialTriggerBiosemi import BiosemiTrigger
# Initialize the trigger interface
biosemi = BiosemiTrigger("COM7", initial_delay=3) # Adjust port as needed
# Test the connection
biosemi.test_trigger(signal_byte=0b00000001) # Activates trigger 1
# Don't forget to close the connection
biosemi.close()
```

### Arduino Trigger Interface (Check `SerialTriggerArduino.py` for more details)

```python
from SerialTriggerArduino import ArduinoTrigger
# Initialize the trigger interface
arduino = ArduinoTrigger("COM8") # Adjust port as needed
# Send trigger signals
arduino.send_signal(True) # HIGH signal
arduino.send_signal(False) # LOW signal
# Close the connection
arduino.close()
```


## File Structure

- `SerialTriggerBiosemi.py` - Main class for Biosemi trigger interface
- `SerialTriggerArduino.py` - Main class for Arduino trigger interface
- `SerialTriggerBiosemi_example.py` - Example usage for Biosemi
- `SerialTriggerArduino_example.py` - Example usage for Arduino
- `trigger_pulse_5ms_arduino/` - Arduino sketch for trigger functionality
- `how_to_byte_python.ipynb` - Jupyter notebook explaining byte handling in Python

## Technical Details

### Biosemi Interface
- Supports 8-bit trigger signals
- 3.3V output
- 8ms trigger pulse duration
- Configurable trigger patterns
- Thread-safe operations available

### Arduino Interface
- 5V output (modifiable: You can experiment with PWM `analogWrite()` function)
- 5ms pulse duration (modifiable: Change delay between signals)
- Simple HIGH/LOW triggering
- Visual feedback via built-in LED


