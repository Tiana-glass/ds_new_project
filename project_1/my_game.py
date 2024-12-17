import numpy as np

# Создаем функцию для угадывания числа
def game_core(number: int = 1) -> int:
    """Угадываем число с помощью метода половинного деления
    (метод дихотомии), используя информацию о больше или меньше.
    Функция принимает загаданное число и возвращает количество попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    
    count = 0
    min_value = 0
    max_value = 101
    
    while True:
        count += 1
        predict = (min_value + max_value)//2
        if number == predict:
            # Выход из цикла, если угадали
            break
        elif number > predict:
            min_value = predict
        else:
            max_value = predict
    
    return count


# Создаем функцию для оценки работы алгоритма угадывания
def score_game(game_core) -> int:
    """За какое количество попыток в среднем за 1000 подходов 
    алгоритм угадывает число.

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)
    # Загадываем список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    # Находим среднее количество попыток
    score = int(np.mean(count_ls))
    
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")

print('Run benchmarking for game_core: ', end='')
score_game(game_core)