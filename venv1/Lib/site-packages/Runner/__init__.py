#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#   Author(s): Milan Falesnik   <milan@falesnik.net>
#                               <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__version__ = "1.1"

class Run(object):

    """
        A class for running shell commands.
        To run a command, use the Run.command(...) class method.
        Result contains stdout, stderr, rc and run command:
        self.stdout, self.stderr, self.rc, self.command.
        Result is usable in if, if the $?=0, if evaluates as True.

        Run.bash() runs the bash script provided as a parameter.
    """

    import subprocess
    import shlex
    import os

    def __init__(self, stdout, stderr, stdin, rc, command, shell=False):
        """ Constructor, self-explaining :)

        """
        self.stdout = stdout
        self.stderr = stderr
        self.stdin = stdin
        self.rc = rc
        self.command = command
        self.shell = shell

    def __repr__(self):
        return "<Run->%d stdout='%s...' stderr='%s...'>" % (self.rc, self.stdout[:16].strip(), self.stderr[:16].strip())

    def __nonzero__(self):
        """ Used for testing in if- and similar statements.

            Example:
            passwd = common.shell.Run.command("cat /etc/shadow)
            if passwd:
                print "Yay :)"
            else:
                print "Booo"

        :returns: True if the $? is 0
        """
        return self.rc == 0

    def rerun(self):
        """ Performs a new run of the command which produced this result

        :returns: Instance of Run() class
        """
        return Run.command(self.command, self.stdin)

    def AssertRC(self, rc=0):
        """ Assert used for testing on certain RC values

        :raises: ``AssertionError``
        """
        assert self.rc == rc, "Command `%s` failed. $? expected: %d, $? given: %d" % (self.command, rc, self.rc)

    @classmethod
    def command(cls, command, stdin=None, shell=False):
        """ Runs specified command.

        The command can be fed with data on stdin with parameter ``stdin``.
        The command can also be treated as a shell command with parameter ``shell``.
        Please refer to subprocess.Popen on how does this stuff work

        :returns: Run() instance with resulting data
        """
        if not shell and isinstance(command, str):
            command = cls.shlex.split(command)
        collate_original = None
        try:
            collate_original = cls.os.environ['LC_ALL']
        except KeyError:
            pass
        cls.os.environ['LC_ALL'] = "C"  # Because of my czech locale, YUCK! :)
        try:
            process = cls.subprocess.Popen(command,
                                           stdout=cls.subprocess.PIPE,
                                           stderr=cls.subprocess.PIPE,
                                           stdin=cls.subprocess.PIPE,
                                           shell=shell)
            (stdout, stderr) = process.communicate(stdin)
        finally:
            if collate_original:
                cls.os.environ['LC_ALL'] = collate_original
            else:
                del cls.os.environ['LC_ALL']
        return cls(stdout, stderr, stdin, process.returncode, command)

    @classmethod
    def bash(cls, script_body, stdin=None):
        """ Uses Run.command(...) to open bash shell and feed it with script from string ``script_body``.

        :returns: Run() instance with resulting data
        """
        return Run.command(["bash", "-c", script_body], stdin=stdin)
