import logging

from modules.dummy.DummyManager import DummyManager

def initialize():
    logging.info("Initializing dummy module...")

    DummyManager.initialize()

def connect():
    pass

def load_manager():
    return DummyManager.load()

def depends_on():
    return []