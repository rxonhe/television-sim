from television_sim.model.commands.command import Command


class OnCommand(Command):
    def execute(self):
        print("Turned On...")
