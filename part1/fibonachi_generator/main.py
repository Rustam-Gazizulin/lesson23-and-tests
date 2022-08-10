# Напишите, свой собственный генератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Дополните функцию fib


def fib(n):
    count = 0
    fib1 = 0
    fib2 = 1
    while count < n:
        count += 1
        if count < 3:
            yield count - 1
            continue
        id = fib1 + fib2
        fib1 = fib2
        fib2 = id
        yield id


fib_gen = fib(15)

if __name__ == "__main__":
    print([x for x in fib_gen])
