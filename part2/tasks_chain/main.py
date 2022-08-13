# У вас есть список городов towns.
# Нужно написать функцию get_ids, 
# которая получит города только из Московской области,
# отсортирует их по названию и вернет список id. 
# На вход функция принимает список объектов towns, 
# на выходе функция должна возвращать список чисел (id) 

class Town:
    def __init__(self, id, name, region):
        self.id = id
        self.name = name
        self.region = region

    def __repr__(self):
        return f'{self.region} - {self.name}'


towns = [Town(1, 'Балашиха', 'МО'), Town(2, 'Химки', 'МО'), Town(3, 'Тула', 'Тульская область'), Town(4, 'Альфа', 'МО')]

 
def get_ids(towns):
    return list(map(lambda c: c.id, sorted(filter(lambda v: v.region == 'МО', towns), key=lambda v: v.name, reverse=False)))

if __name__ == "__main__":
    print(get_ids(towns))
