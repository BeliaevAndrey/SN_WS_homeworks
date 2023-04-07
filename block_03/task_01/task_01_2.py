# 1.1 Написать декоратор, который перед запуском произвольной функции с
# произвольным набором аргументов будет показывать в консоли сообщение
# "Покупайте наших котиков!" и возвращать результат запущенной функции
from typing import Callable, Any

ADV = "Покупайте наших котиков!"


def outer_deco(d_args: Any = ADV) -> Callable:
    def decorator(func: Callable,) -> Callable:
        advertisement = d_args

        def wrapper(*args, **kwargs):
            print(advertisement)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@outer_deco()
def function(num) -> tuple[int]:
    primes = [2, ] + [n for n in range(3, num, 2)
                      if all([n % d for d in range(2, int(n ** 0.5) + 1)])]
    return tuple(primes)


@outer_deco(f'\n{"Buy OUR kitties!":^80}')
def function_other(num) -> tuple[int]:
    primes = [2, ] + [n for n in range(3, num, 2)
                      if all([n % d for d in range(2, int(n ** 0.5) + 1)])]
    return tuple(primes)


def main():
    print(function(20))
    print(function_other(30))


if __name__ == '__main__':
    main()
