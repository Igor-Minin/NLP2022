# 1. Створіть словник, зв'язавши його з змінною school, і наповніть його даними,
# які б відображали кількість учнів у десяти різних класах (наприклад, 1а, 1б, 2б, 6а, 7в і т.д.).
# 2. Дізнайтеся скільки людей в якомусь класі.
# 3. Уявіть, що в школі відбулися зміни, внесіть їх до словника:
# в трьох класах змінилася кількість учнів;
# у школі з'явилося два нових класи;
# у школі розформували один з класів.
# Зауваження:
# Користувач сам вибирає, в якому з класів (це повинен бути існуючий клас) відбудуться зміни
# і на скільки учнів кількість збільшиться чи зменшиться.
# Зміни в класах повинні бути адекватними, якщо змінити в умові кількість учнів класу.
# 4. Виведіть вміст словника на екран.

school = {
    "1a": 28,
    "2a": 25,
    "3a": 33,
    "4a": 21,
    "5a": 25,
    "6a": 20,
    "7a": 30,
    "8a": 32,
    "9a": 28,
    "10a": 27,
    "11a": 25,
    "12a": 26
}


def classesInfo():
    for i in school.keys():
        print(f'There are {school.get(i)} students in {i}')


def updateClass(numberOfClass, numberOfStudents):
    school[numberOfClass] = numberOfStudents


def addNewClass(numberOfClass, numberOfStudents):
    school[numberOfClass] = numberOfStudents


def deleteClass(numberOfClass):
    school.pop(numberOfClass)


addNewClass("5b", 26)
addNewClass("8b", 22)
deleteClass("5a")
classesInfo()
