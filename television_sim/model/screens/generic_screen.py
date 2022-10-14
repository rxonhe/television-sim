from television_sim.model.screens.screen import Screen


class GenericScreen(Screen):
    color: str

    def __init__(self):
        super().__init__("LET'S WATCH!")
