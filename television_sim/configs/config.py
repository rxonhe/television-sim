from television_sim.model.commands.off_command import OffCommand
from television_sim.model.commands.on_command import OnCommand


class Config:
    commands = {
        "on": OnCommand(),
        "off": OffCommand()
    }
