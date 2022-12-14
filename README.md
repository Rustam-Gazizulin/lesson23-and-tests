# Урок 23
Для начала работы скопируйте репозиторий на локальную машину:
c помощью команды в терминале

`https://github.com/skypro-008/lesson23-and-tests.git`

Откройте склонированный репозиторий в PyCharm.

### Cоздайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm
Появляется всплывающее окно, Creating virtuan envrironment c тремя полями.
В первом поле выбираем размещение папки с вирутальным окружением, как правило это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпритатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран фаил requirements.txt, находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson23-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значек ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

#### Настройка виртуального окружения завершена!

### Порядок выполнения заданий
#### Часть 1:

- part1/catch_a_string
- part1/exception
- part1/average_age
- part1/first_generator
- part1/fibonachi_iterator
- part1/fibonachi_generator
- part1/func_to_generator
- part1/string_to_ascii_list
- part1/string_to_ascii_dict
- part1/string_to_ascii_gen
- part1/tolerance
- part1/from_for_to_listc
- part1/from_listc_to_dict

#### Часть 2:

- part2/lambda+
- part2/foo_bar_test+
- part2/city_expert+
- part2/region_cities+
- part2/sorted_cities+
- part2/tasks_chain+
- part2/streets_numbering+
- part2/top3+
- part2/counting



Задачи описаны в комментариях в файле main.py
В текущих заданиях вы будете изучать функциональное 
программирование. И учиться применять его для простых задач
После того, как Вы выполнили  задание, 
попробуйте запустить фаил main.py.
Вы можете это сделать, кликнув на него правой кнопкой мыши в окне проекта.

*Обращаем ваше внимание, что для каждого задания предусмотрены свои тесты
и запускать нужно именно те тесты, которые находятся в папке с заданием*

*Пожалуйста, запускайте тесты с помощью файла tests_runner.py*

