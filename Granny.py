import random
total = 0
print('ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!')

while True:
    year = random.randint(1930,1950)
    say = input()
    if total == 2:
        print('ДО СВИДАНИЯ, МИЛЫЙ!')
        break
    elif say == 'ПОКА!':
        print(f'НЕТ, НИ РАЗУ С {year} ГОДА!.')
        total += 1
    elif say.isupper() == True:
        print(f'НЕТ, НИ РАЗУ С {year} ГОДА!.')
    else:
        print('АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!')