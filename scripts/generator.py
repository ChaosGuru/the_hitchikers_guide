def make_batches(items: list, batch_size: int) -> list:
    current_batch = []

    for item in items:
        current_batch.append(item)

        if (len(current_batch) == batch_size):
            yield current_batch
            current_batch = []

    if current_batch:
        yield current_batch


if __name__ == '__main__':
    print(list(make_batches([1, 2, 3, 4, 5, 6, 7, 8], 3)))
