# Ввод дробного значения с клавиатуры c последующей конвертацией в int
x_str = input("Введите число с плавающей запятой: ")
print("Вы ввели: ", x_str)
print("Тип полученного значения - ", type(x_str))
x_float = float(x_str)
x_int = int(x_float)
print("После конвертации в int мы получили: ", x_int)
print("Тип значения после конвертации - ", type(x_int))