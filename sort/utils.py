# coding=utf-8

import time

def timer(func):
    """Measure the running time of the function

    Args:
        func: the function name to be measured

    Return:
        print the runtime taken by the func
    """

    def inner(*args, **kwargs):
        t1 = time.time()  # start measuring
        f = func(*args, **kwargs)
        t2 = time.time()  # end measuring
        print(f'Runtime took {t2 - t1} seconds')
        return f

    return inner
