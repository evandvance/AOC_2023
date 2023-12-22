from datetime import datetime

def time_me(func):
    def wrapped(*args, **kwargs):

        start_time = datetime.now()
        print(f'Started at {start_time}')

        result = func(*args, **kwargs)

        end_time = datetime.now() - start_time
        print(f'Function: {func.__name__} took: {end_time}')
        return result

    return wrapped
