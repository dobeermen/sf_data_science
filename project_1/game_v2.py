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
    d1 = 1
    d2 = 100


    while number != predict:
        count += 1
       
        if number > predict:
            d1 = predict           
            predict = np.random.randint(d1, d2+1)  
                     
        elif number < predict:
            d2 = predict
            predict = np.random.randint(d1, d2+1)            
            
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