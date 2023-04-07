# 1.1 Написать декоратор, который перед запуском произвольной функции с
# произвольным набором аргументов будет показывать в консоли сообщение
# "Покупайте наших котиков!" и возвращать результат запущенной функции
from typing import Callable

ADV = "Покупайте НАШИХ котиков!"


def decorator(func: Callable) -> Callable:
    advertisement = ADV

    def wrapper(*args, **kwargs):
        print(advertisement)
        return func(*args, **kwargs)

    return wrapper


@decorator
def function_1(num) -> tuple[int]:
    primes = [2, ] + [n for n in range(3, num, 2)
                      if all([n % 2] + [n % d for d in range(3, int(n ** 0.5) + 1, 2)])]
    return tuple(primes)


@decorator
def function_2(num: int, low_lim: int = 11, ) -> tuple[int]:
    def is_prime(tst_nm: int) -> bool:
        return all([tst_nm % 2] + [tst_nm % d for d in range(3, int(tst_nm ** 0.5) + 1, 2)])

    if low_lim > num:
        return tuple()
    if low_lim >= 2:
        primes = []
    else:
        primes = [2, ]
        low_lim = 3
    primes += [n for n in range(low_lim, num) if is_prime(n)]
    return tuple(primes)


def main():
    print(function_1(10))
    print(function_2(101, 99))
    print(function_2(20, 5))
    print(function_2(20, -1))
    print(function_2(20, low_lim=14))


if __name__ == '__main__':
    main()
