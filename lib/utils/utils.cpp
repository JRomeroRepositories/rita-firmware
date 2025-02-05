#ifndef UTILS_H
#define UTILS_H

#include <Arduino.h>
#include "utils.hpp"

// TODO: Make a proper log function.
void log(const char *message) {
    Serial.println(message);
}


#endif
