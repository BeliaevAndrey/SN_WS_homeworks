# 2.2 Параметризовать декоратор таким образом, чтобы количество попыток
# выполнения функции можно было задавать как параметр во время декорирования.
from typing import Callable, Any


def parametric_decor(calls_amt) -> Callable:

    def recalling_decor(func: Callable) -> Callable:
        possible_exc = None

        def wrapper(*args) -> Any:
            restarts = calls_amt
            nonlocal possible_exc
            while restarts:
                restarts -= 1
                try:
                    return func(*args)
                except Exception as exc:
                    possible_exc = exc
            else:
                raise possible_exc

        return wrapper

    return recalling_decor


@parametric_decor(10)
def divider_fun(numerator: int, denominator: int) -> float:
    return numerator / denominator


@parametric_decor(5)
def residues_lister(number: int, divisors: list[int]) -> list[int]:
    return [number % div for div in divisors]


def main():
    print(divider_fun(5, 2))
    print(divider_fun(2, 5))
    try:
        print(divider_fun(5, 0))
    except Exception as exc:
        print(exc)
    print(residues_lister(num := 20, [div for div in range(1, num)]))
    print(residues_lister(num := 20, [div for div in range(num)]))


if __name__ == '__main__':
    main()
