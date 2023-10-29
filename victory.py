import random

famous_people = {
    'Бернар Арно': '05.03.1949',
    'Джефф Безос': '12.01.1964',
    'Ларри Эллисон': '17.08.1944',
    'Майкл Блумберг': '14.02.1942',
    'Билл Гейтс': '28.10.1955',
    'Уоррен Баффетт': '30.08.1930',
    'Илон Маск': '28.06.1971',
    'Марк Цукерберг': '14.05.1984',
    'Павел Дуров': '10.10.1984',
    'Стив Джобс': '24.02.1955'
}


def finish_text(text):
    text_str = text.split('.')
    text_list = list(text_str)
    return text_list



answer = ''

# print(type(famous_people))
months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
days = {
    '01': 'первого',
    '02': 'второго',
    '03': 'третьего',
    '04': 'четвертого',
    '05': 'пятого',
    '06': 'шестого',
    '07': 'седьмого',
    '08': 'восьмого',
    '09': 'девятого',
    '10': 'десятого',
    '11': 'одиннадцатого',
    '12': 'двенадцатого',
    '13': 'тренадцатого',
    '14': 'четырнадцатого',
    '15': 'пятнадцатого',
    '16': 'шестнадцатого',
    '17': 'семнадцатого',
    '18': 'восемнадцатого',
    '19': 'девятнадцатого',
    '20': 'двадцатого',
    '21': 'двадцать первого',
    '22': 'двадцать второго',
    '23': 'двадцать третьего',
    '24': 'двадцать четвертого',
    '25': 'двадцать пятого',
    '26': 'двадцать шестого',
    '27': 'двадцать седьмого',
    '28': 'двадцать восьмого',
    '29': 'двадцать девятого',
    '30': 'тридцатого',
    '31': 'тридцать первого',
}


def victory_game():
    counter = 0
    while True:

        print('Давайте поиграем в викторину, вам надо угадать день рождения известных людей!')

        # for key in famous_people.keys():
        # print(key)
        # print(famous_people[key])

        # numbers = ['sdf', 'dsf', 'wer']

        fp_list = []

        for human in famous_people:
            fp_list.append(human)
            # print(human)
        result = random.sample(fp_list, 5)

        # print(type(result))

        random_5 = {}

        for i in range(5):
            # print(i)
            # print(result[i])
            random_5[result[i]] = input(f'Напишите дату рождения (в формате "dd.mm.yyyy") {result[i]}: ')
        print(result)

        print(random_5.items())
        print('')
        print('Известный человек   ---   Ваш ответ   ---   Правильный ответ   ---   Результат   ')
        for key in random_5.keys():
            str_translation = finish_text(famous_people[key])
            if random_5[key] == famous_people[key]:
                answer = '"+"'
                counter += 1
            else:
                answer = '"-"'

            # print(f'{key} --- {random_5[key]} --- {famous_people[key]}')
            print(
                f'{key}   ---   {random_5[key]}   ---   {days[str_translation[0]]} {months[str_translation[1]]} {str_translation[2]}   ---   {answer}')
            # print(str_translation)
            # print(f'{days[str_translation[0]]} {months[str_translation[1]]} {str_translation[2]}')
        print('')
        print(f'Количество правильных ответов: {counter}')

        # result[answer] = input(f'Напишите дану рождения (в формате "dd.mm.yyyy") {answer}: ')

        game = input('Если хотите начать заново нажмите на кнопку "1": ')

        if game != '1':
            break


#victory_game()
