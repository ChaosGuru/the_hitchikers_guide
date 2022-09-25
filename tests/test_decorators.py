from hitchikers.scripts import decorators


def test_hello(capfd):
    decorators.hello()
    out, err = capfd.readouterr()
    assert out == 'Decorator\nHello, World!\n'


def test_hello2(capfd):
    decorators.hello2()
    out, err = capfd.readouterr()
    assert out == 'Decorator\nHello, People!\n'