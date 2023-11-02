

def save_call_to_file(func):
    def inner(*args, **kwargs):

        function_name=func.__name__
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{function_name}\n')

        result=func(*args, **kwargs)
        return result

    return inner()