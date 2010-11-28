"""Language independent engines' interpreter functions. """

from outputtrap import OutputTrap

class Interpreter(object):
    """Base class for Python-managed interpreters. """

    filename = '<online-lab>'

    def __init__(self, debug=False):
        self.debug = debug
        self.trap = OutputTrap()
        self.index = 0

