from hitchikers.scripts import hello


def test_hello_world(capfd):
    hello.print_hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"