import time

from simulator.factory import Factory
from simulator.utils import current_time


factory = Factory()

factory.start_factory()

while True:

    print("\n" + "=" * 70)
    print("             EcoPulse AI Virtual Factory")
    print("Time :", current_time())
    print("=" * 70)

    factory.update()

    factory.display()

    time.sleep(1)