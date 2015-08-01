import StringIO
from zope.interface.verify import verifyObject
        bytes = "bytes"
        p.childDataReceived(1, bytes)
        self.assertEqual(received, [bytes])
        bytes = "bytes"
        p.childDataReceived(2, bytes)
        self.assertEqual(received, [bytes])
        self.data = ''
        self.err = ''
        self.transport.write("abcd")
            if self.data != "abcd":
            self.transport.write("1234")
            if self.err != "1234":
            self.transport.write("abcd")
    s = "1234567" * 1001
        if buffer(self.buffer, self.count, len(data)) != buffer(data):
        exe = sys.executable
            self, exe, [exe, "-c", self.program] + argv, env=env)
    run = classmethod(run)
    program = (
        return ''.join(chunks).split('\0')
    program = (
        "items = environ.iteritems()\n"
        environString = ''.join(chunks)
        environ = iter(environString.split('\0'))
                k = environ.next()
                v = environ.next()
class ProcessTestCase(unittest.TestCase):
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_twisted.py")
        env = {"PYTHONPATH": os.pathsep.join(sys.path)}
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=env,
        p.transport.write("hello, world")
        p.transport.write("abc")
        p.transport.write("123")
            self.assertEqual(p.outF.getvalue(), "hello, worldabc123",
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_echoer.py")
        procTrans = reactor.spawnProcess(p, exe,
                                    [exe, scriptPath], env=None)
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_tester.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None)
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_tester.py")
        args = [exe, "-u", scriptPath]
            reactor.spawnProcess(p, exe, args, env=None)
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_echoer.py")
        reactor.spawnProcess(p, exe, [exe, scriptPath], env=None)
            self.assertEqual(len(''.join(p.buffer)), len(p.s * p.n))
        args = [r'a\"b ', r'a\b ', r' a\\"b', r' a\\b', r'"foo bar" "', '\tab', '"\\', 'a"b', "a'b"]
        pyExe = sys.executable
        scriptPath = util.sibpath(__file__, "process_cmdline.py")
        reactor.spawnProcess(p, pyExe, [pyExe, "-u", scriptPath]+args, env=None,
                             path=None)
            self.assertEqual(p.errF.getvalue(), "")
        exe = sys.executable
            {"foo": 2},
            {"foo": "egg\0a"},
            {3: "bar"},
            {"bar\0foo": "bar"}]
            [exe, 2],
            "spam",
            [exe, "foo\0bar"]]
            badArgs.append([exe, badUnicode])
                reactor.spawnProcess, p, exe, [exe, "-c", ""], env=env)
                reactor.spawnProcess, p, exe, args, env=None)
    encodedValue = "UNICODE"
            self.assertEqual(argv, ['-c', self.encodedValue])
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_reader.py")
            p = reactor.spawnProcess(self.pp[num],
                                     exe, [exe, "-u", scriptPath], env=None,
                                     usePTY=usePTY)
        if self.verbose: print "closing stdin [%d]" % num
        if self.verbose: print self.pp[0].finished, self.pp[1].finished
        if self.verbose: print "starting processes"
class TestTwoProcessesNonPosix(TestTwoProcessesBase, unittest.TestCase):
class TestTwoProcessesPosix(TestTwoProcessesBase, unittest.TestCase):
        if self.verbose: print "kill [%d] with SIGTERM" % num
        if self.verbose: print self.pp[0].finished, self.pp[1].finished
        if self.verbose: print "starting processes"
        if self.verbose: print "starting processes"
        if self.verbose: print "starting processes"
    data = ""
        self.transport.writeToChild(0, "abcd")
                if self.data != "righto":
                self.data = ""
                self.transport.writeToChild(3, "efgh")
                if self.data != "closed":
class FDTest(unittest.TestCase):
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_fds.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None,
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_linger.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None,
                                 "here is some text\ngoodbye\n")
        self.outF = StringIO.StringIO()
        self.errF = StringIO.StringIO()
