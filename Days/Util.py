from datetime import datetime

class Util:
    def time_me(func):
        def wrapped(*args, **kwargs):

            start_time = datetime.now()
            print(f'Function - {func.__name__} started at {start_time}')

            result = func(*args, **kwargs)

            end_time = datetime.now() - start_time
            print(f'Function - {func.__name__} took: {end_time}')
            return result

        return wrapped

    def cache_me(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result

        return wrapper

