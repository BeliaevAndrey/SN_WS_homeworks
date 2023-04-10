# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд.
# Предусмотреть механизм автоматической очистки кэша в процессе выполнения функций.
from typing import Callable, Any
from time import time_ns as _tns, time
from functools import wraps

TIME_GAP = 10


class Storage:
    """ Storage class for caching decorator. """
    _cache_dct = {}
    _subst = 'time normal; result calculated;'

    @classmethod
    def check_func(cls, func_name) -> bool:
        """ A check if function had been  called before. """
        return func_name in cls._cache_dct

    @classmethod
    def check_para(cls, func_name, params) -> bool:
        """ A check if function has been called with certain parameters before. """
        return params in cls._cache_dct[func_name]['params']

    @classmethod
    def get_results(cls, func_name, params) -> Any:
        """ Get a results of function if they are not expired. """
        for item in cls._cache_dct[func_name]['info']:
            if item[0] == params:
                if time() - item[1] < TIME_GAP:
                    return item[2]
                else:
                    cls._cache_dct[func_name]['info'].remove(item)
                    return None

    @classmethod
    def set_func_results(cls, func_name, params, results) -> None:
        """ Set a results of function if they are absent or expired. """
        if func_name not in cls._cache_dct:
            cls._cache_dct[func_name] = {
                'params': [params],
                'info': [(params, time(), results)],
            }
        elif params not in cls._cache_dct[func_name]['params']:
            cls._cache_dct[func_name]['params'].append(params)
            cls._cache_dct[func_name]['info'].append((params, time(), results))
        else:
            cls._cache_dct[func_name]['info'].append((params, time(), results))


def caching_decor(func: Callable) -> Callable:
    deco_cache = Storage()
    fin_str = format('SEMAPHORE (v2): {}')

    @wraps(func)
    def wrapper(*args) -> Any:
        nonlocal deco_cache
        subst = 'time normal; result calculated;'
        if (deco_cache.check_func(func.__name__) and
                deco_cache.check_para(func.__name__, args)):
            subst = 'time exceeded; result calculated;'
            if result := deco_cache.get_results(func.__name__, args):
                print(fin_str.format('time normal; result cached;'))
                return result

        result = func(*args)
        deco_cache.set_func_results(func.__name__, args, result)
        print(fin_str.format(subst))
        return result

    return wrapper


@caching_decor
def factorial_calc(number: int) -> int:
    if number in (0, 1):
        return 1
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


@caching_decor
def factorials_row(number: int) -> dict:
    resulting_dct = {}
    for i in range(number + 1):
        resulting_dct[i] = factorial_calc(i)
    return resulting_dct


def main():
    start = _tns()
    for i in 1, 3, 40_000, 99_000, 300_000:
        factorial_calc(i)
    end1 = _tns() - start

    start = _tns()
    for i in 1, 300_000, 3, 40_000, 99_000:
        factorial_calc(i)
    end2 = _tns() - start

    start = _tns()
    for i in 1, 3, 40_000, 99_000, 300_000:
        factorial_calc(i)
    end3 = _tns() - start
    print(f'time wasted:'
          f'\nlap 1: {end1 / 1e9}'
          f'\nlap 2: {end2 / 1e9}'
          f'\nlap 3: {end3 / 1e9}')
    print()

    start = _tns()
    for i in 1, 200, 3, 4, 50:
        factorials_row(i)
    end4 = _tns() - start

    start = _tns()
    for i in 1, 200, 3, 4, 50:
        factorials_row(i)
    end5 = _tns() - start

    print(f'time wasted: '
          f'\nlap 1: {end4 / 1e9:.2e}'
          f'\nlap 2: {end5 / 1e9:.2e}')
    print()


if __name__ == '__main__':
    main()
