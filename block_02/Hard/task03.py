# 4. Перенесите глобальный счетчик на уровень объемлющей функции.
# Будет ли работать наш код? Если да, то как поменялся смысл написанного кода?
# Если нет, то что надо изменить, чтобы всё заработало?
from typing import Callable, Any


def outer_function() -> [Callable, None]:

    def summation(args) -> [int, float]:
    # def summation(*args) -> [int, float]:
        print(args)
        return sum(args)

    return summation


def counter(func) -> Callable:
    count = 0

    def inner(*args) -> Any:
        nonlocal count
        count += 1
        print(f'Function "{func.__name__}" calls: {count}')
        return func()(args)       # Изменение вызова функции
        # return func()(*args)       # Изменение вызова функции

    return inner


def main():
    fun = counter(outer_function)
    print(fun)
    print(fun())
    print(fun(1, 2, 3, 4))
    print(fun(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
