"""Bootstrap code for a Python engine. """

boot = """\
from onlinelab.service.engine.python.runtime import PythonEngine
PythonEngine().run(port=%(port)d)
"""

