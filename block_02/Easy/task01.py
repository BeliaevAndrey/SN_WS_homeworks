# 1. Реализовать счетчик, который будет увеличиваться каждый раз,
# когда у нас осуществляется запуск функции суммирования.
from typing import Callable, Any


def counter(func) -> Callable:
    count: int = 0

    def inner(*args) -> Any:
        nonlocal count
        count += 1
        print(f'{count=}')
        return func(*args)
    return inner


def summation(*args) -> [int, float]:
    return sum(args)


print(summation(1, 2, 3, 4, 5))

fun = counter(summation)

for _ in range(5):
    print(fun(1, 2, 3, 4, 15))
