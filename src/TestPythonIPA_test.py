from . import TestPythonIPA

def test_TestPythonIPA():
    assert TestPythonIPA.apply("Jane") == "hello Jane"
