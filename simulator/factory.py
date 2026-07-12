from machines.motor import Motor
from machines.compressor import Compressor
from machines.hvac import HVAC
from machines.lighting import Lighting

from logger import DataLogger
from utils import current_time


class Factory:

    def __init__(self):

        self.machines = []

        self.logger = DataLogger()

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

            self.logger.log(
                machine,
                current_time()
            )

    def display(self):

        for machine in self.machines:

            machine.display()

            print()