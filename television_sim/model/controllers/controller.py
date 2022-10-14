from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def turn_on(self):
        """Turn on method"""

    @abstractmethod
    def turn_off(self):
        """Turn on method"""


class TimedOffController(Controller):
    @abstractmethod
    def timed_off(self):
        """Timed off method"""


class TimedOnController(Controller):
    @abstractmethod
    def timed_on(self):
        """Timed off method"""
