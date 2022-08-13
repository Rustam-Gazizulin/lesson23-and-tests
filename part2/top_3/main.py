# Вам нужно написать функцию top3, 
# которая на вход принимает строку и 
# возвращает 3 наиболее повторяющихся элемента из входной строки. 

from collections import Counter

def top3(input_str):

    return [item[1] for item in Counter(input_str).most_common(3)]


if __name__ == "__main__":
    print(top3('1111111122222222333333334444444455555555555555555'))
