# 3.3 Параметризовать время кэширования в декораторе.
from typing import Callable
from time import time_ns as _tns, time

TIME_GAPS = [20, 10]


def caching_decor(time_gap) -> Callable:
    def parametrized_caching_decor(func: Callable):
        params = []
        results = []
        start = time()

        def wrapper(*args):
            nonlocal params, results, start
            if (time() - start) >= time_gap:
                print(time() - start)
                params = []
                results = []
                start = time()
            if tuple(args) in params:
                return results[params.index(args)]
            result = func(*args)
            params.append(args)
            results.append(result)
            return result

        return wrapper
    return parametrized_caching_decor


@caching_decor(TIME_GAPS[0])
def factorial_calc(number: int) -> int:
    if number in (0, 1):
        return 1
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


@caching_decor(TIME_GAPS[1])
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
