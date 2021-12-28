# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_1 = input('пиши первую букву: ')
letter_2 = input('пиши букву вторую: ')
print(f'\nномер буквы {letter_1}: {alphabet.find(letter_1)+1}\nномер буквы {letter_2}: {alphabet.find(letter_2)+1}\n'
      f'а между ними букв {len(alphabet[alphabet.find(letter_1):alphabet.find(letter_2)])-1} шт.')
