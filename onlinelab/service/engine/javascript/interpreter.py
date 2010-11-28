"""Customized interpreter for JavaScript engines. """

import sys
import time

import PyV8

from onlinelab.service.engine import Interpreter

class JavaScriptInterpreter(Interpreter):
    """Customized JavaScript interpreter. """

    _extensions = ['print']

    def __init__(self, debug=False):
        super(JavaScriptInterpreter, self).__init__(debug)

        extensions = []

        for ext in self._extensions:
            name = getattr(self, 'setup_' + ext)()
            extensions.append(name)

        self.context = PyV8.JSContext(extensions=extensions)

    @classmethod
    def setup_print(cls):
        """Setup JavaScript analog of ``print`` statement. """

        def jsext_print(*args):
            """Print values to stdout. """
            for arg in args:
                print arg,
            print

        src = 'native function print(arg);'
        ext = PyV8.JSExtension('print/python', src, lambda _: jsext_print)

        return ext.name

    def evaluate(self, source):
        """Evaluate a piece of JavaScript source code. """
        interrupted = False
        traceback = False
        result = None

        source = source.rstrip()

        if not self.debug:
            self.trap.set()

        start = time.clock()

        try:
            try:
                with self.context as ctx:
                    result = ctx.eval(source, self.filename)

                    if result is not None and source and source[-1] != ';':
                        sys.stdout.write(str(result) + '\n')
            except SystemExit:
                raise
            except KeyboardInterrupt:
                traceback = "Interrupted"
                interrupted = True
            except PyV8.JSError as exc:
                traceback = "%s: %s" % (exc.name, exc.message)

            end = time.clock()

            out = self.trap.out
            err = self.trap.err
        finally:
            self.trap.reset()

        self.index += 1

        result = {
            'source': source,
            'index': self.index,
            'traceback': traceback,
            'interrupted': interrupted,
            'time': end - start,
            'out': out,
            'err': err,
        }

        return result

    def complete(self, source):
        """Find all names that start with the given prefix. """
        return {
            'completions': [],
            'interrupted': False,
        }

