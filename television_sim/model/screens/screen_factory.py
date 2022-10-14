from television_sim.model.screens.generic_screen import GenericScreen
from television_sim.model.screens.lg_screen import LGScreen
from television_sim.model.screens.samsung_screen import SamsungScreen


class ScreenFactory:
    _available_models = {
        'lg': LGScreen,
        'samsung': SamsungScreen,
        'generic': GenericScreen
    }

    def build(self, model):
        return self._available_models.get(model, GenericScreen)()
