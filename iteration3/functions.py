'''
подключаемый файл с функциями, необходимыми для подсчёта символов в файле, нагрузки на пальцы
'''
import matplotlib.pyplot as plt
import numpy as np

def characters_in_file_counter(filenames):
    '''
    получает: название файла
    возвращает: словарь "chars" - 'символ': количество
    '''
    
    #возвращаемый словарь: 'символ': количество
    chars = {}
    
    #заполнение словаря chars - анализ внешнего текстового
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                for char in line:
                    if char in chars:
                        chars[char] += 1
                    else:
                        chars[char] = 1
    return chars
 
def entry_checker(item, the_dict):
    '''
    получает: айтем, словарь
    возвращает: ключ, в значения которого входит айтем
    '''
    for key, value in the_dict.items():
        if item in value:
            return key


def fingers_load_calculator(chars_dict, imported_layout, data):
    '''
    получает: словарь - 'символ': количество, файл со словарём разметки раскладки, файл со словарями соответствия сканкодов - цены/пальца
    возвращает: словарь "final_fingers_load" - 'палец': нагрузка
    '''

    #возвращаемый словарь 
    final_fingers_load = {
        'lfi5': 0,
        'lfi4': 0,
        'lfi3': 0,
        'lfi2': 0,
        'lfi1': 0,
        'rfi1': 0,
        'rfi2': 0,
        'rfi3': 0,
        'rfi4': 0,
        'rfi5': 0
    }

    #блок прогона каждой клавиши, поиск соответствия символа из словаря "chars" с файлом разметки раскладки, после - сопоставление нагрузки и пальца
    for char, count in chars_dict.items():
        for key, value in imported_layout.items():
            if char == key:
                if len(value) > 1: #если согласно файла разметки раскладки символ набирается с шифтом
                    scancode = value[1]
                    price = entry_checker(scancode, data.key_price)
                    finger = entry_checker(scancode, data.key_finger)
                    if not finger:
                        continue
                    final_fingers_load[finger] += count*price

                scancode = value[0]
                price = entry_checker(scancode, data.key_price)
                finger = entry_checker(scancode, data.key_finger)
                if not finger:
                        continue
                final_fingers_load[finger] += count*price
    return final_fingers_load


def hands_load_calculator(the_dict):
    lcounter = 0
    rcounter = 0
    final_hands_load = {}
    for key, value in the_dict.items():
        if 'l' in key:
            lcounter += value
        if 'r' in key:
            rcounter += value

    final_hands_load['lh'] = round(lcounter/(lcounter+rcounter)*100)
    final_hands_load['rh'] = round(rcounter/(lcounter+rcounter)*100)

    return final_hands_load


def formated_fingers_result_out(the_dict):
    for finger, count in the_dict.items():
       print(f"{finger}: {count}")
    print('\n')

def formated_hands_result_out(the_dict):
    for finger, count in the_dict.items():
       print(f"{finger}: {count}%")
    print('\n')



def team1_to_us_translator(vyzov_dict):
    translated = {
      'lfi5': 0,
      'lfi4': 0,
      'lfi3': 0,
      'lfi2': 0,
      'lfi1': 0,
      'rfi1': 0,
      'rfi2': 0,
      'rfi3': 0,
      'rfi4': 0,
      'rfi5': 0
      }

    for key, value in vyzov_dict.items():   
        match key:
            case 'левый мизинец':
                translated['lfi5'] = value
            case 'левый безымянный':
                translated['lfi4'] = value
            case 'левый средний':
                translated['lfi3'] = value
            case 'левый указательный':
                translated['lfi2'] = value
            case 'левый большой':
                translated['lfi1'] = value
            case 'правый большой':
                translated['rfi1'] = value
            case 'правый указательный':
                translated['rfi2'] = value
            case 'правый средний':
                translated['rfi3'] = value
            case 'правый безымянный':
                translated['rfi4'] = value
            case 'правый мизинец':
                translated['rfi5'] = value
    return translated

