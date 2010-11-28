"""Bootstrap code for a Python engine. """

boot = """\
from onlinelab.service.engine.python.runtime import PythonEngine
PythonEngine().run(port=%(port)d)
"""

def builder(port):
    """Build command-line for running Python engine. """
    return ["python", "-c", boot % {'port': port}]

