"""Runtime environment for Python engines. """

from onlinelab.service.engine import Engine
from interpreter import PythonInterpreter

class PythonEngine(Engine):
    """The default Python engine. """

    _interpreter = PythonInterpreter

