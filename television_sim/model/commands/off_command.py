from television_sim.model.commands.command import Command


class OffCommand(Command):
    def execute(self):
        print("Turned Off...")
