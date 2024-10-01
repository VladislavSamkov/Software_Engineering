from datetime import datetime  # Импортируем класс datetime из модуля datetime
from math import sqrt  # Импортируем функцию sqrt из модуля math

def calculate_distance(coordinates):  # Определяем функцию для расчета расстояния
    return sqrt(coordinates[0] ** 2 + coordinates[1] ** 2)  # Возвращаем корень суммы квадратов координат

def main(**kwargs):  # Определяем главную функцию с аргументами в виде кортежа
    results = {key: calculate_distance(value) for key, value in kwargs.items()}  # Используем словарь для хранения результатов
    for key, result in results.items():  # Перебираем результаты
        print(result)  # Выводим каждое значение на экран

if __name__ == '__main__':  # Проверяем, запущен ли файл напрямую
    start_time = datetime.now()  # Сохраняем текущее время
    main(one=[10, 3], two=[5, 4], three=[15, 13], four=[93, 53], five=[133, 15])  # Вызываем основную функцию
    time_costs = datetime.now() - start_time  # Вычисляем разницу времени
    print(f"Время выполнения программы: {time_costs}")  # Выводим время выполнения программы
