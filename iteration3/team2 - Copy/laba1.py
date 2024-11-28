"""
laba1 - Фаил в котором реализуется наша программа.
Наименование переменных и за что они отвечают:
lfi1 - rfi5 - сколько раз были использованы пальцы
(левой и правой руки) на раскладке ДИКТОРе
lf1 - rf5 - сколько раз были использованы пальцы
(левой и правой руки) на раскладке ИЦУКЕНе
lfig1 - rfig5 - сколько раз были использованы пальцы
(левой и правой руки) на раскладке vyzov
lfigs1 - rfigs5 - сколько раз были использованы пальцы
(левой и правой руки) на раскладке skoropis
big_bukvas1 - счетчик больших букв для ИЦУКЕНа на левой руке
big_bukvas2 - счетчик больших букв для ИЦУКЕНа на правой руке
big_bukvas3 - счетчик больших букв для ДИКТОРа на левой руке
big_bukvas4 - счетчик больших букв для ДИКТОРа на правой руке
big_bukvas5 - счетчик больших букв для vyzov на левой руке
big_bukvas6 - счетчик больших букв для vyzov на правой руке
big_bukvas7 - счетчик больших букв для skoropis на левой руке
big_bukvas8 - счетчик больших букв для skoropis на правой руке

translate_stroka - массив, где храниться параметры букв слова для ИЦУКЕНа
translate_stroka1 - массив, где храниться параметры букв слова для ДИКТОРа
translate_stroka2 - массив, где хранятся параметры букв слова для ВЫЗОВ
"""

import klava
import re
import matplotlib.pyplot as plt
import numpy as np

lfi1, lf1, lfig1, lfigs1 = 0, 0, 0, 0
lfi2, lf2, lfig2, lfigs2 = 0, 0, 0, 0
lfi3, lf3, lfig3, lfigs3 = 0, 0, 0, 0
lfi4, lf4, lfig4, lfigs4 = 0, 0, 0, 0
lfi5, lf5, lfig5, lfigs5 = 0, 0, 0, 0

rfi1, rf1, rfig1, rfigs1 = 0, 0, 0, 0
rfi2, rf2, rfig2, rfigs2 = 0, 0, 0, 0
rfi3, rf3, rfig3, rfigs3 = 0, 0, 0, 0
rfi4, rf4, rfig4, rfigs4 = 0, 0, 0, 0
rfi5, rf5, rfig5, rfigs5 = 0, 0, 0, 0

big_bukvas1 = 0 #qwerty
big_bukvas2 = 0

big_bukvas3 = 0 #diktor
big_bukvas4 = 0

big_bukvas5 = 0 #vyzov
big_bukvas6 = 0

big_bukvas7 = 0 #skoropis
big_bukvas8 = 0

prob_left = 0
prob_left1 = 0
prob_left2 = 0
prob_left3 = 0

prob_right = 0
prob_right1 = 0
prob_right2 = 0
prob_right3 = 0

translate_stroka = []
translate_stroka1 = []
translate_stroka2 = []
translate_stroka3 = []

