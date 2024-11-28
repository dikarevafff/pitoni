"""
Файл со всеми функциями, требующимися при расчете нагрузки на пальцы
"""
import dict_finger
import matplotlib.pyplot as plt
import numpy as np
from dict_finger import *


def find_finger(character, keyboard_layout):
  """
      Определяет, какой палец используется
      для набора данного символа на клавиатуре.
  """
  flag = 0
  for finger_name, characters in keyboard_layout.items():
    if character in characters:
      return finger_name, flag
    else:
      if keyboard_layout == keyboard_finger_vyzov:
        for finger_name, characters \
                in keyboard_finger_vyzov_dop.items():
          if character in characters:
            flag = 1
            return finger_name, flag
      else:
        if keyboard_layout == keyboard_finger_qwerty:
          for finger_name, characters \
                  in keyboard_finger_qwerty_dop.items():
            if character in characters:
              flag = 1
              return finger_name, flag
        else:
          if keyboard_layout == keyboard_finger_dictor:
            for finger_name, characters \
                    in keyboard_finger_dictor_dop.items():
              if character in characters:
                flag = 1
                return finger_name, flag
          else:
            if keyboard_layout == keyboard_finger_scoropis:
              for finger_name, characters \
                      in keyboard_finger_scoropis_dop.items():
                if character in characters:
                  flag = 1
                  return finger_name, flag
  else:
    return "Invalid character: {}".format(character), flag

def count_finger_load_qwerty(text):
  """
      Подсчитывает нагрузку на пальцы, использованные при наборе текста
      на клавиатурной раскладке QWERTY.
  """
  for character in text:
      finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_qwerty)
      if finger_name in dict_finger.qwerty_finger_count:
          dict_finger.qwerty_finger_count[finger_name] += 1
          if character.isupper() or flag_nado == 1:
              shift_finger = 'lfi5'
              dict_finger.qwerty_finger_count[shift_finger] += 1

  layout_1 = list(qwerty_finger_count.values())
  return layout_1

def count_finger_load_vyzov(text):
  """
      Подсчитывает нагрузку на пальцы, использованные при наборе текста
      в раскладке "Вызов".
  """
  for character in text:
    finger_name, flag_nado = \
      find_finger(character.lower(), keyboard_finger_vyzov)
    alt_finger = 'rfi1'
    if finger_name in dict_finger.vyzov_finger_count:
      dict_finger.vyzov_finger_count[finger_name] += 1
      if character.isupper() or flag_nado == 1:
        shift_finger = 'lfi5'
        dict_finger.vyzov_finger_count[shift_finger] += 1
    if character == '№':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'ц':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'щ':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'ъ':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'ю':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'э':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'Ц':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'Щ':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'Ю':
      dict_finger.vyzov_finger_count[alt_finger] += 1
    if character == 'Э':
      dict_finger.vyzov_finger_count[alt_finger] += 1

  layout_2 = list(vyzov_finger_count.values())
  return layout_2

def count_finger_load_dictor(text):
  """
      Подсчитывает нагрузку на пальцы, использованные при наборе текста
      на клавиатурной раскладке DICTOR.
  """
  for character in text:
      finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_dictor)
      if finger_name in dict_finger.dictor_finger_count:
          dict_finger.dictor_finger_count[finger_name] += 1
          if character.isupper() or flag_nado == 1:
              shift_finger = 'lfi5'
              dict_finger.dictor_finger_count[shift_finger] += 1

  layout_3 = list(dictor_finger_count.values())
  return layout_3

def count_finger_load_scoropis(text):
  """
      Подсчитывает нагрузку на пальцы, использованные при наборе текста
      на клавиатурной раскладке SCOROPIS.
  """
  for character in text:
      finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_scoropis)
      if finger_name in dict_finger.scoropis_finger_count:
          dict_finger.scoropis_finger_count[finger_name] += 1
          if character.isupper() or flag_nado == 1:
              shift_finger = 'lfi5'
              dict_finger.scoropis_finger_count[shift_finger] += 1

  layout_4 = list(scoropis_finger_count.values())
  return layout_4

def vyvod_gistogramma(layout1, layout2, layout3, layout4):
    fingers = ['Мизинец (левая)', 'Безымянный (левая)', 'Средний (левая)', 'Указательный (левая)', 'Большой (левая)',
                'Большой (правая)', 'Указательный (правая)', 'Средний (правая)', 'Безымянный (правая)', 'Мизинец (правая)']
    color1 = ['#ff0033']
    color2 = ['#0000ff']
    color3 = ['#009900']
    color4 = ['#ffcc00']
    index = np.arange(len(fingers))
    bar_width = 0.2
    for i in range(len(fingers)):
            plt.barh(index[i] - bar_width * 1.5, layout1[i], bar_width, label='Йцукен' if i == 0 else "", color=color1 ,
                alpha=1.0)
            plt.barh(index[i] - bar_width * 0.5, layout2[i], bar_width, label='Вызов' if i == 0 else "", color=color2,
                alpha=1.0)
            plt.barh(index[i] + bar_width * 0.5, layout3[i], bar_width, label='Диктор' if i == 0 else "", color=color3,
                      alpha=1.0)
            plt.barh(index[i] + bar_width * 1.5, layout4[i], bar_width, label='Скоропись' if i == 0 else "", color=color4,
                      alpha=1.0)
    plt.ylabel('Пальцы')
    plt.xlabel('Количество нажатий')
    plt.yticks(index , fingers)
    plt.show()

def load_hand_left(list):
  """
        Вычисляет процент нагрузки
        на левую руку на основе значений из переданного списка.
      """
  start_index = 0
  end_index = 5
  start_index_1 = 0
  end_index_1 = 9
  partial_sum = sum(list[start_index:end_index])
  general_sum = sum(list[start_index_1:end_index_1])
  procent = int((partial_sum * 100) / general_sum)
  return procent

def load_hand_right(list):
  """
     Вычисляет процент нагрузки
     на правую руку на основе значений из переданного списка.
     """
  start_index = 5
  end_index = 9
  start_index_1 = 0
  end_index_1 = 9
  partial_sum = sum(list[start_index:end_index])
  general_sum = sum(list[start_index_1:end_index_1])
  procent = int((partial_sum * 100) / general_sum)
  return procent

def clicks(layout_1, layout_2, layout_3, layout_4):
  fing = ['левый мизинец', 'левый безымянный', 'левый средний', 'левый указательный', 'левый большой',
            'правый большой', 'правый указательный', 'правый средний', 'правый безымянный', 'правый мизинец']
  fing_d_qwerty = dict(zip(fing,layout_1))
  fing_d_vyzov = dict(zip(fing, layout_2))
  fing_d_dictor = dict(zip(fing, layout_3))
  fing_d_scoropis = dict(zip(fing, layout_4))
  return fing_d_qwerty, fing_d_vyzov, fing_d_dictor, fing_d_scoropis