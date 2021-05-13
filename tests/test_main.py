import unittest

from app import app

def test_test():
    app.run()
    assert app.start() == "Start Now!"
    