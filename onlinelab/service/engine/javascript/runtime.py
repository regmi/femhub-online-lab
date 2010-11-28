"""Runtime environment for JavaScript engines. """

from onlinelab.service.engine import Engine
from interpreter import JavaScriptInterpreter

class JavaScriptEngine(Engine):
    """The default JavaScript engine. """

    _interpreter = JavaScriptInterpreter

