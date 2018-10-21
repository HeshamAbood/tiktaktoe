class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        print("temperature in constructor")

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
    def pr(self):
        print("private is:",self._temperature)
        print("public is:",self.temperature)
        

o = Celsius(-300)
o.temperature=-100

o.pr()


