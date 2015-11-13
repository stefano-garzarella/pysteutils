from __future__ import absolute_import, division, print_function, unicode_literals #for python2 compatibility
import subprocess

class PyShell():
    """
    Execute shell command in python scripts.

    Example:

    from pysteutils.steshell import PyShell

    pyshell = PyShell()
    # get command output (stdout and stderr) as list of strings
    out, err = pyshell.sh('ls -l *.txt')
    out, err = pyshell.bash('ls -l *.txt')

    # print output (stdout and stderr) during execution
    pyshell.ish('grep -rin asd /')
    pyshell.ibash('grep -rin asd /')

    """

    logger = None

    def __init__(self, logger = None):
        """
        Constructor

        :type Logger
        :param logger: object to use for debug or logging
        """
        self.logger = logger

    def sh(self, cmd):
        """
        Execute a shell command and return the stdout and the
        stderr as a list of lines.

        :type cmd: String
        :param cmd:  a shell command string
        :return: the stdout and stderr as a list of lines.
        """
        sh_cmd = ['sh', '-c', cmd]
        return self.cmda(sh_cmd)

    def ish(self, cmd):
        """
        Interactive shell command execution.

        Execute a shell command and return the stdout and the
        stderr as a list of lines and print output stdout and stderr during execution).

        :type cmd: String
        :param cmd:  a shell command string
        """
        sh_cmd = ['sh', '-c', cmd]
        return self.icmda(sh_cmd)

    def bash(self, cmd):
        """
        Execute a bash command and return the stdout and the
        stderr as a list of lines.

        :type cmd: String
        :param cmd:  a bash command string
        :return: the stdout and stderr as a list of lines.
        """
        bash_cmd = ['bash', '-c', cmd]
        return self.cmda(bash_cmd)

    def ibash(self, cmd):
        """
        Interactive bash command execution.
        Execute a bash command and
        and print output (both stdout and stderr) during execution.

        :type cmd: String
        :param cmd:  a bash command string
        """
        bash_cmd = ['bash', '-c', cmd]
        return self.icmda(bash_cmd)


    ######################### utilities #########################

    def cmda(self, cmd_a):
        """
         Executes an array of commands and return both the stdout
            and stderror as a list of line.

        :param cmd_a:  array of commands
        :return: the stdout and stderr as a list of lines.
        """
        if self.logger != None:
            self.logger.getChild('steshell.icmda').info(cmd_a)

        process = subprocess.Popen(cmd_a, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = process.communicate()
        shout = ret[0].decode()
        sherr = ret[1].decode()

        if self.logger != None:
            self.logger.getChild('steshell.cmda').info("out: " + shout)
            self.logger.getChild('steshell.cmda').info("out: " + sherr)

        return shout.splitlines(), sherr.splitlines()

    def icmda(self, cmd_a):
        """
        Executes an array of commands and print output (both stdout and stderr)
        during the execution.

        :param cmd_a:  array of commands
        """
        if self.logger != None:
            self.logger.getChild('steshell.cmda').info(cmd_a)

        process = subprocess.Popen(cmd_a, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in process.stdout:
            print(line.decode(), end='')

        return