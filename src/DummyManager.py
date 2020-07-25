import yaml

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

class DummyManager(Manager):
    @staticmethod
    def initialize():
        DummyManager.__instance = DummyManager()

        return

    @staticmethod
    def load():
        return DummyManager.__instance