# 2. Написать функцию, внутри которой у нас будет объявляться
# наша функция суммирования и возвращаться в качестве
# результата работы из объемлющей функции.

def outer_function():

    def summation(*args):
        return sum(args)

    return summation


def main():
    print(outer_function())         # subtask 02
    result = outer_function()       # subtask 03
    print(result)
    print(result(1, 2, 3, 4, ))                 # subtask 04 - v1
    print(outer_function()(1, 2, 3, 4, ))       # subtask 04 - v2


if __name__ == '__main__':
    main()
