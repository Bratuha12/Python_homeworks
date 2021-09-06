# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здоровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии. При инициализации случайным образом выбирается воздух, огонь или вода.
# У лучников есть дополнительная характеристика - тип лука. При инициализации случайным образом выбирается лук, арбалет или праща.
# У рыцарей есть дополнительная характеристика - тип оружия. При инициализации случайным образом выбирается меч, топор или пика.
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает только интелект.
# Лучник увеличивает только ловкость.
# Рыцарь увеличивает только силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Реализовать базовый класс Unit, с общим функционалом для всех юнитов
# Отнаследоваться от него и дополнить особенностями персонажа для Mage, Archer, Knight.
# Реализовать метод __str__ для родительского класса и наследников.
from random import choice


class Unit:
    def __init__(self, name, clan):
        self._name = name
        self.clan = clan
        self._health = 100
        self._strength = 1
        self._dexterity = 1
        self._intelligence = 1

    def __str__(self):
        return f"Персонаж:\nимя {self._name}, клан {self.clan}\n" \
               f"Характеристики: здоровье {self._health}" \
               f", сила {self._strength}, ловкость {self._dexterity}, интелект " \
               f"{self._intelligence} "

    def increase_health(self):
        if self._health <= 90:
            self._health += 10
        else:
            self._health = 100

    @staticmethod
    def _increase_skill(skill):
        if skill <= 9:
            skill += 1
        else:
            skill = 10
        return skill

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def intelligence(self):
        return self._intelligence


class Mage(Unit):
    def __init__(self, name, clan):
        super(Mage, self).__init__(name, clan)
        self._magic = choice(['воздух', 'огонь', 'вода'])

    def __str__(self):
        return f"{super().__str__()}, класс - маг, тип магии - {self._magic}"

    def increase_intelligence(self):
        self._intelligence = Unit._increase_skill(self._intelligence)

    @property
    def magic(self):
        return self._magic


class Archer(Unit):
    def __init__(self, name, clan):
        super(Archer, self).__init__(name, clan)
        self._bow = choice(['лук', 'арбалет', 'праща'])

    def __str__(self):
        return f"{super().__str__()}, класс - лучник, тип лука - {self._bow}"

    def increase_dexterity(self):
        self._dexterity = Unit._increase_skill(self._dexterity)

    @property
    def bow(self):
        return self._bow


class Knight(Unit):
    def __init__(self, name, clan):
        super(Knight, self).__init__(name, clan)
        self._weapon = choice(['меч', 'топор', 'пика'])

    def __str__(self):
        return f"{super().__str__()}, класс - рыцарь, тип оружия - " \
               f"{self._weapon}"

    def increase_strength(self):
        self._strength = Unit._increase_skill(self._strength)

    @property
    def weapon(self):
        return self._weapon


mage = Mage('Phess', 'Fireballs')
mage.increase_intelligence()
mage.increase_intelligence()
print(mage)
archer = Archer('Legolas', 'Forest shooters')
archer.increase_dexterity()
print(archer)
knight = Knight('Ричард', 'Steel shields')
knight._health = 85
knight.increase_health()
knight.increase_strength()
knight.increase_strength()
knight.increase_strength()
knight.increase_strength()
print(knight)
