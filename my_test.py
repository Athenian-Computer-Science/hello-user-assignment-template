import pytest
from my_code import *

global name, name2
name1 = 'Brianna'
name2 = 'Newton'

def test_greeting1(capsys):
    greeting(name1)
    captured = capsys.readouterr()
    assert captured.out == f"Hello, {name1}!\n"

def test_greeting2(capsys):
    greeting(name2)
    captured = capsys.readouterr()
    assert captured.out == f"Hello, {name2}!\n"
