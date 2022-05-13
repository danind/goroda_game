def massiv(a) -> set:
    '''The function takes as input the variable into which the file is read. Returns a set of cities.'''
    vse_goroda = a.read().split(', ')
    vse_goroda = set(vse_goroda)
    for i in vse_goroda:
        i = i.replace('ё', 'е')
    return vse_goroda


def input_by_user(city_name) -> str:
    '''The function takes as input a variable with the name of the city entered by the user. Returns the name of the city in the correct format (with a capital letter, without extra spaces).Also handles cases of recognition of defeat by the user'''
    city = city_name.lower().strip().replace("ё", "е")
    if city == 'я проиграл' or city == 'я проиграла':
        return city
    city = city.title().replace('-На-', '-на-')
    return city


def fair_play(city, mn) -> bool:
    '''The function checks whether there is a city entered by the user in the set. If there is, removes it from the set. Returns True or False.'''
    if city not in mn:
        print("Выбери другой город (ты повторяешься, либо такого города нет в базе данных)!")
        return False
    else:
        mn.discard(city)
        return True


def fair_play_2(city, bukv) -> bool:
    '''The function checks whether the user entered the city with the correct letter. Returns True or False.'''
    bukv = chr(ord(bukv) -32)
    if city[0] == bukv:
        return True
    else:
        print('Введи город на правильную букву', '(' + bukv +')')
        return False


def last_char(city) -> str:
    '''The function returns the last letter in the name of the city.'''
    for l in city[-1::-1]:
        if l != 'ъ' and l != 'ы' and l != 'й' and l != 'ь':
            return l


def podbor(last_ch, spis_gor) -> str:
    '''The function displays a city from the set that meets the rules. If there is no such, informs the user that he has won. Returns the last letter of its city or -1 (in case of defeat).'''
    last_ch = chr(ord(last_ch) - 32)
    d = 0
    for i in spis_gor:
        if i[0] == last_ch:
            d = i
            break
    if d != 0:
        j = last_char(d)
        print(d + '. Тебе на букву ' + j + '.')
        spis_gor.discard(d)
        return j
    else:
        print('Ты победил!')
        return '-1'


f = open('towns.txt', 'r', encoding = 'utf-8')
spisok_gorodov = massiv(f)
f.close()
bukva = 0
while bukva != '-1':
    if bukva == 0:
        print('Введи название любого города РФ')
        print('Если захочешь сдаться, напиши: я проиграл(а)')
    user_town = input_by_user(input())
    while not(user_town == 'я проиграла') and not(user_town == 'я проиграл') and not(fair_play(user_town, spisok_gorodov)):
        user_town = input_by_user(input())
        if bukva != 0:
            while not(user_town == 'я проиграла') and not(user_town == 'я проиграл') and not(fair_play_2(user_town, bukva)):
                user_town = input_by_user(input())
    if user_town == 'я проиграл' or user_town == 'я проиграла':
        print('Ты жалок...')
        break
    char_progr = last_char(user_town)
    bukva = podbor(char_progr, spisok_gorodov)





