# Ввод целочисленного значения с клавиатуры c последующей конвертацией во float
x_str = input("Введите целое число: ")
print("Вы ввели: ", x_str)
print("Тип полученного значения - ", type(x_str))
x_float = float(x_str)
print("После конвертации во float мы получили: ", x_float)
print("Тип значения после конвертации - ", type(x_float))