with open('summary.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        if line == '\n':
            continue
        text = line
        text1 = line
        text1 = re.sub(r'[^а-я, ,^А-Я,^0-9 ,.:!";+*%№()?]', '', text)
        text = text.lower()
        text = re.sub(r'[^а-я, ,^0-9,.:!";+*%№()?]', '', text)
        text = text.split()
        text1 = text1.split()
        if not text:
            break
        for i in text1:
            big = klava.get_b_bukvi(i, g=0)
            big1 = klava.get_b_bukvi(i, g=1)
            big2 = klava.get_b_bukvi(i, g=2)
            big3 = klava.get_b_bukvi(i, g=3)
            big_bukvas1 += big[0]
            big_bukvas2 += big[1]
            big_bukvas3 += big1[0]
            big_bukvas4 += big1[1]
            big_bukvas5 += big2[0]
            big_bukvas6 += big2[1]
            big_bukvas7 += big3[0]
            big_bukvas8 += big3[1]
            prob_left += big[2]
            prob_right += big[3]
            prob_left1 += big1[2]
            prob_right1 += big1[3]
            prob_left2 += big2[2]
            prob_right2 += big2[3]
            prob_left3 += big3[2]
            prob_right3 += big3[3]
        for i in text:
            translate_stroka = klava.get_fin(i, g=0)
            translate_stroka1 = klava.get_fin(i, g=1)
            translate_stroka2 = klava.get_fin(i, g=2)
            translate_stroka3 = klava.get_fin(i, g=3)
            hands = klava.counter(i, g=0)
            hands1 = klava.counter(i, g=1)
            hands2 = klava.counter(i, g=2)
            hands3 = klava.counter(i, g=3)
            lfi1 += hands[0]
            lfi2 += hands[1]
            lfi3 += hands[2]
            lfi4 += hands[3]
            lfi5 += hands[4]
            rfi1 += hands[5]
            rfi2 += hands[6]
            rfi3 += hands[7]
            rfi4 += hands[8]
            rfi5 += hands[9]
            lf1 += hands1[0]
            lf2 += hands1[1]
            lf3 += hands1[2]
            lf4 += hands1[3]
            lf5 += hands1[4]
            rf1 += hands1[5]
            rf2 += hands1[6]
            rf3 += hands1[7]
            rf4 += hands1[8]
            rf5 += hands1[9]
            lfig1 += hands2[0]
            lfig2 += hands2[1]
            lfig3 += hands2[2]
            lfig4 += hands2[3]
            lfig5 += hands2[4]
            rfig1 += hands2[5]
            rfig2 += hands2[6]
            rfig3 += hands2[7]
            rfig4 += hands2[8]
            rfig5 += hands2[9]
            lfigs1 += hands3[0]
            lfigs2 += hands3[1]
            lfigs3 += hands3[2]
            lfigs4 += hands3[3]
            lfigs5 += hands3[4]
            rfigs1 += hands3[5]
            rfigs2 += hands3[6]
            rfigs3 += hands3[7]
            rfigs4 += hands3[8]
            rfigs5 += hands3[9]

def plot_finger_load_distribution(data):
    # Имена пальцев
    fingers = ['lfi1', 'rfi1', 'lfi2', 'rfi2', 'lfi3',
               'rfi3', 'lfi4', 'rfi4', 'lfi5', 'rfi5']

    # Получение нагрузок для каждого пальца
    loads_qwerty = [data['QWERTY'][finger] for finger in fingers]
    loads_diktor = [data['DIKTOR'][finger] for finger in fingers]
    loads_vyzov = [data['VYZOV'][finger] for finger in fingers]
    loads_skoropis = [data['SKOROPIS'][finger] for finger in fingers]

    # Параметры для гистограммы
    y = range(len(fingers))

    # Ширина столбцов
    bar_height = 0.23

    # Построение гистограммы
    plt.figure(figsize=(15, 12))
    
    # Горизонтальная гистограмма для QWERTY (красный цвет)
    plt.barh([i + bar_height - 0.2 for i in y], loads_qwerty, height=bar_height, label='QWERTY', color='red')

    # Горизонтальная гистограмма для DIKTOR (синий цвет)
    plt.barh([i + bar_height for i in y], loads_diktor, height=bar_height, label='DIKTOR', color='skyblue')

    # Горизонтальная гистограмма для VYZOV (зеленый цвет)
    plt.barh([j + bar_height + 0.25 for j in y], loads_vyzov, height=bar_height, label='VYZOV', color='green')

    # Горизонтальная гистограмма для SKOROPIS (pink цвет)
    plt.barh([q + bar_height + 0.50 for q in y], loads_skoropis, height=bar_height, label='SKOROPIS', color='pink')

    # Настройки осей
    plt.xlabel('Нагрузка')
    plt.ylabel('Пальцы')
    plt.title('Сравнение нагрузки на пальцы для раскладок QWERTY, DIKTOR, VYZOV и SKOROPIS', )
    
    # Настройка оси Y с названиями пальцев
    plt.yticks([i + bar_height + 0.25 / 2  for i in y], fingers)  # Подписи на оси Y
    plt.legend()
    plt.grid(axis='y')

    # Показать график
    plt.tight_layout()
    plt.show()


# Пример данных для нагрузки (для каждого пальца левой и правой руки)
data_combined = {
    'QWERTY': {
        'lfi1': lf1 + prob_left, 'rfi1': rf1 + prob_right,
        'lfi2': lf2, 'rfi2': rf2,
        'lfi3': lf3, 'rfi3': rf3,
        'lfi4': lf4, 'rfi4': rf4,
        'lfi5': lf5 + big_bukvas1, 'rfi5': rf5 + big_bukvas2,
    },
    'DIKTOR': {
        'lfi1': lfi1 + prob_left1, 'rfi1': rfi1 + prob_right1,
        'lfi2': lfi2, 'rfi2': rfi2,
        'lfi3': lfi3, 'rfi3': rfi3,
        'lfi4': lfi4, 'rfi4': rfi4,
        'lfi5': lfi5 + big_bukvas3, 'rfi5': rfi5 + big_bukvas4,
    },
    'VYZOV': {
        'lfi1': lfig1 + prob_left2, 'rfi1': rfig1 + prob_right2,
        'lfi2': lfig2, 'rfi2': rfig2,
        'lfi3': lfig3, 'rfi3': rfig3,
        'lfi4': lfig4, 'rfi4': rfig4,
        'lfi5': lfig5 + big_bukvas5, 'rfi5': rfig5 + big_bukvas6,
    },
    'SKOROPIS': {
        'lfi1': lfigs1 + prob_left3, 'rfi1': rfigs1 + prob_right3,
        'lfi2': lfigs2, 'rfi2': rfigs2,
        'lfi3': lfigs3, 'rfi3': rfigs3,
        'lfi4': lfigs4, 'rfi4': rfigs4,
        'lfi5': lfigs5 + big_bukvas7, 'rfi5': rfigs5 + big_bukvas8,
    }
}

# Вызов функции для отображения графика
# plot_finger_load_distribution(data_combined)

# total_presses = lfi1 + prob_left1 + rfi1 + prob_right1 + lfi2 + rfi2 + lfi3 + rfi3 + lfi4 + rfi4 + lfi5 + big_bukvas3 + rfi5 + big_bukvas4
# print("all presses:", total_presses)
# print("Diktor:")
# print("lfi1 --", lfi1 + prob_left1, "rfi1 --", rfi1 + prob_right1)
# print("lfi2 --", lfi2, "rfi2 --", rfi2)
# print("lfi3 --", lfi3, "rfi3 --", rfi3)
# print("lfi4 --", lfi4, "rfi4 --", rfi4)
# print("lfi5 --", lfi5 + big_bukvas3, "rfi5 --", rfi5 + big_bukvas4)

# print()
# print("QWERTY:")
# print("lfi1 --", lf1 + prob_left, "rfi1 --", rf1 + prob_right)
# print("lfi2 --", lf2, "rfi2 --", rf2)
# print("lfi3 --", lf3, "rfi3 --", rf3)
# print("lfi4 --", lf4, "rfi4 --", rf4)
# print("lfi5 --", lf5 + big_bukvas1, "rfi5 --", rf5 + big_bukvas2)

# print()

# print("VYZOV:")
# print("lfi1 --", lfig1 + prob_left2, "rfi1 --", rfi1 + prob_right2)
# print("lfi2 --", lfig2, "rfi2 --", rfig2)
# print("lfi3 --", lfig3, "rfi3 --", rfig3)
# print("lfi4 --", lfig4, "rfi4 --", rfig4)
# print("lfi5 --", lfig5 + big_bukvas5, "rfi5 --", rfig5 + big_bukvas6)

# print("SKOROPIS:")
# print("lfi1 --", lfigs1 + prob_left3, "rfi1 --", rfigs1 + prob_right3)
# print("lfi2 --", lfigs2, "rfi2 --", rfigs2)
# print("lfi3 --", lfigs3, "rfi3 --", rfigs3)
# print("lfi4 --", lfigs4, "rfi4 --", rfigs4)
# print("lfi5 --", lfigs5 + big_bukvas7, "rfi5 --", rfigs5 + big_bukvas8)