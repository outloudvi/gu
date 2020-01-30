from gu import cli
from gu.sender import StdoutSender

import os


def test_stdout_package():
    pkg = StdoutSender({})
    pkg.sendText("hello, world")


def test_cli():
    assert os.system("gu --sender stdout hello") == 0
