# Вам дана обычная функция foo, перепишите ее на лямбду функцию.

# #def foo(n):
#     for i in range(n):
#         yield i**2


def new_foo(x):
    return list(map(lambda i: i**2, [i for i in range(x)]))


if __name__ == "__main__":
    print(new_foo(5))
    #  print([x for x in new_foo(5)])


