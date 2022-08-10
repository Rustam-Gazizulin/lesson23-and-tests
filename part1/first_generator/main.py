# С помощью функции iter нужно создать итератор,
# затем получить и вывести первые 3 элемента списка arr
# С помощью функции arr_generator нужно создать генератор,
# затем получить и вывести первые 3 элемента списка.
# Просим Вас в этом задании не пользоваться блоком if __name__ == __main__
# чтобы наши тесты могли проверить, на самом ли деле ожидаемые ответы были
# выведены в терминал

#
def arr_generator(arr):
    for item in arr:
        yield item


arr = [1, 2, 3, 4, 5]


def my_iter(data):
    it = iter(data)
    count = 0
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        print(x)
        count += 1
        if count == 3:
            break


my_iter(arr)

def my_gen(data, count):
    x = arr_generator(data)
    while count > 0:
        print(next(x))

        count -= 1

my_gen(arr, 3)



