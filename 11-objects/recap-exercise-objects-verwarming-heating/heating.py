class Heating:
    def __init__(self, name, desired_temp, min_temp, max_temp):
        self.name = name
        self.min_temp = float(min_temp)
        self.max_temp = float(max_temp)

        self._desired_temp = None
        self.desired_temp = desired_temp

    @property
    def desired_temp(self):
        return self._desired_temp

    @desired_temp.setter
    def desired_temp(self, value):
        if value < self.min_temp:
            self._desired_temp = self.min_temp
        elif value > self.max_temp:
            self._desired_temp = self.max_temp
        else:
            self._desired_temp = float(value)

    def change_temperature(self, temp_change):
        self.desired_temp = self._desired_temp + temp_change

    def __str__(self):
        return (f"{self.name}: desired temperature: {self._desired_temp:.1f}; "
                f"allowed min: {self.min_temp:.1f}; allowed max: {self.max_temp:.1f}")
