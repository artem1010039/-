import csv


with open('game.txt') as file:  # Открываем файл
    rd = csv.reader(file, delimiter='$', quotechar="'")  # Читаем файл
    games = list(rd)[1:]  # Создаем список из всех строк кроме первой
    for name, charcs, error, date in games:  # Перебираем значения
        if '55' in str(error):  # Если в ошибке 55
            print(f'У персонажа\t{charcs}\tв игре\t{name}\tнашлась ошибка с кодом:\t {error}.\tДата фиксации:\t {date}')
            error = 'Done'
            date = '0000-00-00'


with open('game_new.csv', 'w') as newfile:  # Открываем новый файл
    write = csv.writer(newfile)
    write.writerow(['name', 'charcs', 'error', 'date'])
    write.writerows(games)
