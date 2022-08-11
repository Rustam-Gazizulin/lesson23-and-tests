# Вам дана обычная функция foo, перепишите ее на лямбду функцию.

# #def foo(n):
#     for i in range(n):
#         yield i**2


new_foo = lambda x: (i**2 for i in range(x))

if __name__ == "__main__":
    #  print([x for x in new_foo(5)])
    print(list(new_foo(5)))

