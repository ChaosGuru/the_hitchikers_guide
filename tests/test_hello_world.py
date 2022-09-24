from context import hello_world


def test_hello_world(capfd):
    hello_world.print_hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"