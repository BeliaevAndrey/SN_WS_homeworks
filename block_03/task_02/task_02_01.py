# 2.1 Написать декоратор, который внутри себя выполнял бы функцию
# и возвращал бы результат её работы в случае успешного выполнения.
# В случае возникновения ошибки во время выполнения функции нужно
# сделать так, чтобы выполнение функции было повторено ещё раз с
# теми же самыми аргументами, но не более 10 раз. Если после
# последней попытки функцию так и не удастся выполнить успешно,
# то бросать исключение.
from typing import Callable


def recalling_decor(func: Callable) -> Callable:
    possible_exc = None

    def wrapper(*args, **kwargs):
        restarts = 10
        nonlocal possible_exc
        while restarts:
            restarts -= 1
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                possible_exc = exc
        else:
            raise possible_exc

    return wrapper


@recalling_decor
def divider_fun(numerator: int, denominator: int) -> float:
    return numerator / denominator


@recalling_decor
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
