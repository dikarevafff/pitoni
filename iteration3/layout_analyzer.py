'''
main файл объединяющий все файлы, в качестве аргумента через командную строку получает название файла
'''

import sys
import data
# from main import fing_d_vyzov
# from laba1 import data_combined
import main
import laba1
from functions import *

if __name__ == "__main__":
    filenames = sys.argv[1:]
    chars_dict = characters_in_file_counter(filenames)
    icuken_fdict = fingers_load_calculator(chars_dict, data.layout_map_icuken, data)
    icuken_hdict = hands_load_calculator(icuken_fdict)
    skoropis_fdict = fingers_load_calculator(chars_dict, data.layout_map_skoropis, data)
    skoropis_hdict = hands_load_calculator(skoropis_fdict)
    create_text_file(filenames, 'summary.txt')
    vyzov_fdict = team1_to_us_translator(main.main())
    vyzov_hdict = hands_load_calculator(vyzov_fdict)
    dictor_fdict = team2_to_us_translator(laba1.main())
    dictor_hdict = hands_load_calculator(dictor_fdict)
    print('Йцукен:')
    formated_fingers_result_out(icuken_fdict)
    formated_hands_result_out(icuken_hdict)
    print('СКОРОПИС:')
    formated_fingers_result_out(skoropis_fdict)
    formated_hands_result_out(skoropis_hdict)
    print('ВЫЗОВ:')
    formated_fingers_result_out(vyzov_fdict)
    formated_hands_result_out(vyzov_hdict)
    print('ДИКТОР:')
    formated_fingers_result_out(dictor_fdict)
    formated_hands_result_out(dictor_hdict)

    visualization(icuken_fdict, skoropis_fdict, vyzov_fdict, dictor_fdict, filenames, icuken_hdict, skoropis_hdict, vyzov_hdict, dictor_hdict)