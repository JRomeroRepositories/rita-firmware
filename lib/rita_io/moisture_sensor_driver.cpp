// #include <Arduino.h>
// #include <map>


// // 
// class MoistureSensorDriver {
//     public:
//         int pin;
//         int value;

//         void setup() {
//             pinMode(pin, INPUT);
//         }

//         // read_moisture_raw() returns the raw value from the sensor (0-1023)
//         int read_moisture_raw() {
//             value = analogRead(pin);
//             return value;
//         }

//         // read_moisture() returns the moisture level as a percentage (0-100)
//         int read_moisture() {
//             value = analogRead(pin);
//             return map(value, 0, 1023, 0, 100);
//         }

//         // TODO: Implement a moving average function since readings can be noisy

// };

//     // TODO: Implement a moving average function since readings can be noisy
