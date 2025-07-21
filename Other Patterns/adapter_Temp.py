# Target interface
class CelsiusTemperature:
    def get_temperature(self):
        pass

# Adaptee (the class with the incompatible interface)
class FahrenheitTemperature:
    def get_temperature_in_fahrenheit(self):
        return 100.0  

# Adapter
class FahrenheitToCelsiusAdapter(CelsiusTemperature):
    def __init__(self, fahrenheit_temperature):
        self.fahrenheit_temperature = fahrenheit_temperature

    def get_temperature(self):
        # Convert Fahrenheit to Celsius
        return (self.fahrenheit_temperature.get_temperature_in_fahrenheit() - 32) * 5.0/9.0

# Client code
def print_temperature(temperature_object):
    print(f'Temperature: {temperature_object.get_temperature()}°C')

# Using the Adapter pattern
fahrenheit_temperature = FahrenheitTemperature()
adapter = FahrenheitToCelsiusAdapter(fahrenheit_temperature)
print_temperature(adapter)
print(adapter.get_temperature())
