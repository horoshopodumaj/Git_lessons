import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


def game_core_v3(number):
    '''Вариант 1. Сначала устанавливаем любое random число, затем устанавливаем минимальную и
    максимальную границы диапазона чисел, которые (границы) мы будем уменьшать или увеличивать,
    в зависимости от загаданного числа. В начале работы алгоритма число, которым угадываем (predict)
    произвольное. Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    low = 0
    high = 101
    while number != predict:
        count += 1
        if number > predict:
            mid = abs((high-predict) // 2)
            low = predict
            predict = predict + mid
        elif number < predict:
            mid = abs((predict-low) // 2)
            high = predict
            predict = predict - mid

    return count


print(score_game(game_core_v3))


def game_core_v4(number):
    '''Вариант 2. Сначала устанавливаем любое random число, затем устанавливаем минимальную и
    максимальную границы диапазона чисел, которые (границы) мы будем уменьшать или увеличивать,
    в зависимости от загаданного числа. В начале работы алгоритма число, которым угадываем (predict)
     равно половине диапазона. Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    max_number = 101
    min_number = 0
    while True:
        count += 1
        predict = (max_number+min_number) // 2
        if number == predict:
            break
        elif number > predict:
            min_number = predict
        elif number < predict:
            max_number = predict

    return count


print(score_game(game_core_v4))