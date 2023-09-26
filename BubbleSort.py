import random
import time

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def random_array(a,b,c):
    arr = []
    for i in range(a):
        arr.append(random.randint(b, c))
    return arr

def read_file(a):
    file = open( a + ".txt", "r")
    data = file.read()
    file.close()
    array = eval(data)
    arr = convert_to_list(array)
    return arr

def write_file(a, arr):
    file = open(a + ".txt", "w")
    arr_str = str(arr)
    file.write(arr_str)
    file.close()

def convert_to_list(arr):
    lst = []
    for elem in arr:
        lst.append(elem)
    return lst

array = []
choice = input("Считать ваш файл или создать новый? \n 1.Считать \n 2.Создать новый \n")
if choice == '1':
    try:
        name = input("Введите название файла: ")
        array = read_file(name)
    except SyntaxError:
        print("Данные в файле неправильно заполнены, числа должны идти через запятую.")
        exit()
    except FileNotFoundError:
        print("Такого файла несуществует или его не получилось открыть, файл должен быть в формате .txt")
        exit()
elif choice == '2':
    input_str = input("Введите количество чисел, минимальный и максимальный порог чисел через пробел: ")
    print()
    input_list = input_str.split()
    arr = []
    for num in input_list:
        arr.append(int(num))
    array = random_array(arr[0],arr[1],arr[2])
    name = input("Введите название для файла: ")
    write_file(name,array)
else:
    print("Такого варианта нет, вы скорее всего ошиблись")
    exit()
if len(array) < 50:
    print("\nНеотсортированный")
    print(array)
    bubble_sort(array)
    print("\nОтсортированный")
    print(array)
else:
    start = time.time()
    bubble_sort(array)
    end = time.time()
    time = end - start
    print("Время выполнения функции:", time, "секунд")
write_file(name + " отсортированный", array)