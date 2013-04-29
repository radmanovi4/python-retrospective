from collections import OrderedDict


def groupby(func, sec):
    result = {}
    for i in sec:
        if func(i) in result:
            result[func(i)].append(i)
        else:
            result[func(i)] = [i]
    return result


def composition(func1, func2):
    return lambda *args: func1(func2(*args))


def iterate(func):
    composing = lambda x: x
    yield composing
    while True:
        yield composition(func, composing)
        composing = composition(func, composing)


def zip_with(func, *iterables):
    if not len(list(iterables)):
        return iter([])
    return map(lambda *args: func(*args), *iterables)


def cache(func, cache_size):
    storage = OrderedDict({})

    def func_cached(*args):
        if args in storage:
            return storage[args]
        if len(storage) >= cache_size:
            storage.popitem(False)
        storage[args] = func(*args)
        return storage[args]

    return func_cached
