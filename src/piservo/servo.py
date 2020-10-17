import pigpio

class Servo:
    def __init__(self, gpio, min_value=0, max_value=180, min_pulse=0.5, max_pulse=2.4, frequency=50):
        self.__gpio = gpio
        self.__min_pulse = min_pulse
        self.__max_pulse = max_pulse
        self.__frequency = frequency
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = min_value
        self.start()
    
    def write(self, value):
        self.__value = value
        write_value = (value - self.__min_value) / (self.__max_value - self.__min_value) * (self.__max_pulse - self.__min_pulse) + self.__min_pulse
        self.__servo.hardware_PWM(self.__gpio, self.__frequency, int(max(min(write_value, self.__max_pulse), self.__min_pulse) * self.__frequency * 1000))
    
    def read(self, value):
        return self.__value
    
    def stop(self):
        self.__servo.set_mode(self.__gpio, pigpio.INPUT)
        self.__servo.stop()
    
    def start(self):
        self.__servo = pigpio.pi()
        self.__servo.set_mode(self.__gpio, pigpio.OUTPUT)
