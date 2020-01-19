import random


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100


def gen(N):
    for _ in range(N):
        yield random.randint(1, 100)


# написать генераторное выражение, которое делает то же самое
gen_v2 = lambda N: (random.randint(1, 100) for _ in range(N))

if __name__ == '__main__':
    print('--generator function works')
    numbers = gen(3)
    for n in numbers:
        print(n)
    print('\ngenerator expression-- works')
    numbers_v2 = gen_v2(3)
    for n in numbers_v2:
        print(n)
