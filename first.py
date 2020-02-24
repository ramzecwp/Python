print("Goodbye, World!")
a = 2
b = 3
print(a+b) # print - печатать
print(a+b)
a = 3e4 # e показывает степень десяти
с = "hello world" # " " и '' нет разницы
d = '''в пределах тройных кавычек можно использовать другие кавычки'''
# строки нельзя изменять
# format
age = 26
name = 'Ramil'
print('Возраст {0} -- {1} лет.'.format(name, age)) # 0 - это name 1 - это age
print('Возраст'+ name + ' -- ' + str(age) + ' лет.') # пример аналогично верхнему
print('Возраст {} -- {} лет.'.format(name, age)) # так тоже можно
i = 3
print(i)
i = 3;
print(i);
i = 3; print(i) # можно и так и сяк
print\
(i) #можно так делать если длинная строка
print('a' + 'b')

# ** степень // целочисленое деление % остаток от деления << сдвиг влево по битам >> сдвиг
# вправо по битам & побитовое и | побитовое или != не равно not логическо не x = true; not x
# дает false and и or или - это операторы

# команды

number = 23
guess = int(input('Введите целое число : '))
if guess == number:
 print('Поздравляю, вы угадали,') # отступ важен
 print('(хотя и не выиграли никакого приза!)')
elif guess < number: # else  и if это elif
 print('Нет, загаданное число немного больше этого.')
else:
 print('Нет, загаданное число немного меньше этого.')
print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if

# while - оператор цикла, может выполняться многократно

number = 23
running = True # булево
while running: # ruhning == true
    guess  = int(input('введите целое число: '))
    if guess == number:
        print('вы угадали')
        running = False
    elif guess < number:
        print('Нет, загаданное больше этого')
    else:
        print('Нет, загаданное меньше этого')
else:
     print('Цикл while окончен')
print ('завершение')

# for

for i in range(1, 5): # range делает шаги 1-2-3-4-5 -- 4 шага , задав 3 число можно указать
# размер шага range(1, 5, 2) будет 1 и 3 выведено, 2 число цикл в себя не включает
    print(i)
else:
    print('Цикл For окончен')

    # опратор break - служит для прерывания цикла, можно применять и в for

while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    print ('Длинна строки: ', len(s))
print('завершение')

#* continue - позводяет пропустить все оставшиеся команды цикла и продолжить со следующей итерации цикла

while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print('Введенная строка достаточной длинны')

# функции

def sayHello():
    print('Hello, world')
    # конец функции
sayHello() # вызов функции
sayHello()
def printMax(x, y):
    if x > y:
        print(x, 'максимально')
    elif x == y:
        print(x, 'равно', y)
    else:
        print(y, 'максимально')
printMax(3, 4) # прямая прередача значений
x = 7
y = 3
printMax(x, y)

# локальные переменные (внимательно читай вывод)

z = 50
def func(z):
    print ('z raven ', z)
    z = 2 # z вне функции остается нетронутым
    print('Zamena lokalnogo z na ', z)
func(z)
print('z po pregnemu ', z)

z = 60
def func1():
    global z # можно сразу несколько объявить global z, x, y
    print ('z raven ', z)
    z = 2 # z вне функции остается нетронутым
    print('Zamena globalnogo z na ', z)
func1()
print('z teper ', z)

# nonlocal для функции в функции стр 63 укус питона

# по умальчанию - если пользователь не ввел значение переменной это значение
# будет изначально

def say (massage, times = 1):
    print(massage * times)
say('Privet')
say('Mir', 5)
# def say(massage = 1, times) - недопустимо
# стр 65
# для любого числа параметров 10.7 стр 65

# return - возврат из функции
def max(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа Равны'
    else:
        return y
print(max(2, 3))

# строки документации (docstring)

def max1(x,y):
    '''Выводит максимальное из  2 чисел.

    Оба значения должны быть целыми.'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'max')
    else:
        print(y, 'max')
max1(3, 5)
print(max1.__doc__)
