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
                    result = func(*args)
                    break
                except Exception as exc:
                    possible_exc = exc
            else:
                print(f'{restarts=}')
                raise possible_exc
            print(f'{restarts=}')
            return result

        return wrapper

    return recalling_decor


@parametric_decor(10)
def divider_fun_t02_02(numerator: int, denominator: int) -> float:
    return numerator / denominator


@parametric_decor(5)
def residues_lister_t02_02(number: int, divisors: list[int]) -> list[int]:
    return [number % div for div in divisors]


def main():
    print(divider_fun_t02_02(5, 2))
    print(divider_fun_t02_02(2, 5))
    try:
        print(divider_fun_t02_02(5, 0))
    except Exception as exc:
        print(exc)
    print(residues_lister_t02_02(num := 20, [div for div in range(1, num)]))
    print(residues_lister_t02_02(num := 20, [div for div in range(num)]))


if __name__ == '__main__':
    main()
