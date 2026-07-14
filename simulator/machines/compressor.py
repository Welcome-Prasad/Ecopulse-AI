import random

from simulator.machine import Machine


class Compressor(Machine):

    def __init__(self, machine_id):

        super().__init__(
            machine_id=machine_id,
            name="Compressor",
            rated_power=12
        )

        self.pressure = 8.0
        self.air_flow = 120.0
        self.tank_level = 75.0

    def update(self):

        super().update()

        if self.status:

            self.pressure = round(
                random.uniform(7.5, 8.5),
                2
            )

            self.air_flow = round(
                random.uniform(100, 140),
                2
            )

            self.tank_level = round(
                random.uniform(60, 100),
                2
            )

    def display(self):

        super().display()

        print(f"Pressure   : {self.pressure} bar")
        print(f"Air Flow   : {self.air_flow} L/min")
        print(f"Tank Level : {self.tank_level}%")