# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция
# будет запущена с теми параметрами с которыми она уже запускалась - брать
# результат из кэша и не производить повторное выполнение функции.
from typing import Callable
from time import time_ns as _tns


def caching_decor(func: Callable):
    params = []
    results = []

    def wrapper(*args):
        nonlocal params, results
        if tuple(args) in params:
            return results[params.index(args)]
        result = func(*args)
        params.append(args)
        results.append(result)
        return result

    return wrapper


@caching_decor
def factorial_calc(number: int) -> int:
    if number == 0:
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
    for i in 1, 20, 3, 4, 50:
        factorial_calc(i)
    end1 = _tns() - start

    start = _tns()
    for i in 1, 20, 3, 4, 50:
        factorial_calc(i)
    end2 = _tns() - start

    start = _tns()
    for i in 1, 20, 3, 4, 50:
        factorial_calc(i)
    end3 = _tns() - start
    print(f'times wasted:'
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

    print(f'times wasted: '
          f'\nlap 1: {end4 / 1e9:.2e}'
          f'\nlap 2: {end5 / 1e9:.2e}')
    print()


if __name__ == '__main__':
    main()
