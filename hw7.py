# 1. Дано целое число (int). Определить сколько нулей в этом числе.
my_int = 105_601_800
my_str = str(my_int)
my_count = my_str.count('0')
print(my_count)
##############################################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
# 1й вариант
my_int = 105601800
my_count = 0
my_str = str(my_int)
for digit in my_str[::-1]:
    if digit == "0":
        my_count += 1
    else:
        break
print(my_count)

# 2й вариант
my_int = 10560180000
my_count = 0
my_str = str(my_int)
while my_str.rfind('0') == len(my_str) - 1:
    my_count += 1
    my_str = my_str[:-1]
print(my_count)

# 3й вариант (самый простой вариант, почему-то пришёл в голову не сразу :))
my_int = 10560180010
my_str = str(my_int)
my_count = len(my_str) - len(my_str.rstrip('0'))
print(my_count)
##############################################################################
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
my_list_2 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
my_result = []
my_result.extend(my_list_1[::2])
my_result.extend(my_list_2[1::2])
print(my_result)
##############################################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
new_list = []
new_list.extend(my_list[1:])
new_list.extend(my_list[0])
print(new_list)
##############################################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
my_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
my_list.extend(my_list.pop(0))
print(my_list)
##############################################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
my_str = "43 больше чем 34 но меньше чем 56"
my_list = my_str.split(' ')
my_sum = 0
for item in my_list:
    if item.isdigit():
        my_sum += int(item)
print(my_sum)
##############################################################################
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = "o"
r_limit = "g"
left_index = my_str.find(l_limit)
right_index = my_str.rfind(r_limit)
sub_str = my_str[left_index + 1:right_index]
print(sub_str)
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = 'asdfghjkl'
my_list = []
index_str = 0
if len(my_str) % 2 != 0:
    my_str = my_str + "_"
while index_str < len(my_str):
    my_list.append(my_str[index_str:index_str + 2])
    index_str += 2
print(my_list)
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
my_result = []
for my_index in range(1, len(my_list) - 1):
    if my_list[my_index] > my_list[my_index - 1] + my_list[my_index + 1]:
        my_result.append(my_list[my_index])
print(len(my_result))
