# piservo

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
gpio: The gpio pin number to which the servo motor is connected.  
min_value: Minimum angle of servo motor (speed if it is a rotation servo motor).  
max_value: Maximum angle of servo motor (speed if it is a rotation servo motor).  
min_pulse: Minimum control pulse width of servo motor.  
max_pulse: Maximum control pulse width of servo motor.  
frequency: PWM frequency of the servo motor.  

Create an instance.

````python:example.py
write(value)
````
value: Servo motor drive angle (speed if it is a rotation servo motor).

````python:example.py
start()
````
Starts control of the servo motor.

````python:example.py
stop()
````
Stops the control of the servo motor.
