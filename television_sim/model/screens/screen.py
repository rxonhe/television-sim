from abc import ABC


class Screen(ABC):
    turn_on_logo: str

    def __init__(self, turn_on_logo):
        self.turn_on_logo = turn_on_logo
        print(self.turn_on_logo)

    def __repr__(self):
        return self.turn_on_logo
