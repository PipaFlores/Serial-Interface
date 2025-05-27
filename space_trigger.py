import keyboard
from SerialTriggerArduino import ArduinoTrigger
import time

def main():
    # Initialize the serial port
    serialport = ArduinoTrigger("COM8", initial_delay=3)
    
    print("Press SPACE to send a signal. Press ESC to exit.")
    
    try:
        while True:
            # Wait for space key press   
            keyboard.wait('space')
            
            # Send the signal
            print("Sending signal...")
            serialport.send_signal(True, sleep=0.1)  # Short pulse              
            
            serialport.send_signal(False)
            
            # Small delay to prevent multiple triggers from one press
            time.sleep(0.2)
            
            # Check for ESC key to exit
            if keyboard.is_pressed('esc'):
                break
                
    except KeyboardInterrupt:
        pass
    finally:
        # Make sure to close the serial port
        serialport.close()
        print("\nProgram stopped")

if __name__ == "__main__":
    main() 