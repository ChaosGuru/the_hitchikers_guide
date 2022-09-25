import timeit


def concat(times: int = 50) -> str:
    result = ''
    for i in range(times):
        result += str(i)

    return result


def with_join(times: int = 50) -> str:
    result = []
    for i in range(times):
        result.append(str(i))

    return ''.join(result)


def with_comprehension(times: int = 50) -> str:
    return ''.join(str(i) for i in range(times))


if __name__=='__main__':
    print('concat: ', timeit.timeit('concat(5000)', globals=globals(), number=1000))
    print('with_join: ', timeit.timeit('with_join(5000)', globals=globals(), number=1000))
    print('with_comprehension: ', timeit.timeit('with_comprehension(5000)', globals=globals(), number=1000))