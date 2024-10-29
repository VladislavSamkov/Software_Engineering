class Player():
    # Инициализация полей
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # Определяем метод, для вывода информации о игроке 
    def who_am_i(self):
        print(f"My name is {self.name} and i have a category {self.category}")

class Sniper(Player):
    def __init__(self, name, damage, hp):
        # вызываем конструктор наследуемового класса
        super().__init__(name, "Sniper")
        # Дополняем конструктор новым свойством
        self.damage = damage
        self.hp = hp

        self.common_damage = 0

    def attack(self):
        self.common_damage += self.damage
        self.hp -= 14
        print(f"Нанесённый урон {self.common_damage}")
    
    def my_health(self):
        print(f"Ваше здоровье: {self.hp}")

player = Sniper("Ivan", 52, 100)
player.who_am_i()

player.my_health()

player.attack()
player.attack()

player.my_health()