class PosixProcessBase:
        if os.path.exists('/bin/%s' % (commandName,)):
            cmd = '/bin/%s' % (commandName,)
        elif os.path.exists('/usr/bin/%s' % (commandName,)):
            cmd = '/usr/bin/%s' % (commandName,)
        return cmd
        reactor.spawnProcess(p, cmd, ['true'], env=None,
        exe = sys.executable

        reactor.spawnProcess(p, exe, [exe, '-c', 'import sys; sys.exit(1)'],
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_signal.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None,
            reactor.spawnProcess(p, cmd, ['false'], env=None,
                errData = "".join(p.errData + p.outData)
                self.assertIn("Upon execvpe", errData)
                self.assertIn("Ouch", errData)
        pythonExecutable = sys.executable
        scriptPath = util.sibpath(__file__, "process_echoer.py")
            ErrorInProcessEnded(), pythonExecutable,
            [pythonExecutable, scriptPath],
    @type fdio: C{StringIO.StringIO}
    readData = ""
        Fake C{os.fdopen}. Return a StringIO object whose content can be tested
        later via C{self.fdio}.
        self.fdio = StringIO.StringIO()
class MockProcessTestCase(unittest.TestCase):
        cmd = '/mock/ouch'
            reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        self.assertRaises(SystemError, reactor.spawnProcess, p, cmd, ['ouch'],
        cmd = '/mock/ouch'
            reactor.spawnProcess(p, cmd, ['ouch'], env=None,
            self.assertIn("RuntimeError: Bar", self.mockos.fdio.getvalue())
        cmd = '/mock/ouch'
            reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
            reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
            reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None,
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None, usePTY=False)
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None, usePTY=False)
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None, usePTY=False)
        cmd = '/mock/ouch'
        proc = reactor.spawnProcess(p, cmd, ['ouch'], env=None, usePTY=False)
class PosixProcessTestCase(unittest.TestCase, PosixProcessBase):
        cmd = sys.executable

        reactor.spawnProcess(p, cmd,
                             [cmd, "-c",
                              "import sys; sys.stderr.write('%s')" % (value,)],
            self.assertEqual(value, p.errF.getvalue())
        s = "there's no place like home!\n" * 3
        reactor.spawnProcess(p, cmd, [cmd, "-c"], env=None, path="/tmp",
class PosixProcessTestCasePTY(unittest.TestCase, PosixProcessBase):
    Just like PosixProcessTestCase, but use ptys instead of pipes.
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_tty.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None,
        p.transport.write("hello world!\n")
                "hello world!\r\nhello world!\r\n",
        pyExe = sys.executable
        pyArgs = [pyExe, "-u", "-c", "print 'hello'"]
            usePTY=1, childFDs={1:'r'})
                ValueError("Wrong exit code: %s" % (reason.exitCode,)))
class Win32ProcessTestCase(unittest.TestCase):
        pyExe = sys.executable
        scriptPath = util.sibpath(__file__, "process_stdinreader.py")
        reactor.spawnProcess(p, pyExe, [pyExe, "-u", scriptPath], env=None,
        p.transport.write("hello, world")
        pyExe = sys.executable
        pyArgs = [pyExe, "-u", "-c", "print 'hello'"]
            reactor.spawnProcess, p, pyExe, pyArgs, uid=1)
            reactor.spawnProcess, p, pyExe, pyArgs, gid=1)
            reactor.spawnProcess, p, pyExe, pyArgs, usePTY=1)
            reactor.spawnProcess, p, pyExe, pyArgs, childFDs={1:'r'})
        exe = sys.executable
        scriptPath = util.sibpath(__file__, "process_signal.py")
        reactor.spawnProcess(p, exe, [exe, "-u", scriptPath], env=None)

        pyExe = sys.executable
        pyArgs = [pyExe, "-u", "-c", "print 'hello'"]
class Win32UnicodeEnvironmentTest(unittest.TestCase):
class Dumbwin32procPidTest(unittest.TestCase):
        exe = sys.executable
        comspec = str(os.environ["COMSPEC"])
        cmd = [comspec, "/c", exe, scriptPath]
class UtilTestCase(unittest.TestCase):
        for name, mode in [(j(self.foobaz, "executable"), 0700),
                           (j(self.foo, "executable"), 0700),
                           (j(self.bazfoo, "executable"), 0700),
                           (j(self.bazfoo, "executable.bin"), 0700),
            f = file(name, "w")
    output = ''
    errput = ''
class ClosingPipes(unittest.TestCase):
            p, sys.executable, [
                sys.executable, '-u', '-c',
                'raw_input()\n'
                '    os.write(%d, "foo\\n")\n'
                'sys.exit(42)\n' % (fd,)
        p.transport.write('go\n')
        self.assertEqual(p.output, '')
            self.assertIn('OSError', errput)
                self.assertIn('Broken pipe', errput)
            self.assertEqual(errput, '')
    PosixProcessTestCase.skip = skipMessage
    PosixProcessTestCasePTY.skip = skipMessage
    TestTwoProcessesPosix.skip = skipMessage
    FDTest.skip = skipMessage
    Win32ProcessTestCase.skip = skipMessage
    TestTwoProcessesNonPosix.skip = skipMessage
    Dumbwin32procPidTest.skip = skipMessage
    Win32UnicodeEnvironmentTest.skip = skipMessage
    ProcessTestCase.skip = skipMessage
    ClosingPipes.skip = skipMessage