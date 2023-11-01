"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
import os.path
import account_json


def separator():
    sep = '---------------------------'
    # print('-'*27)
    return sep


def bank_account():
    #storage = account_json.start_storage()

    storage = {
        'account': 0,
        'history': [
            #     {
            #     'purchase_number': 0,
            #     'price': 0,
            #     'buy_name': ''
            # }
        ]
    }
    account_storage = 'account.json'
    while True:
        try:
            # Чтение из файла
            with open(account_storage, 'r', encoding='utf8') as f:
                storage = json.load(f)
                #print(storage)
                break
        except:
            if os.path.exists(account_storage):
                os.remove(account_storage)
            # Сохранение в файл
            with open(account_storage, 'a', encoding='utf8') as f:
                json.dump(storage, f, ensure_ascii=False, indent=2)

            input('Ошибка при работе с файлом')

    account = int(storage['account'])
    addition = 0
    price = 0

    purchases = []
    purchase_number = 0

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        '''1. пополнение счета
    при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
    после того как пользователь вводит сумму она добавляется к счету
    снова попадаем в основное меню'''
        if choice == '1':
            print(f'У вас на счету {account}₽')

            while True:
                try:
                    account += int(input(f'На какую сумму хотите пополнить счет: '))
                    print(f'Теперь у Вас на счету: {account}₽')
                    break
                except:
                    print('Вы ввели не корректную сумму!')

            '''2. покупка
    при выборе этого пункта пользователю предлагается ввести сумму покупки
    если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
    если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
    снимаем деньги со счета
    сохраняем покупку в историю
    выходим в основное меню '''
        elif choice == '2':
            while True:
                print(f'У вас на счету {account}₽')
                try:

                    price = int(input(f'Введите сумму покупки: '))
                    if account >= price > 0:

                        purchase_number += 1
                        buy_name = input(f'Введите название покупки: ')
                        print(f'Вы купили: "{buy_name}" на сумму: "{price}₽"')
                        account -= price
                        purchases.append(purchase_number, buy_name, price)
                        # print(purchases)
                        new_data = {'purchase_number': 1, 'price': 185, 'buy_name': 'шоколадка'}
                        storage['history'].append(new_data)

                        print(f'Теперь у Вас на счету: {account}₽')

                    elif price > account:
                        print('У Вас не достаточно средств на счету!')

                    else:
                        print('Вы ввели не корректную сумму!')

                    break

                except:
                    print('Вы ввели не корректную сумму!')

            '''3. история покупок
    выводим историю покупок пользователя (название и сумму)
    возвращаемся в основное меню'''
        elif choice == '3':
            print()
            print(separator())
            print(' №    Название    Цена')
            for i in purchases:
                print(f' {i[0]}  {i[1]}  {i[2]}₽')
            print(separator())
            print()

            '''4. выход
    выход из программы'''
        elif choice == '4':

            storage['account'] = account
            # Сохранение в файл
            with open(account_storage, 'a', encoding='utf8') as f:
                json.dump(storage, f, ensure_ascii=False, indent=2)

            break
        else:
            print('Неверный пункт меню')
