import csv
import os


class DataLogger:

    def __init__(self):

        self.filename = "data/datasets/factory_data.csv"

        os.makedirs("data/datasets", exist_ok=True)

        if not os.path.exists(self.filename):

            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Time",
                    "Machine_ID",
                    "Machine_Name",
                    "Voltage",
                    "Current",
                    "Power",
                    "Temperature",
                    "Efficiency",
                    "Health",
                    "Runtime"
                ])

    def log(self, machine, timestamp):

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                machine.machine_id,
                machine.name,
                machine.voltage,
                machine.current,
                machine.power,
                round(machine.temperature, 2),
                round(machine.efficiency, 2),
                round(machine.health, 2),
                machine.runtime
            ])