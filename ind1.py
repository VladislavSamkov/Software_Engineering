class Player():
    # Инициализация полей
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # Определяем метод, для вывода информации о игроке 
    def who_am_i(self):
        print(f"My name is {self.name} and i have a category {self.category}")

player1 = Player("Ivan", "Sniper")
player1.who_am_i()