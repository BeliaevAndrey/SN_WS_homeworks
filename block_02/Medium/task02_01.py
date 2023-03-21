# 1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу
# со счетчиком аналогично той, которая была решена для запуска функции суммирования.

# function 1
def symbol_counter(smb_to_count: str, line_in: str) -> int:
    """
    Count amount of definite symbol in line
    :param smb_to_count: str
    :param line_in: str
    :return: int
    """
    amt = 0
    if len(line_in) < len(smb_to_count):
        raise TypeError('Wrong consequence of arguments.')
    for smb in line_in:
        if smb == smb_to_count:
            amt += 1
    return amt


# function 2
def longest_consequence(line_in: str) -> (str, int):
    """
    Find longest continuing consequence of symbol
    :param line_in: str
    :return: tuple [str, int]
    """
    amt = 1
    amt_max = 0
    tmp_smb = line_in[0]
    prev_smb = ' '
    for smb in line_in[1:]:
        if smb == tmp_smb:
            amt += 1
        else:
            prev_smb = [prev_smb, tmp_smb][amt_max < amt]
            amt_max = [amt_max, amt][amt_max < amt]
            amt = 1
            tmp_smb = smb
    prev_smb = [prev_smb, tmp_smb][amt_max < amt]
    amt_max = [amt_max, amt][amt_max < amt]
    return prev_smb, amt_max


# function 3
def factorial_linear(number: int) -> int:
    """linear factorial calculation"""
    result = 1
    if number == 0:
        return 1
    while number > 0:
        result *= number
        number -= 1
    return result


# function 4
def factorial_rec(number: int) -> int:
    """recursive factorial calculation"""
    if number == 0:
        return 1
    return number * factorial_rec(number - 1)


# counter function
def counting_function(func):
    count = 0

    def inner(*args):
        nonlocal count
        count += 1
        print(f'Function {func.__name__} calls: {count}')
        return func(*args)

    return inner


# def run_functions():
    # test_line1 = 'aaaabbbaabbbbbaaibmn'
    # test_line2 = 'abcdefghijkkknopqrst'
    # test_line3 = 'abcdefghijkkktttttttt'
    # test_line4 = 'zzzzzzzzzabcdefghijkkkt'
#
#     print(symbol_counter('b', test_line1), test_line1.count('b'))
#     print(longest_consequence(test_line1))                          # split case
#     print(symbol_counter('b', test_line2), test_line2.count('b'))
#     print(longest_consequence(test_line2))                          # simple case
#     print(symbol_counter('b', test_line3), test_line3.count('b'))
#     print(longest_consequence(test_line3))                          # edge case right
#     print(symbol_counter('b', test_line4), test_line4.count('b'))
#     print(longest_consequence(test_line4))                          # edge case left
#
#     res_lin, res_rec = factorial_linear(1), factorial_rec(1)
#     print(res_lin, res_rec, res_lin == res_rec)
#
#     res_lin, res_rec = factorial_linear(0), factorial_rec(0)
#     print(res_lin, res_rec, res_lin == res_rec)
#
#     res_lin, res_rec = factorial_linear(10), factorial_rec(10)
#     print(f'{res_lin=:.3e}, {res_rec=:.3e}, {res_lin == res_rec = }')
#
#     res_lin, res_rec = factorial_linear(50), factorial_rec(50)
#     print(f'{res_lin=:.3e}, {res_rec=:.3e}, {res_lin == res_rec = }')


def main():
    test_lines = ['aaaa_bbb_aa_bbbbb_aaibmn',
                  'a_b_cdefghijkkknopqrst',
                  'zzzzzzzzzabcdefghijkkkt', ]

    cnt_symbol_counter = counting_function(symbol_counter)
    cnt_longest_consequence = counting_function(longest_consequence)
    for test_line in test_lines:
        print(cnt_longest_consequence(test_line))
        print(cnt_symbol_counter('b', test_line, ))

    cnt_factorial_linear = counting_function(factorial_linear)
    cnt_factorial_rec = counting_function(factorial_rec)
    for i in range(5):
        print(cnt_factorial_linear(i))
        print(cnt_factorial_rec(i))


if __name__ == '__main__':
    # run_functions()
    main()
