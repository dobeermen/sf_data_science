import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число.
        Далее в цикле, в зависимости больше или меньше предпологаемое число загадонного, 
        определяем диапазон возможного вхождения загадонного числа.
        Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    # Диапазон поиска загаданного числа number
    range_1 = 1
    range_2 = 100

    while number != predict:
        count += 1
       
        if number > predict:
            range_1 = predict           
            predict = np.random.randint(range_1, range_2+1)                     
        elif number < predict:
            range_2 = predict
            predict = np.random.randint(range_1, range_2+1)            
            
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
#Run benchmarking to score effectiveness of all algorithms

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)