# Вы решили посчитать средний возраст
# своих друзей в ВК по городам. Для этого вы обратились
# в VK API и получили ответ vk_resp. Но у некоторых
# пользователей не указана дата рождения и город.
# Нужно учесть особенности API и доработать функцию
# calc_average_age, чтобы она обрабатывала исключения,
# то есть сделать так, чтобы код работал и не падал.
#
# Вам дана лямбда функция foo, перепишите ее на обычную функцию.


#foo = lambda **kwargs: {v: k for k, v in kwargs.items()}

def foo(**kwargs):
    name_list = {}
    for k, v in kwargs.items():
        name_list[v] = k
    return name_list

if __name__ == "__main__":
 #   print(foo(a=1, b=2))
    print(foo(a=1, b=2))
