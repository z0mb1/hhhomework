from decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    operations = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '/': lambda a, b: a / b,
                  '*': lambda a, b: a * b,
                  '**': lambda a, b: a ** b}
    assert operation in operations.keys()
    return operations[operation](a, b)


def get_number():
    while True:
        number = input('Введите число: ')
        try:
            number = int(number)
            break
        except ValueError:
            print(f'введенный символ {number} не является числом')
    return number


if __name__ == '__main__':
    a = get_number() # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    b = get_number()
    action = input('Введите операцию')
    print('Результат: ', calculator(a, b, action))

