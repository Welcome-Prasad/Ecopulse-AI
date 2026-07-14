import random

from simulator.machine import Machine


class HVAC(Machine):

    def __init__(self, machine_id):

        super().__init__(
            machine_id=machine_id,
            name="HVAC",
            rated_power=8
        )

        self.fan_speed = 1200
        self.cooling_load = 50
        self.room_temperature = 24.0

    def update(self):

        super().update()

        if self.status:

            self.fan_speed = random.randint(1000, 1600)

            self.cooling_load = round(
                random.uniform(30, 90),
                2
            )

            self.room_temperature = round(
                random.uniform(22, 27),
                2
            )

    def display(self):

        super().display()

        print(f"Fan Speed  : {self.fan_speed} RPM")
        print(f"Cooling Load : {self.cooling_load}%")
        print(f"Room Temp  : {self.room_temperature} °C")