from machine import Machine


class Motor(Machine):

    def __init__(self, machine_id):

        super().__init__(
            machine_id=machine_id,
            name="Motor",
            rated_power=3.5
        )

        self.rpm = 1450
        self.torque = 20
        self.vibration = 0.2

    def update(self):

        super().update()

        if self.status:

            import random

            self.rpm = random.randint(1400, 1500)

            self.torque = round(
                random.uniform(18, 22),
                2
            )

            self.vibration = round(
                random.uniform(0.1, 0.5),
                2
            )

    def display(self):

        super().display()

        print(f"RPM        : {self.rpm}")
        print(f"Torque     : {self.torque} Nm")
        print(f"Vibration  : {self.vibration} mm/s")