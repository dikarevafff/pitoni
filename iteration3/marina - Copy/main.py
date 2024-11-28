"""
Данный скрипт анализирует текстовый файл, подсчитывает нагрузку на пальцы
при наборе текста в двух клавиатурных раскладках: ЙЦУКЕН и ВЫЗОВ.
Также вычисляет процент нагрузки на левую и правую руки для каждой раскладки
и выводит результаты, включая визуализацию в виде гистограммы.
Используемые функции:
 count_finger_load_qwerty(text): Подсчитывает нагрузку на пальцы (ЙЦУКЕН).
- count_finger_load_vyzov(text): Подсчитывает нагрузку на пальцы (ВЫЗОВ).
- load_hand_left(list): Вычисляет процент нагрузки на левую руку.
- load_hand_right(list): Вычисляет процент нагрузки на правую руку.
- vyvod_gistogramma(layout1, layout2): Вывод итоговой гистограммы.
Входные данные:
- text (str): Путь к текстовому файлу, вводится пользователем.
Выводимые данные:
Нагрузка на левую и правую руки в процентах для раскладок: ЙЦУКЕН и Вызов.
- Гистограмма, показывающая нагрузку на каждый палец в обеих раскладах.
Пример использования:
Введите файл с текстом: ваш_файл_с_текстом.txt
ЙЦУКЕН
Нагрузка на левую руку в процентах: X% Нагрузка на правую руку в процентах: Y%
ЫЗОВ
Нагрузка на левую руку в процентах: Z% Нагрузка на правую руку в процентах: W%
"""

from functions import *
if __name__ == "__main__":
    with open('voina-i-mir.txt', "r", encoding='utf-8') as f:
        text = f.read()
    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    dictor_finger_load = count_finger_load_dictor(text)
    scoropis_finger_load = count_finger_load_scoropis(text)
    print(qwerty_finger_load)
    print(vyzov_finger_load)
    print(dictor_finger_load)
    print(scoropis_finger_load)
    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    left_vyzov = load_hand_left(vyzov_finger_load)
    right_vyzov = load_hand_right(vyzov_finger_load)
    left_dictor = load_hand_left(dictor_finger_load)
    right_dictor = load_hand_right(dictor_finger_load)
    left_scoropis = load_hand_left(scoropis_finger_load)
    right_scoropis = load_hand_right(scoropis_finger_load)
    print('ЙЦУКЕН')
    print('Нагрузка на левую руку в процентах:', left_qwerty, '%')
    print('Нагрузка на правую руку в процентах:', right_qwerty, '%')
    print('ВЫЗОВ')
    print('Нагрузка на левую руку в процентах:', left_vyzov, '%')
    print('Нагрузка на правую руку в процентах:', right_vyzov, '%')
    print('ДИКТОР')
    print('Нагрузка на левую руку в процентах:', left_dictor, '%')
    print('Нагрузка на правую руку в процентах:', right_dictor, '%')
    print('СКОРОПИСЬ')
    print('Нагрузка на левую руку в процентах:', left_scoropis, '%')
    print('Нагрузка на правую руку в процентах:', right_scoropis, '%')
    fing = ['левый мизинец', 'левый безымянный', 'левый средний', 'левый указательный', 'левый большой',
            'правый большой', 'правый указательный', 'правый средний', 'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, qwerty_finger_load))
    fing_d_vyzov = dict(zip(fing, vyzov_finger_load))
    fing_d_dictor = dict(zip(fing, dictor_finger_load))
    fing_d_scoropis = dict(zip(fing, scoropis_finger_load))
    print(fing_d_qwerty)
    print(fing_d_vyzov)
    print(fing_d_dictor)
    print(fing_d_scoropis)
    vyvod_gistogramma(qwerty_finger_load, vyzov_finger_load, dictor_finger_load, scoropis_finger_load)