# piServoCtl

## Overview
This is a servo motor control library for Raspberry Pi. In addition to normal servo motors, continuous rotation servo motors can also be controlled.
It utilizes hardware PWM. Therefore, the servo motor can be moved smoothly. Since you are using pigpio, you need to install pigpio and start pigpiod. To start pigpiod, you need to press the ````sudo pigpiod```` command or run pigpiod automatically.  
In addition, you can easily make an RC car by using two rotation servo motors. Use the Drive class to set the GPIO pin and servo motor. You can easily implement the steering function by using the steering method.  

## Installation

````shell:command.sh
sudo pip3 install piServoCtl
````

## Usage

First, start pigpiod (if it is not started). Then import the module. The module name is "piservo". Please note that it is different from the name when it was installed.  

````shell:command.sh
sudo pigpiod
````

### Servo

The easiest way is to use ````Servo(gpio)```` (where ````gpio```` is the GPIO pin number). Use GPIO that supports hardware PWM.  
You can control the servo motor with the ````write```` method.

### Drive

The easiest way is to use ````Drive(left_gpio, right_gpio)```` (````left_gpio````, ````right_gpio```` enter the GPIO pin number). Use GPIO that supports hardware PWM. You can swap the ````left_gpio```` and ````right_gpio```` to flip the front and back of the car.  
You can control the car with the ````steering```` method.  

## Demo

### Servo

````{.lines-numbers}python:example.py
from piservo import Servo
import time

myservo = Servo(12)

myservo.write(180)
time.sleep(3)
myservo.write(0)
time.sleep(3)
myservo.stop()
````

### Drive

````{.lines-numbers}python:example.py
from piservo import Drive
import time

mycar = Drive(12, 13)

mycar.steering(50, 45)
time.sleep(1)
mycar.steering(-50, 0)
time.sleep(1)
mycar.stop()
````

## Method

### Servo

````python:example.py
Servo(gpio, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50)
````

gpio: The gpio pin number to which the servo motor is connected.  
min_value: Minimum angle of servo motor (speed if it is a rotation servo motor).  
max_value: Maximum angle of servo motor (speed if it is a rotation servo motor).  
min_pulse: Minimum control pulse width of servo motor (millisecond).  
max_pulse: Maximum control pulse width of servo motor (millisecond).  
frequency: PWM frequency of the servo motor.  

Create an instance.  

````python:example.py
Servo.write(value)
````

value: Servo motor drive angle (speed if it is a rotation servo motor).  

Drives the servo motor.  

````python:example.py
Servo.read()
````

Read the current value of the servo motor.

````python:example.py
Servo.start()
````

Starts control of the servo motor.  

````python:example.py
Servo.stop()
````

Stops control of the servo motor.  

### Drive

````python:example.py
Drive(left_gpio, right_gpio, min_value=-100, max_value=100, min_pulse=0.5, max_pulse=2.4, frequency=50)
````

left_gpio: GPIO pin number to which the left servo motor is connected.  
right_gpio: GPIO pin number to which the right servo motor is connected.  
min_value: Minimum speed of servo motor.  
max_value: Maximum speed of servo motor.  
min_pulse: Minimum control pulse width of servo motor (millisecond).  
max_pulse: Maximum control pulse width of servo motor (millisecond).  
frequency: PWM frequency of the servo motor.  

Create an instance.  

````python:example.py
Drive.steering(speed=50, direction=0)
````

speed: Speed of movement.  
direction: Direction of movement.  

It moves in the specified direction at the specified speed.  

````python:example.py
Drive.stop()
````

Stop moving.  

````python:example.py
Drive.start()
````

Start control.  

````python:example.py
Drive.set_speed(speed)
````

speed: Speed of movement.  

Moves in the previously specified direction and at the specified speed.  

````python:example.py
Drive.set_direction(direction)
````

direction: Direction of movement.  

Moves in the specified direction at the previously specified speed.  

````python:example.py
Drive.get_speed()
````

Get the current speed.  

````python:example.py
Drive.get_direction()
````

Gets the current direction.  

## License

MIT
