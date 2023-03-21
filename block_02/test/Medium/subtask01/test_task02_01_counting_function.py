import pytest

from block_02.Medium.task02_01 import counting_function
from block_02.Medium.task02_01 import (
    factorial_rec,
    factorial_linear,
    fibonacci_rec,
)


def test_count_factorial_linear(capsys):
    """Тест вычисления факториала в цикле"""
    count_calls = counting_function(factorial_linear)
    expected_out = []
    for i in range(5):
        expected_out.append(f'Function "factorial_linear" calls: {i + 1}')
        count_calls(i)
    captured = capsys.readouterr()
    assert(expected_out == captured.out.strip().split('\n'))


def test_count_factorial_rec(capsys):
    """Тест рекурсивного вычисления факториала"""
    count_calls = counting_function(factorial_rec)
    expected_out = []
    for i in range(5):
        expected_out.append(f'Function "factorial_rec" calls: {i + 1}')
        count_calls(i)
    captured = capsys.readouterr()
    assert(expected_out == captured.out.strip().split('\n'))


def test_count_fibonacci_rec(capsys):
    """Тест рекурсивного вычисления числа фибоначчи"""
    count_calls = counting_function(fibonacci_rec)
    expected_out = []
    for i in range(5):
        expected_out.append(f'Function "fibonacci_rec" calls: {i + 1}')
        count_calls(i)
    captured = capsys.readouterr()
    assert(expected_out == captured.out.strip().split('\n'))
