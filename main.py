import json
import os
import shutil
import platform
import psutil
import victory
import my_bank_account


def menu():
    while True:
        print('Выберите нужный пункт меню и нажмете цифру:')
        print('1.  Создать (файл/папку)')
        print('2.  Удалить (файл/папку)')
        print('3.  Копировать (файл/папку)')
        print('4.  Просмотреть содержимое рабочей директории')
        print('5.  Посмотреть только папки')
        print('6.  Посмотреть только файлы')
        print('7.  Просмотреть информацию об операционной системе')
        print('8.  Вывод информации о создателе программы')
        print('9.  Запуск игры викторина')
        print('10. Мой банковский счет')
        print('11. Смена рабочей директории')
        print('12. Сохранить содержимое рабочей директории в файл')
        print('13. Выход')

        number = input('Номер цифры: ')
        # Создать (файл/папку)
        if number == '1':

            while True:
                number_inner = input('Введите "1"если папку и "2" если файл: ')
                if number_inner == '1':
                    name_dir = input('Введите название папки: ')
                    if not os.path.exists(name_dir):
                        os.mkdir(name_dir)
                        break
                elif number_inner == '2':
                    name_file = input(r'Введите название файла: ')
                    if not os.path.exists(name_file):
                        new_file = open(name_file, 'w')
                        new_file.close()
                        break

        # Удалить (файл/папку)
        elif number == '2':
            while True:
                number_inner = input('Введите "1"если хотите удалить папку и "2" если хотите удалить файл: ')
                if number_inner == '1':
                    name_dir = input('Введите название папки: ')
                    if os.path.exists(name_dir):
                        os.rmdir(name_dir)
                        break

                elif number_inner == '2':
                    name_file = input(r'Введите название файла: ')
                    if os.path.exists(name_file):
                        os.remove(name_file)
                        break


        # Копировать (файл/папку)
        elif number == '3':
            while True:
                number_inner = input('Введите "1"если хотите копировать папку и "2" если хотите удалить файл: ')
                if number_inner == '1':
                    name_dir = input('Введите название папки для копирования: ')
                    new_name_dir = input('Введите названия новой папки: ')
                    if os.path.exists(name_dir):
                        shutil.copytree(name_dir, new_name_dir)
                        break

                elif number_inner == '2':
                    name_file = input(r'Введите название файла, который надо копирования: ')
                    new_name_file = input(r'Введите название нового файла для создания копии')
                    if os.path.exists(name_file):
                        shutil.copy(name_file, new_name_file)
                        break

        # Просмотреть содержимое рабочей директории
        elif number == '4':
            dir_list = os.listdir()
            print(dir_list)
            input()


        # Посмотреть только папки
        elif number == '5':
            dir = [f for f in os.listdir() if os.path.isdir(f)]
            for d in dir:
                print(d)
            input()


        # Посмотреть только файлы
        elif number == '6':
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                print(f)
            input()



        # Просмотреть информацию об операционной системе
        elif number == '7':
            my_system = platform.uname()

            print(f"System: {my_system.system}")
            print(f"Node Name: {my_system.node}")
            print(f"Release: {my_system.release}")
            print(f"Version: {my_system.version}")
            print(f"Machine: {my_system.machine}")
            print(f"Processor: {my_system.processor}")
            print(f"Memory :{psutil.virtual_memory()}")
            print()
            print()
            # traverse the info
            # Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
            # new = []
            #
            # # arrange the string into clear info
            # for item in Id:
            #     new.append(str(item.split("\r")[:-1]))
            # for i in new:
            #     print(i[2:-2])

            input()


        # Вывод информации о создателе программы
        elif number == '8':
            print('Программу создал Артем Химин')
            input()

        # Запуск игры викторина
        elif number == '9':
            victory.victory_game()
            input()

        # Мой банковский счет
        elif number == '10':
            my_bank_account.bank_account()
            input()

        # Смена рабочей директории
        elif number == '11':
            print('Установите новую рабочую директорию')
            print('ПРИМЕР: D:\\Python\\console_file_manager')
            print(os.getcwd())
            path = os.chdir(input())
            print(os.getcwd())
            dir_list = os.listdir()
            print(dir_list)
            input()

        # Сохранить содержимое рабочей директории в файл
        elif number == '12':
            print('Сохранить содержимое рабочей директории в файл: ')
            dir_list = os.listdir()
            print(dir_list)

            name_file = 'listdir.txt'
            data={'files':{},'dirs':{}}

            print('********* files *********')
            data['files'] = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in data['files']:
                print(f)

            print('********* dirs *********')
            data['dirs'] = [f for f in os.listdir() if os.path.isdir(f)]
            for d in data['dirs']:
                print(d)

            # Сохранить в файл
            with open(name_file, 'w', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            input()




        # Выход
        elif number == '13':
            break

        else:
            print('Введено неверное значение')
            print()


print('Добро пожаловать в Консольный менеджер')

menu()