def team2_to_us_translator(skoropis_dict):
    translated = {
      'lfi5': 0,
      'lfi4': 0,
      'lfi3': 0,
      'lfi2': 0,
      'lfi1': 0,
      'rfi1': 0,
      'rfi2': 0,
      'rfi3': 0,
      'rfi4': 0,
      'rfi5': 0
      }

    for key, value in skoropis_dict.items():   
        match key:
            case 'lfi5':
                translated['lfi5'] = value
            case 'lfi4':
                translated['lfi4'] = value
            case 'lfi3':
                translated['lfi3'] = value
            case 'lfi2':
                translated['lfi2'] = value
            case 'lfi1':
                translated['lfi1'] = value
            case 'rfi1':
                translated['rfi1'] = value
            case 'rfi2':
                translated['rfi2'] = value
            case 'rfi3':
                translated['rfi3'] = value
            case 'rfi4':
                translated['rfi4'] = value
            case 'rfi5':
                translated['rfi5'] = value
    return translated


# Функция визуализации
def visualization(layout1, layout2, layout3, layout4, files, hh1, hh2, hh3, hh4):

    layout1 = list(layout1.values())
    layout2 = list(layout2.values())
    layout3 = list(layout3.values())
    layout4 = list(layout4.values())

    hh1 = list(hh1.values())
    hh2 = list(hh2.values())
    hh3 = list(hh3.values())
    hh4 = list(hh4.values())

    # Создаем фигуру с основным графиком и 4 круговыми диаграммами
    fig = plt.figure(figsize=(15, 7))
    grid = fig.add_gridspec(2, 4, height_ratios=[2, 1])

    # Горизонтальная гистограмма
    ax1 = fig.add_subplot(grid[0, :])
    fingers = ['П Мизинец', 'П Безымянный', 'П Средний',
               'П Указательный', 'П Большой',
               'Л Большой', 'Л Указательный',
               'Л Средний', 'Л Безымянный', 'Л Мизинец']
    index = np.arange(len(fingers))
    bar_width = 0.2

    for i in range(len(fingers)):
        ax1.barh(index[9-i] + bar_width * 1.5, layout1[i], bar_width, label='ЙЦУКЕН' if i == 0 else "", color=['#ff3333'], alpha=1.0)
        ax1.barh(index[9-i] + bar_width * 0.5, layout2[i], bar_width, label='Скоропис' if i == 0 else "", color=['#99ff33'], alpha=1.0)
        ax1.barh(index[9-i] - bar_width * 0.5, layout3[i], bar_width, label='Вызов' if i == 0 else "", color=['#0077ff'], alpha=1.0)
        ax1.barh(index[9-i] - bar_width * 1.5, layout4[i], bar_width, label='Диктор' if i == 0 else "", color=['#b60aff'], alpha=1.0)

    ax1.set_xlabel('Количество нажатий')
    ax1.set_title(", ".join(files))
    ax1.set_yticks(index)
    ax1.set_yticklabels(fingers)
    ax1.legend()

    # Круговые диаграммы
    labels = ['Левая рука', 'Правая рука']
    axs = [fig.add_subplot(grid[1, i]) for i in range(4)]

    hh_values = [hh1, hh2, hh3, hh4]
    hh_titles = ['ЙЦУКЕН', 'Скоропис', 'Вызов', 'Диктор']
    pie_colors = ['#30d5c8', '#ff0033']

    for i, ax in enumerate(axs):
        ax.pie(hh_values[i], labels=labels, autopct='%1.1f%%', startangle=90, colors=pie_colors)
        ax.set_title(hh_titles[i], fontdict={'fontweight': 'bold', 'fontsize': 12})

    # Настройки и отображение
    fig.canvas.manager.set_window_title('Сбор статистики для оптимизации русских раскладок для слепопечатников')
    plt.tight_layout()
    plt.show()


def create_text_file(filenames, summarized_file):
    #создаёт текстовый файл из содержимого переданных файлов
    with open(summarized_file, 'w', encoding='utf-8') as file:
        for file_name in filenames:
            with open(file_name, 'r', encoding='utf-8') as in_file:
                file.write(in_file.read())