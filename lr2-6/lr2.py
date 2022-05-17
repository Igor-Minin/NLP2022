# Змінній var_int надайте значення 10, var_float - значення 8.4, var_str - "No".
# Змініть значення, збережене у змінній var_int, збільшивши його в 3.5 рази,
# результат зв'яжіть зі змінною big_int.
# Змініть значення, збережене у змінній var_float, зменшивши його на одиницю,
# результат зв'яжіть з тією ж змінною.
# Розділіть var_int на var_float, а потім big_int на var_float.
# Результат даних виразів не прив'язуйте ні до яких змінних.
# Змініть значення змінної var_str на "NoNoYesYesYes".
# При формуванні нового значення використовуйте операції конкатенації (+) і повторення рядка (*).
# Виведіть значення всіх змінних.

var_int = 10
var_float = 8.4
var_str = "No"

big_int = var_int * 3.5
var_float -= 1
var_int / var_float
big_int / var_float
var_str = "No" * 2 + "Yes" * 3
print("var_int =", var_int)
print("var_float =", var_float)
print("big_int =", big_int)
print("var_str =", var_str)

# Присвойте двом змінним будь-які числові значення.
# Складіть чотири складних логічних вирази за допомогою оператора and,
# два з яких повинні давати True, а два інших - False.
# Аналогічно виконайте п. 2, але вже використовуючи оператор or.
# Спробуйте використовувати у складних логічних виразах роботу зі змінними рядкового типу.
a = 2
b = -5
print((a + b) and (b - a) < 0)
print(a and not b)
print(not not b)
print(not a)
print("")
print((a or b) == b)
print(not a or not b)
print(not (not a or not b))
print(a + b == 3 or b < 5)
