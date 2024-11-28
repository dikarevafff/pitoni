import matplotlib.pyplot as plt
import numpy as np

def giver(the_dict):
    the_list = list(the_dict.values())
    l_list = the_list[:4]
    r_list = the_list[4:8]
    thumb = the_list[8]
    return l_list, r_list, thumb


def input(list1, list2, thumb):
    list1.insert(0, 0)
    list2.insert(0, thumb)


def start_the_calculation(dict1, dict2):
    # Задаем имена пальцев
    fingers = ['Большой', 'Указательный', 'Средний', 'Безымянный', 'Мизинец']

    # Генерируем случайные значения для левой и правой руки для двух раскладок, левый б.1 = 0, правый б.2 = 0
    left_values_layout1, right_values_layout1, thumb1 = giver(dict1)
    left_values_layout2, right_values_layout2, thumb2 = giver(dict2)
    input(left_values_layout1, right_values_layout1, thumb1)
    input(right_values_layout2, left_values_layout2, thumb2)


    # Настраиваем параметры графика
    x = np.arange(len(fingers))  # Места для пальцев
    width = 0.2  # Ширина столбиков

    # Создаем гистограмму
    fig, ax = plt.subplots()

    # Столбики для первой раскладки
    # Столбики для второй раскладки
    bars1_left = ax.bar(x - width, left_values_layout1, width, color='blue', label='Раскладка 1')
    bars2_left = ax.bar(x , left_values_layout2, width, color='orange', label='Раскладка 2')
    bars1_right = ax.bar(x + width, right_values_layout1, width, color='blue')
    bars2_right = ax.bar(x + 2 * width, right_values_layout2, width, color='orange')

    # Добавляем значения над столбиками
    for bar in bars1_left + bars1_right + bars2_left + bars2_right:
        yval = bar.get_height()
        if yval != 0:
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Настраиваем оси и легенду
    ax.set_ylabel('Значения')
    ax.set_title('Гистограмма по пальцам рук')
    ax.set_xticks(x + width - 0.105)  # Сдвигаем метки по оси X
    ax.set_xticklabels(fingers)

    # Добавляем подписи для рук
    for i in range(4):
        ax.text(i + 1 - width + 0.08 , -0.7, 'Л', ha='center', va='top', fontsize=8)  # Л для левой руки
        ax.text(i + 1 + width * 1.5 + 0.009, -0.7, 'П', ha='center', va='top', fontsize=8)  # П для правой руки

    # Добавляем легенду
    ax.legend()

    # Показать гистограмму
    plt.tight_layout()
    plt.show()
