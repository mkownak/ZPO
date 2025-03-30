class FahrenheitSensor:
    def __init__(self, temperature):
        self.temp =temperature

    def get_temp(self)->float:
        return self.temp


class TemperatureAdapter:
    def __init__(self, sensor: FahrenheitSensor):
        self.sensor = sensor

    def convert_temp(self)->float:
        temp = self.sensor.get_temp()
        temp = (temp - 32) * 5/9
        return round(temp, 1)


F_sensor = FahrenheitSensor(40.4)
temp_adapter = TemperatureAdapter(F_sensor)
print(temp_adapter.convert_temp())
