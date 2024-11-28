'''
main файл объединяющий все файлы, в качестве аргумента через командную строку получает название файла
'''

import sys
import icuken
import skoropis
import traditional_scancodes_map
import grafika
import functions

if __name__ == "__main__":
    filename = sys.argv[1]
    chars_dict = functions.characters_in_file_counter(filename)
    finger_dict1 = functions.finger_load_calculator(chars_dict, icuken, traditional_scancodes_map)
    finger_dict2 = functions.finger_load_calculator(chars_dict, skoropis, traditional_scancodes_map)
    for finger, count in finger_dict1.items():
       print(f"{finger}: {count}")
    print('\n')
    for finger, count in finger_dict2.items():
       print(f"{finger}: {count}")
    grafika.start_the_calculation(finger_dict1, finger_dict2)
