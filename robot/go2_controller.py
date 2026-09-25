import time

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient


class Go2Controller:

    def __init__(self, network_interface):
        print("Initialisation du Go2...")

        ChannelFactoryInitialize(0, network_interface)

        self.client = SportClient()
        self.client.SetTimeout(10.0)
        self.client.Init()

        print("Go2 connecté.")

    def stand_up(self):
        self.client.StandUp()

    def stand_down(self):
        self.client.StandDown()

    def forward(self, duration=1):
        duration = min(duration, 3)

        self.client.Move(0.2, 0.0, 0.0)
        time.sleep(duration)
        self.client.StopMove()

    def backward(self, duration=1):
        duration = min(duration, 3)

        self.client.Move(-0.2, 0.0, 0.0)
        time.sleep(duration)
        self.client.StopMove()

    def turn_left(self, duration=1):
        duration = min(duration, 3)

        self.client.Move(0.0, 0.0, 0.3)
        time.sleep(duration)
        self.client.StopMove()

    def turn_right(self, duration=1):
        duration = min(duration, 3)

        self.client.Move(0.0, 0.0, -0.3)
        time.sleep(duration)
        self.client.StopMove()

    def hello(self):
        self.client.Hello()

    def sit(self):
        self.client.Sit()

    def stretch(self):
        self.client.Stretch()

    def dance(self):
        self.client.Dance1()

    def backflip(self):
        self.client.BackFlip()

    def stop(self):
        self.client.StopMove()

    def stop(self):
        self.client.StopMove()