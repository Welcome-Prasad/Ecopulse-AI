import random

from simulator.config import (
    DEFAULT_VOLTAGE,
    ROOM_TEMPERATURE,
    MAX_HEALTH
)


class Machine:

    def __init__(self, machine_id, name, rated_power):

        self.machine_id = machine_id
        self.name = name

        self.status = False

        self.voltage = DEFAULT_VOLTAGE
        self.current = 0.0

        self.rated_power = rated_power
        self.power = 0.0

        self.temperature = ROOM_TEMPERATURE

        self.efficiency = 100.0
        self.health = MAX_HEALTH

        self.runtime = 0

    def turn_on(self):

        self.status = True

    def turn_off(self):

        self.status = False
        self.current = 0
        self.power = 0

    def update(self):

        if not self.status:
            return

        self.runtime += 1

        self.power = round(
            random.uniform(
                self.rated_power * 0.80,
                self.rated_power * 1.20
            ),
            2
        )

        self.current = round(
            self.power * 1000 / self.voltage,
            2
        )

        self.temperature += random.uniform(0.1, 0.8)

        self.efficiency = max(
            80,
            self.efficiency - random.uniform(0.01, 0.05)
        )

        self.health = max(
            70,
            self.health - random.uniform(0.005, 0.02)
        )

    def display(self):

        print("-" * 40)
        print(f"Machine ID : {self.machine_id}")
        print(f"Name       : {self.name}")
        print(f"Status     : {'ON' if self.status else 'OFF'}")
        print(f"Voltage    : {self.voltage} V")
        print(f"Current    : {self.current} A")
        print(f"Power      : {self.power} kW")
        print(f"Temp       : {self.temperature:.2f} °C")
        print(f"Efficiency : {self.efficiency:.2f}%")
        print(f"Health     : {self.health:.2f}%")
        print(f"Runtime    : {self.runtime} sec")