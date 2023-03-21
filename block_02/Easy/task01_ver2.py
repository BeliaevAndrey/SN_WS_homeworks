# 1. Реализовать счетчик, который будет увеличиваться каждый раз,
# когда у нас осуществляется запуск функции суммирования.
class CountCalls:
    _count: int

    def __init__(self, start: int = 0) -> None:
        self._count = start

    def __iadd__(self, other: int) -> 'CountCalls':
        self._count = self._count + other
        return self

    def __add__(self, other: int) -> 'CountCalls':
        return CountCalls(self._count + other)

    def __int__(self) -> int:
        return self._count

    def get_calls_amt(self) -> int:
        return self._count

    def __str__(self) -> str:
        return f'Call count: {self._count}'

    def __repr__(self) -> str:
        return f'Call count: {self._count}'


def counter(func, count: CountCalls):

    def inner(*args):
        nonlocal count
        count += 1
        print(f'{count=}')
        return func(*args)
    return inner


def summation(*args):
    return sum(args)


print(summation(1, 2, 3, 4, 5))
call_amt = CountCalls()
fun = counter(summation, call_amt)

for _ in range(5):
    print(fun(1, 2, 3, 4, 15))
    print(call_amt)
