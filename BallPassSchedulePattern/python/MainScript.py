from World import World
import time

class MainScript:
    def __init__(self):
        self.world = World()

    def main(self):
        while True:
            self.world.firstPlayer.catch_ball(world=self.world)


a = MainScript()
a.main()

