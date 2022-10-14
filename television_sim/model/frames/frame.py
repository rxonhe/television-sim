from abc import ABC


class Frame(ABC):
    logo: str

    def __init__(self, logo):
        self.logo = logo
        print("======================{}======================".format(self.logo))

    def __repr__(self):
        return self.logo
