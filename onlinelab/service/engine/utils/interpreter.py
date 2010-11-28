"""Language independent engines' interpreter functions. """

import sys
import traceback

from outputtrap import OutputTrap

class Interpreter(object):
    """Base class for Python-managed interpreters. """

    filename = '<online-lab>'

    def __init__(self, debug=False):
        self.debug = debug
        self.trap = OutputTrap()
        self.index = 0

    def traceback(self):
        """Return nicely formatted most recent traceback. """
        type, value, tb = sys.exc_info()
        return ''.join(traceback.format_exception(type, value, tb.tb_next))

