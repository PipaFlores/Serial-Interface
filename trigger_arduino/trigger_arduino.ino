bool trigger_state = false;
int trigger_pin = A5;

// This Arduino sketch is designed to control a trigger pin and the built-in LED based on serial input.
// The trigger pin is set to HIGH (5V) when the serial port receives a 1, and LOW (0V) when it receives a 0.
// The built-in LED is turned on when the trigger pin is HIGH, and off when it is LOW.
// The serial port must be initialized with a baud rate of 9600.

void setup() {
    Serial.begin(9600);        // Initialize Serial communication with 9600
    pinMode(A5, OUTPUT); // Set the pin as an output
    pinMode(LED_BUILTIN, OUTPUT); // Set the built-in LED pin as an output
}

void loop() {
    if (Serial.available() > 0) {
        String value = Serial.readStringUntil('\n');  // Read until newline
        int intValue = value.toInt();
        if (intValue == 1) {
            trigger_state = true;
        } else if (intValue == 0) {
            trigger_state = false;
        }
    }
    if (trigger_state) {
        digitalWrite(trigger_pin, HIGH);  // Set pin to 5V
        digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED
        // Serial.println("Trigger sent");
    } else {
        digitalWrite(trigger_pin, LOW);   // Set pin to 0V
        digitalWrite(LED_BUILTIN, LOW); // Turn off the built-in LED
    }
}
