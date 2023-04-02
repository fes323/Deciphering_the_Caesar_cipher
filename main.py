
print('Взлом шифра Цезаря')
print('Нажмите ENTER и введите сообщение для дешефровки')
message = input('> ')

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

for key in range(len(SYMBOLS)):
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            
            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
            
    print('Ключ: #{}: {}'.format(key, translated))