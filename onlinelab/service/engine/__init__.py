"""Common tools for Python-managed engines. """

import os
import sys

from python.server import PythonXMLRPCServer

class Engine(object):
    """Base class for Python-managed engines. """

    _transport = PythonXMLRPCServer
    _interpreter = None

    def __init__(self, interpreter=None):
        if interpreter is None:
            self.interpreter = self._interpreter()
        else:
            self.interpreter = interpreter

    def notify_ready(self):
        """Notify a service that an engine is running. """
        sys.stdout.write('OK (pid=%s)\n' % os.getpid())

    def run(self, port, interactive=False):
        """Run a Python engine on the given port. """
        server = self._transport(port, self.interpreter)
        self.notify_ready()
        server.serve_forever(interactive)

