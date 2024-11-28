import keyboard

# Инициализация словаря штрафов
price = {}

# Функция для добавления множества клавиш в словарь по уровню штрафа
def add_keys_to_price(penalty_level):
    print(f"Ожидаю нажатия клавиш для штрафа уровня {penalty_level}. Нажмите Enter, чтобы завершить.")
    
    # Множество для хранения скан-кодов текущего уровня штрафа
    keys_for_penalty = set()
    
    while True:
        # Считываем событие клавиши
        event = keyboard.read_event()
        
        if event.event_type == "down":
            key_code = event.scan_code
            
            # Проверка на завершение ввода (Enter)
            if key_code == 28:  # Код Enter
                print("Завершение ввода для данного уровня штрафа.")
                break
            
            # Добавляем код в множество, избегая дубликатов
            keys_for_penalty.add(str(key_code))
            print(f"Добавлен код клавиши: {key_code}")
    
    # Сохраняем отсортированный набор скан-кодов для выбранного уровня штрафа
    price[penalty_level] = sorted(keys_for_penalty, key=int)  # Сортировка по числовому значению
    print(f"Коды клавиш для уровня штрафа {penalty_level} сохранены и отсортированы.")

# Основной цикл программы
while True:
    try:
        # Запрашиваем уровень штрафа
        penalty_level = int(input("Введите уровень штрафа (или -1 для выхода): "))
        
        if penalty_level == -1:
            break  # Выход из программы
        
        # Добавляем клавиши к выбранному уровню штрафа
        add_keys_to_price(penalty_level)
        
        # Отображаем текущий словарь
        print("Текущий словарь штрафов:", price)
        
    except ValueError:
        print("Ошибка: введите целое число для уровня штрафа.")
