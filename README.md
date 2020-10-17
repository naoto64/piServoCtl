# piservo
====

## Overview
This is a servo motor control library for Raspberry Pi.
It utilizes hardware PWM. Therefore, the servo motor can be moved smoothly. Since you are using pigpio, you need to install pigpio and start pigpio. To start pigpio, you need to hit the ````sudo pigpiod```` command or make pigpio start automatically.

## Demo

````python:example.py
from Servo import piservo
import time

myservo = Servo(12)

myservo.write(180)
time.sleep(3)
myservo.write(0)
time.sleep(3)
myservo.stop()
````

## Usage

#### Method

````python:example.py
Servo(gpio, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50)
````
