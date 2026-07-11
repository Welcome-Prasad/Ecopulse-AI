from machines.motor import Motor


class Factory:

    def __init__(self):

        self.machines = []

    def add_machine(self, machine):

        self.machines.append(machine)

    def load_default_factory(self):

        self.add_machine(Motor("M001"))
        self.add_machine(Motor("M002"))
        self.add_machine(Motor("M003"))

    def start(self):

        for machine in self.machines:
            machine.turn_on()

    def update(self):

        for machine in self.machines:
            machine.update()

    def display(self):

        for machine in self.machines:
            machine.display()
            print()