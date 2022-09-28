from hitchikers.scripts import generator


def test_make_batches():
    items = [1, 2, 3, 4, 5, 6, 7, 8]
    batch_size = 3
    result = [[1, 2, 3], [4, 5, 6], [7, 8]]

    assert list(generator.make_batches(items, batch_size)) == result
