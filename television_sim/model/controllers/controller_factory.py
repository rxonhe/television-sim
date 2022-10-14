from television_sim.model.controllers.generic_controller import GenericController
from television_sim.model.controllers.smart_controller import SmartController


class ControllerFactory:

    def __init__(self, commands):
        self.commands = commands
        self._available_models = {
            'generic': GenericController(on_command=commands.get("on"), off_command=commands.get("off")),
            'smart': SmartController(on_command=commands.get("on"), off_command=commands.get("off"))
        }

    def build(self, model):
        return self._available_models.get(model, GenericController)
