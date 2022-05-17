# Напишіть програмний код, в якому у випадку, якщо значення якоїсь змінної більше 0,
# виводилося б спеціальне повідомлення (використовуйте функцію print).
# Один раз виконайте програму при значенні змінної більше 0, другий раз - менше 0.
# Вдоскональте попередній код за допомогою гілки else так, щоб залежно від значення змінної,
# виводилося або 1, або -1.
# Самостійно придумайте програму, в якій би використовувалася інструкція if (бажано з гілкою else).
# Вкладений код повинен містити не менше трьох виразів.
a = 5
b = -5


def isPositive(num):
    if num > 0:
        print("1")
    else:
        print("-1")


isPositive(a)
isPositive(b)


def alcoholPermision(age):
    if age < 13:
        print("alcohol is forbidden")
    elif 13 < age < 18:
        print("slightly allowed")
    elif age > 18:
        print("allowed")


alcoholPermision(19)

# 1.Напишіть програму за наступним описом:
# двом змінним присвоюються числові значення;
# якщо значення першої змінної більше другої,
# то знайти різницю значень змінних (відняти від першої другу), результат присвоїти третій змінній;
# якщо перша змінна має менше значення, ніж друга,
# то третю змінну пов'язати з результатом суми значень двох перших змінних;
# у всіх інших випадках, присвоїти третій змінній значення першої змінної;
# вивести значення третьої змінної на екран.
# 2.Придумайте програму, в якій би використовувалася інструкція if-elif-else.
# Кількість гілок повинна бути як мінімум чотири.

c = 5
d = 10
answer = 0
if c > d:
    answer = c - d
elif d > c:
    answer = c + d
else:
    answer = c
print(answer)


class OldPhone:

    @staticmethod
    def playButtonSound(buttonNumber):
        if buttonNumber == 1:
            print("One")
        elif buttonNumber == 2:
            print("Two")
        elif buttonNumber == 3:
            print("Three")
        elif buttonNumber == 4:
            print("Four")
        elif buttonNumber == 5:
            print("Five")
        elif buttonNumber == 6:
            print("Six")
        elif buttonNumber == 7:
            print("Seven")
        elif buttonNumber == 8:
            print("Eight")
        elif buttonNumber == 9:
            print("Nine")
        elif buttonNumber == 0:
            print("Zero")
        else:
            print("There are only 10 buttons 0-9")


phone = OldPhone()
phone.playButtonSound(3)


# Напишіть скрипт на мові програмування Python, що виводить ряд чисел Фібоначчі (див. приклад вище).
# Запустіть його на виконання. Потім змініть код так, щоб виводився ряд чисел Фібоначчі,
# починаючи з п'ятого члена ряду і закінчуючи двадцятим.
# Напишіть цикл, що виводить ряд парних чисел від 0 до 20. Потім, кожне третє число в ряді від -1 до -21.
# Самостійно придумайте програму на Python, в якій би використовувався цикл while.
# Напишіть програму (файл example.py), яка пропонувала б користувачеві вирішити приклад 4*100-54.
# Якщо користувач напише правильну відповідь, то отримає привітання від програми, інакше - програма
# повідомить йому про помилку. (При вирішенні задачі використовуйте конструкцію if-else.)
# Перепишіть попередню програму так, щоб користувачеві пропонувалося вирішувати приклад до тих пір,
# поки він не напише правильну відповідь. (При вирішенні задачі використовуйте цикл while.)

def fibonacci(n):
    a = 0
    b = 1
    c = 0

    for i in range(n):
        c = a + b
        a = b
        b = c
    return c


def pairedNumbers(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)


def eachThirdNegative():
    for i in range(abs(-1), abs(-21)):
        if i % 3 == 0:
            print(-i)


def quiz():
    flag = False
    print("4*100-54")
    while not flag:
        print("Enter answer:")
        num = input()
        if int(num) == (4 * 100 - 54):
            print("Congratulations!")
            flag = True
        else:
            print("Try again")
            continue


for i in range(5, 20):
    print(fibonacci(i))

print("")

pairedNumbers(20)

print("")

eachThirdNegative()

quiz()
