from collections import defaultdict, OrderedDict


def groupby(func, seq):
    grouped_elements = defaultdict(list)
    for element in seq:
        grouped_elements[func(element)].append(element)
    return dict(grouped_elements)


def composition(func1, func2):
    return lambda *args: func1(func2(*args))


def iterate(func):
    composing_function = lambda x: x
    yield composing_function
    while True:
        yield composition(func, composing_function)
        composing_function = composition(func, composing_function)


def zip_with(func, *iterables):
    if not len(list(iterables)):
        return iter([])
    return map(lambda *args: func(*args), *iterables)


def cache(func, cache_size):
    storage = OrderedDict({})
    if cache_size <= 0:
        return func

    def func_cached(*args):
        if args in storage:
            return storage[args]
        if len(storage) >= cache_size:
            storage.popitem(False)
        storage[args] = func(*args)
        return storage[args]

    return func_cached
