import time

from television_sim.model.commands.command import Command
from television_sim.model.controllers.controller import TimedOffController


class SmartController(TimedOffController):
    on_command: Command
    off_command: Command

    def __init__(self, on_command, off_command):
        super().__init__()
        self.on_command = on_command
        self.off_command = off_command

    def turn_on(self):
        self.on_command.execute()

    def turn_off(self):
        self.off_command.execute()

    def timed_off(self, delay=1):
        print("starting delay...")
        time.sleep(delay)
        self.turn_off()
