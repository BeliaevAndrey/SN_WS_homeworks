# 1. Написать простую функцию, которая на вход принимает строку ('test') и
# целое число (3), а возвращает строку вида 'testTESTtest' - исходную строку,
# умноженную на 3, в разном регистре.
# 2. Записать эту функцию в произвольную переменную.
# Напечатать эту переменную на экран. Что вы видите?
# 3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.

def simple_function(in_string: str, multiplier: int):
    return ''.join((in_string.lower() if not i % 2 else in_string.upper()
                    for i in range(multiplier)))


print(simple_function('test', 3))   # output: testTESTtest

random_variable = simple_function
print(random_variable)      # output: <function simple_function at 0x7f3b46348430>

print(random_variable('test', 3))   # output: testTESTtest
