import time

def time_measure(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print('Function %s, finished in %s' % (f.__name__, end - start))
        return res
    return wrapper