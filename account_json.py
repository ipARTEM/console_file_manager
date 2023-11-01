# import json
# import os.path
#
#
# # def start_storage():
#
# # result = json.dumps(storage)
# # print(result)
#
# # account = 0
# # storage = {'account': 0}
#
# #****************************************************************************
# storage = {
#     'account': 0,
#     'history': [
#         #     {
#         #     'purchase_number': 0,
#         #     'price': 0,
#         #     'buy_name': ''
#         # }
#     ]
# }
# account_storage = 'account.json'
# while True:
#     try:
#         # Чтение из файла
#         with open(account_storage, 'r', encoding='utf8') as f:
#             storage = json.load(f)
#             #print(storage)
#             break
#     except:
#         if os.path.exists(account_storage):
#             os.remove(account_storage)
#         # Сохранение в файл
#         with open(account_storage, 'w', encoding='utf8') as f:
#             json.dump(storage, f, ensure_ascii=False, indent=2)
#
#         input('Ошибка при работе с файлом')
#
# #****************************************************************************
#
# # return storage
#
# # start_storage()
#
#
# #storage['account'] = input('Введите значение account: ')
# purchases = []
# counter = 0
# purchase_number = 1
# buy_name = 'dsfdsf'
# price = 33
#
# # Запись только значений
# # storage['history']=[purchase_number, buy_name, price]
#
# new_data = {'purchase_number': 1, 'price': 185, 'buy_name': 'шоколадка'}
# storage['history'].append(new_data)
#
# # Сохранение в файл
# with open(account_storage, 'w', encoding='utf8') as f:
#     json.dump(storage, f, ensure_ascii=False, indent=2)
