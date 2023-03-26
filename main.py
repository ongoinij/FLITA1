from numpy import binary_repr


len = int(input("Введите, сколько элементов будет в вашем множестве: "))

listofint = set()
listofbin = set()

for i in range(0, len):
    try:
        elementint = int(input())
        listofint.add(elementint)
    except:
        continue


print("Задаем первое множество целых десятичных чисел: ", listofint)

print("Переводим целые десятичные числа в бинарные: ")

for num in list(listofint):
    elementbin = binary_repr(num)
    listofbin.add(elementbin)
    print(num, "--->", elementbin)


print("Множество целых чисел: ", listofint, "Множество бинарных чисел: ", listofbin, sep="\n")