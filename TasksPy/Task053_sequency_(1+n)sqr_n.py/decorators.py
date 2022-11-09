from functools import wraps
from datetime import datetime
import time


def cacher(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        key = args[0]
        if key not in cache:
            cache[key] = func(*args)
        print(cache)
        return cache[key]

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        # time.sleep(0.000000001) #!
        end = time.time_ns()
        executing_time = end - start
        args = args[0]
        with open('log.csv', 'a+', encoding= 'utf-8') as f:
            f.write('')
        with open('log.csv', 'r+', encoding= 'utf-8') as f:
            data = f.read().splitlines()
            if data == []:
                f.write('DATE; TIME; EXECUTING_TIME; ARGUMETS; RESULT;\n')
            f.write(f'{datetime.now().strftime("%d-%M-%y")}; '\
                    f'{datetime.now().strftime("%H:%M")}; '\
                    f'{executing_time}; '\
                    f'{args}; '\
                    f'{result};\n')
        return result
    
    return wrapper