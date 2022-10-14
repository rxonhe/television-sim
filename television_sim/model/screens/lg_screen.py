from television_sim.model.screens.screen import Screen


class LGScreen(Screen):
    turn_on_logo: str

    def __init__(self):
        super().__init__("Life is Good!")
