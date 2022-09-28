from hitchikers.scripts import context


def test_context_manager(capfd):
    with context.ContextManager('Hello') as cm:
        assert cm == 'Hello'[:-1]

    out, err = capfd.readouterr()
    assert out == 'Context Manager ENTER\nContext Manager EXIT\n'
