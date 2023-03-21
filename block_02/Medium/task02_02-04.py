# 2. Написать функцию, внутри которой у нас будет объявляться
# наша функция суммирования и возвращаться в качестве
# результата работы из объемлющей функции.
from typing import Callable


def outer_function() -> Callable:
    """Объемлющая функция"""

    def summation(*args) -> [int, float]:
        """Вложенная функция"""
        return sum(args)

    return summation    # Возврат вложенной функции


def main():
    print(outer_function())         # subtask 02; output: <function outer_function.<locals>.summation at 0x7fbec6738ca0>
    result = outer_function()       # subtask 03;
    print(result)                   # output: <function outer_function.<locals>.summation at 0x7fbec6738ca0>
    print(result(1, 2, 3, 4, ))                     # subtask 04 - v1; output: 10
    print(outer_function()(1, 2, 3, 4, 5, ))        # subtask 04 - v2; output: 15


if __name__ == '__main__':
    main()
