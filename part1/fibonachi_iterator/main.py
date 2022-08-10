# Напишите, свой собственный итератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Для решения задачи нужно дополнить класс Fib
# Достаточно будет сделать итератор только для положительных чисел


class Fib:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.fib1 = 0
        self.fib2 = 1
        # TODO напишите Ваш код здесь

    def __iter__(self):
        return self

    def __next__(self):
        # TODO напишите Ваш код
        if self.n > self.count:
            self.count += 1
            if self.count < 3:
                return self.count - 1

            id = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = id

            return id
        else:
            raise StopIteration


fib = Fib(15)

if __name__ == "__main__":
    print([x for x in fib])
