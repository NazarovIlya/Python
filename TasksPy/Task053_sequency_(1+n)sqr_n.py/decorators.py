from functools import wraps


def cacher(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        print(cache)
        return cache[key]
    
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args = args[0]
        with open('log.csv', 'a+', encoding= 'utf-8') as f:
            f.write('')
        with open('log.csv', 'r+', encoding= 'utf-8') as f:
            data = f.read().splitlines()
            if data == []:
                f.write('DATE; TIME; ARGS; RESULT;\n')
            f.write(f'{datetime.now().strftime("%d-%M-%y")}; '\
                    f'{datetime.now().strftime("%H:%M")}; '\
                    f'{args}; '\
                    f'{result}\n')
        return result
    return wrapper