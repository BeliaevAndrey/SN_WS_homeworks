# 1. Реализовать счетчик, который будет увеличиваться каждый раз,
# когда у нас осуществляется запуск функции суммирования.

def counter(func, count: list[int]):

    def inner(*args):
        nonlocal count
        count[0] += 1
        return func(*args)
    return inner


def summation(*args):
    return sum(args)


print(summation(1, 2, 3, 4, 5))
call_amt = [0]
fun = counter(summation, call_amt)

for _ in range(5):
    print(fun(1, 2, 3, 4, 15))
    print(*call_amt)
