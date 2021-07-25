# Булевый тип данных
my_bool = False
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 10==10
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 140==140.0
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 32!=12
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 243==13
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 55!=55
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 85<13
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 78>=78
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 94<=5
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_bool = 84>=20
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))
print()

my_bool = 13>=122
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))
print()

my_int = 5
print('type(my_int): ', type(my_int))
my_bool = bool(my_int)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_int = 0
print('type(my_int): ', type(my_int))
my_bool = bool(my_int)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_int = None
print('type(my_int): ', type(my_int))
my_bool = bool(my_int)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_str = ''
print('type(my_str): ', type(my_str))
my_bool = bool(my_str)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_str = 'add'
print('type(my_str): ', type(my_str))
my_bool = bool(my_str)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_list = [False]
print('type(my_list): ', type(my_list))
my_bool = bool(my_list)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

my_dict = {}
print('type(my_dict): ', type(my_dict))
my_bool = bool(my_dict)
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print()

# И-И
print("Логическая операция И")
df = 91 and False
print('df: ', df)
df = False and -11
print('df: ', df)
df = False and False
print('df: ', df)
df = 0 and 0
print('df: ', df)
df = 0 and 87
print('df: ', df)
df = 21 and 0
print('df: ', df)
df = False and 0
print('df: ', df)
df = 0 and False
print('df: ', df)
df = 32 and 45
print('df: ', df)
print()

# ИЛИ-ИЛИ
print("Логическая операция ИЛИ")
df = 144.5 or False
print('df: ', df)
df = False or False
print('df: ', df)
df = False or True
print('df: ', df)
df = 6 or 8
print('df: ', df)
df = 0 or 0
print('df: ', df)
df = False or 0
print('df: ', df)
df = 0 or False
print('df: ', df)
print()


my_int = -5
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print()

my_float = 0.0
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print()

my_float = 0.0001
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print()

list_ = [8, 2, 3, 4, 'as', '']
print('len(list_): ', len(list_))
if len(list_):
    print('список имеет значения')
else:
    print('список не имеет значения')
print()

list_ = []
print('len(list_): ', len(list_))
if list_:
    print('список имеет значения')
else:
    print('список не имеет значения')
print()

my_float = -105.1
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print()

my_float = 0.
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print()

# Зміна точності
my_float = 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print('my_float = ', my_float)
print(len('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'))
print()

my_float = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
print('bool(my_float): ', bool(my_float))
print('type(my_float): ', type(my_float))
print('my_float = ', my_float)
print(len('000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'))
print()


val_1 = 321.7624634576
val_2 = 321.7624634575
print(val_1==val_2)
print(abs(val_1 - val_2) < 0.0000000001)
print()

my_str = '0'
print('bool(my_str): ', bool(my_str))
print()

my_str = ''
print('my_str: ', my_str)
print('len(my_str): ', len(my_str))
print('bool(my_str): ', bool(my_str))
print()

my_str = ' '
print('my_str: ', my_str)
print('len(my_str): ', len(my_str))
print('bool(my_str): ', bool(my_str))
print()

my_none = None
print('bool(my_none): ', bool(my_none))
print()

my_str = 'False'
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('bool(my_str): ', bool(my_str))
my_bool = True
print('my_bool: ', my_bool)
my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))
my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print()

my_str = 'False'
print('my_str: ', my_str)
print('bool(my_str): ', bool(my_str))
my_bool = False
print('my_bool: ', my_bool)
my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))
my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('bool(my_str): ', bool(my_str))
print('type(my_str): ', type(my_str))
print()

my_val = None
print('type(my_val): ', type(my_val))
print('bool(my_val): ', bool(my_val))
print()

my_val = NotImplemented
print('type(my_val): ', type(my_val))
print('bool(my_val): ', bool(my_val))
print()

my_val = Ellipsis
print('type(my_val): ', type(my_val))
print('bool(my_val): ', bool(my_val))
