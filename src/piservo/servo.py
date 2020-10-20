import pigpio

class Servo:
    def __init__(self, gpio, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50):
        if min_pulse < 0:
            raise ValueError("The value of the argument min_pulse is out of range.")
        if max_pulse < 0:
            raise ValueError("The value of the argument max_pulse is out of range.")
        if max_pulse * 1000 >= 1000000 / frequency:
            raise ValueError("The value of the argument frequency is too large.")
        self.__gpio = gpio
        self.__min_pulse = min_pulse
        self.__max_pulse = max_pulse
        self.__frequency = frequency
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = None
        self.start()
        try:
            self.__servo.hardware_PWM(self.__gpio, self.__frequency, 0)
        except Exception:
            raise ValueError("The value of the argument gpio is out of range.")
    
    def write(self, value):
        if self.__servo is None:
            raise Exception("The function start is not being executed.")
        if value < self.__min_value or value > self.__max_value:
            raise ValueError("The value of the argument value is out of range.")
        self.__value = value
        write_value = (value - self.__min_value) / (self.__max_value - self.__min_value) * (self.__max_pulse - self.__min_pulse) + self.__min_pulse
        self.__servo.hardware_PWM(self.__gpio, self.__frequency, int(write_value * self.__frequency * 1000))
    
    def read(self):
        return self.__value
    
    def stop(self):
        self.__value = None
        self.__servo.set_mode(self.__gpio, pigpio.INPUT)
        self.__servo.stop()
        self.__servo = None
    
    def start(self):
        self.__servo = pigpio.pi()
        self.__servo.set_mode(self.__gpio, pigpio.OUTPUT)

class Drive:
    def __init__(self, left_gpio, right_gpio, min_value=-100, max_value=100, min_pulse=0.5, max_pulse=2.4, frequency=50):
        self.__left = Servo(left_gpio, min_value=min_value, max_value=max_value, min_pulse=min_pulse, max_pulse=max_pulse, frequency=frequency)
        self.__right = Servo(right_gpio, min_value=min_value, max_value=max_value, min_pulse=min_pulse, max_pulse=max_pulse, frequency=frequency)
        self.__min_value = min_value
        self.__max_value = max_value
        self.__speed = None
        self.__direction = None

    def steering(self, speed, direction=0):
        if speed < self.__min_value or speed > self.__max_value:
            raise ValueError("The value of the argument speed is out of range.")
        if direction < -180 or direction > 180:
            raise ValueError("The value of the argument direction is out of range.")
        self.__speed = speed
        self.__direction = direction
        if direction >= 0:
            self.__left.write(speed)
            rightValue = (90 - direction) / 90 * speed
            self.__right.write(-rightValue)
        else:
            self.__right.write(-speed)
            leftValue = (90 + direction) / 90 * speed
            self.__left.write(leftValue)

    def set_speed(self, speed):
        if self.__direction is None:
            raise Exception("The function steering or start is not being executed.")
        self.steering(speed=speed, direction=self.__direction)

    def set_direction(self, direction):
        if self.__speed is None:
            raise Exception("The function steering or start is not being executed.")
        self.steering(speed=self.__speed, direction=direction)
    
    def get_speed(self):
        return self.__speed

    def get_direction(self):
        return self.__direction

    def stop(self):
        self.__speed = None
        self.__direction = None
        self.__right.stop()
        self.__left.stop()
        
    def start(self):
        self.__right.start()
        self.__left.start()
