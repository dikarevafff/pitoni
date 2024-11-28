import icuken
import skoropis
import scancodes_map

def characters_in_file_counter(filename):
    chars = {}
    
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
    for key, value in the_dict.items():
        if item in value:
            return key


def finger_load_calculator(chars_dict, imported_layout):
        final_fingers_load = {
            'lfi2': 0,
            'lfi3': 0,
            'lfi4': 0,
            'lfi5': 0,
            'rfi2': 0,
            'rfi3': 0,
            'rfi4': 0,
            'rfi5': 0,
            'thumb': 0
        }


        for char, count in chars_dict.items():
            for char_temp, scancodes_temp in imported_layout.layout_map.items():
                if char == char_temp:
                    if len(scancodes_temp) > 1:
                        scancode = scancodes_temp[1]
                        price = entry_checker(scancode, scancodes_map.key_price)
                        finger = entry_checker(scancode, scancodes_map.key_finger)
                        final_fingers_load[finger] += count*price

                    scancode = scancodes_temp[0]
                    price = entry_checker(scancode, scancodes_map.key_price)
                    finger = entry_checker(scancode, scancodes_map.key_finger)
                    final_fingers_load[finger] += count*price
        return final_fingers_load

if __name__ == "__main__":
    chars_dict = characters_in_file_counter('example.txt')
    print (chars_dict)
    finger_dict = finger_load_calculator(chars_dict, icuken)
    for finger, count in finger_dict.items():
       print(f"{finger}: {count}")
    finger_dict = finger_load_calculator(chars_dict, skoropis)
    for finger, count in finger_dict.items():
       print(f"{finger}: {count}")