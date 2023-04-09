# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд.
# Предусмотреть механизм автоматической очистки кэша в процессе выполнения функций.
from typing import Callable
from time import time_ns as _tns, time

TIME_GAP = 10


def caching_decor(func: Callable):
    params = []
    results = []
    start = time()

    def wrapper(*args):
        nonlocal params, results, start
        if (delta := time() - start) >= TIME_GAP:
            print(f'SEMAPHORE: time exceeded; delta: {delta:.2e}')
            params = []
            results = []
            start = time()
        if tuple(args) in params:
            print(f'SEMAPHORE: time normal; result cached; delta: {delta:.2e}')
            return results[params.index(args)]
        result = func(*args)
        params.append(args)
        results.append(result)
        print(f'SEMAPHORE: time normal; result calculated, delta: {delta:.2e}')
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
    for i in 1, 300_000, 3, 40_000, 99_000, :
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
