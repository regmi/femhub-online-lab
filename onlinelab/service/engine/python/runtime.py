"""Runtime environment for Python engines. """

import os
import sys

from interpreter import PythonInterpreter
from server import PythonXMLRPCServer

class PythonEngine(object):
    """The most basic Python engine. """

    transport = PythonXMLRPCServer

    def __init__(self, interpreter=None):
        if interpreter is None:
            self.interpreter = PythonInterpreter()
        else:
            self.interpreter = interpreter

    def notify_ready(self):
        """Notify a service that an engine is running. """
        sys.stdout.write('OK (pid=%s)\n' % os.getpid())

    def run(self, port, interactive=False):
        """Run a Python engine on the given port. """
        server = self.transport(port, self.interpreter)
        self.notify_ready()
        server.serve_forever(interactive)

