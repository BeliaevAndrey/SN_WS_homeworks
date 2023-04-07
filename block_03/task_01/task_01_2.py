# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед
# выполнением функции можно было задавать как параметр во время декорирования.
from typing import Callable, Any

ADV = "Покупайте наших котиков!"
ADV2 = f'\n{"Buy OUR kitties!":^80}'


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


@outer_deco(ADV2)
def function_other(num) -> tuple[int]:
    primes = [2, ] + [n for n in range(3, num, 2)
                      if all([n % d for d in range(2, int(n ** 0.5) + 1)])]
    return tuple(primes)


def main():
    print(function(20))
    print(function_other(30))


if __name__ == '__main__':
    main()
