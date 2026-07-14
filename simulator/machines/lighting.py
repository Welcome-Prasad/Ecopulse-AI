import random

from simulator.machine import Machine


class Lighting(Machine):

    def __init__(self, machine_id):

        super().__init__(
            machine_id=machine_id,
            name="Lighting",
            rated_power=2
        )

        self.brightness = 100
        self.occupancy = True
        self.power_mode = "Normal"

    def update(self):

        super().update()

        if self.status:

            self.brightness = random.randint(60, 100)

            self.occupancy = random.choice([True, False])

            if self.occupancy:
                self.power_mode = "Normal"
            else:
                self.power_mode = "Eco"

    def display(self):

        super().display()

        print(f"Brightness : {self.brightness}%")
        print(f"Occupancy  : {'Yes' if self.occupancy else 'No'}")
        print(f"Power Mode : {self.power_mode}")