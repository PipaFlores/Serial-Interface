bool trigger_state = false;
int trigger_pin = A5;

// Sends a 5 ms pulse to the trigger pin.
// The pulse is sent to the trigger pin only if the serial port receives a 1 (binary 00000001 or hex 0x01).
// The built-in LED is turned on when the pulse is sent.
// If the serial port receives a 0, the pulse is not sent and the built-in LED is turned off.

void setup() {
    Serial.begin(9600);        // Initialize Serial communication with 9600
    pinMode(A5, OUTPUT); // Set the pin as an output
    pinMode(LED_BUILTIN, OUTPUT); // Set the built-in LED pin as an output
}

void loop() {
    if (Serial.available() > 0) {
        int intValue = Serial.parseInt();
        if (intValue == 1) {
            trigger_state = true;
        } else if (intValue == 0) {
            trigger_state = false;
        }
    }
    if (trigger_state) {
        digitalWrite(trigger_pin, HIGH);  // Set pin to 5V
        digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED
        delay(5);  // wait for 5 miliseconds
        digitalWrite(trigger_pin, LOW);
        trigger_state = false;
        // Serial.println("Trigger sent");
    } else {
        digitalWrite(trigger_pin, LOW);   // Set pin to 0V
        digitalWrite(LED_BUILTIN, LOW); // Turn off the built-in LED
    }
}
