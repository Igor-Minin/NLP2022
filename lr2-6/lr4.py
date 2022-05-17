# 1. Присвойте змінній з будь-який рядок, що складається не менше ніж з 8 символів.
# Вийміть з рядка перший символ, потім останній, третій з початку і третій з кінця.
# Виміряйте довжину вашого рядка.
# 2. Присвойте змінній довільний рядок довжиною 10-15 символів та отримайте з неї наступні зрізи:
# перші вісім символів;
# чотири символи з центру рядка;
# символи з індексами кратними трьом.

initialLine = "lorem ipsum dolor sit amet"


def cutLine(line):
    line = line[1:]
    line = line[:-1]
    line = line[:3] + line[4:]
    line = line[:-4] + line[-3:]
    return line


print(len(initialLine))
currentLine = cutLine(initialLine)
print(len(currentLine))
print(currentLine)

print("")

print(initialLine[:8])
middleOfTheLine = int((len(initialLine) / 2))
print(initialLine[middleOfTheLine:][:4])
print(initialLine[::3][1:])

# Практична робота
# Створіть два будь-яких списки і зв'яжіть їх із змінними.
# Вийміть з першого списку другий елемент.
# Змініть в другому списку останній об'єкт. Виведіть список на екран.
# З'єднайте обидва списки в один, присвоївши результат новій змінній. Виведіть отриманий список на екран.
# "Зніміть" зріз з об'єднаного списку так, щоб туди потрапили деякі частини обох перших списків.
# Зріз зв'яжіть з якоюсь новою змінною. Виведіть значення цієї змінної.
# Додайте до цього списку-зріза два нові елементи і знову виведіть його.

list1 = ["a", "b", "c", "d", "e"]
list2 = [1, 2, 3, 4, 5]
list1.pop(2)
print(list1)
list2[-1] = -1
print(list2)
list3 = list1 + list2
print(list3)
list4 = list3[3:8]
print(list4)
list4.append("new")
list4.append("element")
print(list4)
