class BaseActions:
    def run():
        pass
    def stop():
        pass

class Player(BaseActions):
    # Инициализация полей
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # Определяем метод, для вывода информации о игроке 
    def who_am_i(self):
        print(f"My name is {self.name} and i have a category {self.category}")

    # Переопределение методов
    def run(self):
        print(f"Персонаж {self.name} побежал")

    def stop(self):
        print(f"Персонаж {self.name} остановился")

class Sniper(Player):
    def __init__(self, name, damage, hp):
        # вызываем конструктор наследуемового класса
        super().__init__(name, "Sniper")
        # Дополняем конструктор новым свойством
        self._damage = damage # Защищённое свойство
        self._hp = hp # Защищённое свойство

        self.__common_damage = 0 # Приватное свойство

    def attack(self):
        self.__common_damage += self._damage
        self._hp -= 14
        print(f"Нанесённый урон {self.__common_damage}")
    
    def my_health(self):
        print(f"Ваше здоровье: {self._hp}")

player = Sniper("Ivan", 52, 100)
player.who_am_i()

player.my_health()

player.run()
player.stop()

player.attack()
player.attack()

player.my_health()