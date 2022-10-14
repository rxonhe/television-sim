from television_sim.model.frames.generic_frame import GenericFrame
from television_sim.model.frames.lg_frame import LGFrame
from television_sim.model.frames.samsung_frame import SamsungFrame


class FrameFactory:
    _available_models = {
        'lg': LGFrame,
        'samsung': SamsungFrame,
        'generic': GenericFrame
    }

    def build(self, model):
        return self._available_models.get(model, GenericFrame)()
