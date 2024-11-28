"""
В данном файле храняться функции программы.
"""

import data1


def get_fin(a_str, g=0):
    """
    Функция перводит текст набранный в файле и
    параметр для текста является a_str
    в соответсвии с выбранным ключевым параметром g,
    где g=0-ИЦУКЕН, g=1-ДИКТОР, g=2 - vyzov, g=3
    """
    if g == 1:
        return a_str.translate(data1.fingers_map_diktor).split(',')
    if g == 0:
        return a_str.translate(data1.fingers_map_QWERTY).split(',')
    if g == 2:
        return a_str.translate(data1.fingers_map_vyzov).split(',')
    if g == 3:
        return a_str.translate(data1.fingers_map_skoropis).split(',')



def get_b_bukvi(text, g=0):
    """
    Данная функция подсчитывает сколько раз
    были нажаты шифты и пробел (левой или правой рукой)
    Параметр text: это слово который берет программа из файла
    Параметр g:определяет номер раскладки клавиатуры,
    где g = 0 - ИЦУКЕН, g = 1-ДИКТОР, g = 2-vyzov
    return: возвращает значения
    left - сколько раз был нажат левый шифт
    left_prob - сколько раз был нажат левый пробел
    right - сколько раз был нажат правый шифт
    right_prob - сколько раз был нажат правый пробел
    """
    left = 0
    left_prob = 0
    right = 0
    right_prob = 0
    if g == 0:
        for i in text:
            if i in data1.left_shift_QWERTY:
                left += 1
            if i in data1.l_s_QWERTY and i == text[-1]:
                left_prob += 1
            if i in data1.right_shift_QWERTY:
                right += 1
            if i in data1.r_s_QWERTY and i == text[-1]:
                right_prob += 1
    if g == 1:
        for i in text:
            if i in data1.left_shift_diktor:
                left += 1
            if i in data1.l_s_diktor and i == text[-1]:
                left_prob += 1
            if i in data1.right_shift_diktor:
                right += 1
            if i in data1.r_s_diktor and i == text[-1]:
                right_prob += 1
    if g == 2:
        for i in text:
            if i in data1.left_shift_vyzov:
                left += 1
            if i in data1.l_s_vyzov and i == text[-1]:
                left_prob += 1
            if i in data1.right_shift_vyzov:
                right += 1
            if i in data1.r_s_vyzov and i == text[-1]:
                right_prob += 1
    if g == 3:
        for i in text:
            if i in data1.left_shift_skoropis:
                left += 1
            if i in data1.l_s_skoropis and i == text[-1]:
                left_prob += 1
            if i in data1.right_shift_skoropis:
                right += 1
            if i in data1.r_s_skoropis and i == text[-1]:
                right_prob += 1
    return [left, right, left_prob, right_prob]


def counter(text, g=0):
    """
    Функция подсчитывает скоро раз были использованы
    палцы(левой и правой рукой) при написаннии слов
    Параметр text: это слово который берет программа из файла
    Параметр g: определяет номер раскладки клавиатуры,
    где g = 0 - ИЦУКЕН, g = 1-ДИКТОР, g = 2-vyzov, g = 3-skoropis
    return: возвращает значения пальцев
    lf1 - левый большой
    lf2 - левый указательный
    lf3 - левый средний
    lf4 - левый безымянный
    lf5 - левый мизинец
    rf1 - правый большой
    rf2 - правый указательный
    rf3 - правый средний
    rf4 - правый безымянный
    rf5 - правый мизинец
    """
    lf1 = 0
    lf2 = 0
    lf3 = 0
    lf4 = 0
    lf5 = 0
    rf1 = 0
    rf2 = 0
    rf3 = 0
    rf4 = 0
    rf5 = 0
    for i in text:
        if data1.cyr[i][g] == data1.lfi1:
            lf1 += 1
        if data1.cyr[i][g] in data1.lfi2:
            lf2 += 1
        if data1.cyr[i][g] in data1.lfi3:
            lf3 += 1
        if data1.cyr[i][g] in data1.lfi4:
            lf4 += 1
        if data1.cyr[i][g] in data1.lfi5:
            lf5 += 1
        if data1.cyr[i][g] == data1.rfi1:
            rf1 += 1
        if data1.cyr[i][g] in data1.rfi2:
            rf2 += 1
        if data1.cyr[i][g] in data1.rfi3:
            rf3 += 1
        if data1.cyr[i][g] in data1.rfi4:
            rf4 += 1
        if data1.cyr[i][g] in data1.rfi5:
            rf5 += 1
    return [lf1, lf2, lf3, lf4, lf5, rf1, rf2, rf3, rf4, rf5]
