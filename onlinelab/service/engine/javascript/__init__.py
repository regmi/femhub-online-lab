"""Bootstrap code for a JavaScript engine. """

boot = """\
from onlinelab.service.engine.javascript.runtime import JavaScriptEngine
JavaScriptEngine().run(port=%(port)d)
"""

def builder(port):
    """Build command-line for running JavaScript engine. """
    return ["python", "-c", boot % {'port': port}]

