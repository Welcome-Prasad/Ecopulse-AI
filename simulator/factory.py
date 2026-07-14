from simulator.machines.motor import Motor
from simulator.machines.compressor import Compressor
from simulator.machines.hvac import HVAC
from simulator.machines.lighting import Lighting

from simulator.logger import DataLogger
from simulator.utils import current_time

from database.db import Database


class Factory:

    def __init__(self):

        self.machines = []

        self.logger = DataLogger()

        self.database = Database()

        self.add_machine(Motor("M001"))
        self.add_machine(Compressor("C001"))
        self.add_machine(HVAC("H001"))
        self.add_machine(Lighting("L001"))

    def add_machine(self, machine):

        self.machines.append(machine)

    def start_factory(self):

        for machine in self.machines:
            machine.turn_on()

    def update(self):

        for machine in self.machines:

            machine.update()

            timestamp = current_time()

            self.logger.log(
                machine,
                timestamp
            )

            self.database.insert_machine(
                timestamp,
                machine
            )

    def display(self):

        for machine in self.machines:

            machine.display()

            print()