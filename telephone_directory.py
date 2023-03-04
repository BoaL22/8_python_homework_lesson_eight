
    # Обязательное ДЗ - 
    # Доделать решение задачи: Задача: 
    # Создать телефонный справочник с внешним хранилищем информации, 
    # доделать функционал полноценной работы с записями - удаление , добавление, редактирование.
    # Необязательное ДЗ № 1 на выбор - сделать телефонный справочник с графическим интерфейсом 
    # (EASYGUI, Tkinter, PyQT) и возможно с использование БД SQLite3.
    # Необязательное ДЗ № 2 на выбор - сделать телефонный справочник 
    # в формате ТГ-бота и возможно с использование БД SQLite3.

import json

telephone_man = {'id': '', 'name': '', 'first_name': '', 'number': ''}
file = 'telephone_directory.json'

with open(file) as file_load:
   g_list = json.load(file_load)
telephone_directory = g_list




def save():
   with open(file, 'w') as file_save:
      file_save.write(f"{json.dumps(telephone_directory)}\n")

def see_contact():
   with open(file) as file_print:
      lst = json.load(file_print)

      command_see = input('Вывести \n\tвесь справочник - all\n\tотдельный контакт - one\n')
      if command_see == 'all':
         if len(lst) == 0:
            print('Справочник пуст! ')
         else:
            for man in lst:
               print(f"{man['id']} {man['name'].title()} {man['first_name'].title()} - {man['number']}")

      elif command_see == 'one':
         glob_search()

      else: 
         print('Введите команду правильно!\n')
         see_contact()

def add_contact():
   telephone_man['id'] = str(len(telephone_directory))
   telephone_man['name'] = input('Введите имя: ').lower()
   telephone_man['first_name'] = input('Введите фамилию: ').lower()
   telephone_man['number'] = input('Введите номер: ').lower()
   telephone_directory.append(telephone_man)
   save()
   print('Контакт добавлен в справочник! ')

def search(comand_search, element, key):
   comand_search = input(f'Введите {element}: ').lower()
   for man in telephone_directory:
      if comand_search in man[key]:
         print(f"{man['id']} {man['name'].title()} {man['first_name'].title()} - {man['number']}\n")
         return man['id']
   print(f'В справочнике нет такого {comand_search}! \nПопробуйте ввести заново')
   search(comand_search, element, key)

def glob_search():
   comand_search = input('Искать будем по\n\tid - id\n\tИмени - name\n\tФамилии - first\n\tНомеру - number\n').lower()

   if comand_search == 'id':
      id = search(comand_search, 'id', 'id')
      return id
   elif comand_search == 'name':
      id = search(comand_search, 'имя', 'name')
      return id
   elif comand_search == 'first':
      id = search(comand_search, 'фамилию', 'first_name')
      return id
   elif comand_search == 'number':
      id = search(comand_search, 'номер', 'number')
      return id
   else: 
      print('Введите команду правильно! ')
      glob_search()

def edit_contact():
   id = glob_search()
   id = int(id)
   command_edit = input('Изменять будем \n\tИмя - name\n\tФамилию - first\n\tНомер - number\n').lower()
   if command_edit == 'name':
      telephone_directory[id]['name'] = input('Введите новое имя: ')
      print('Имя изменено! ')

   elif command_edit == 'first':
      telephone_directory[id]['first'] = input('Введите новую фамилию: ')
      print('Фамилия изменена! ')

   elif command_edit == 'number':
      telephone_directory[id]['number'] = input('Введите новый номер: ')
      print('Номер изменён! ')
   else:
      print('Введите команду правильно! ')
      edit_contact()
   save()

def delete_contact():
   id = glob_search()
   id = int(id)
   command_del = input(f"Удалить контакт {telephone_directory[id]['name']}? \n\tyes / no\n")
   if command_del == 'yes':
      telephone_directory.pop(id)
      print(f'Контакт был удалён! ')
      save()
   elif command_del == 'no':
      return
   else:
      print('Такого id не существует! Попробуйте заново:')
      delete_contact()



while True:
   command = input('\n\nЧто будем делать? Введите команду:\n\tПросмотреть телефонный справочник - see\n\tДобавить пользователя - add\n\tРедактировать контакт - edit\n\tУдалить пользователя - del\n\tЗакончить работу - q\n')
   if command == 'see':
      see_contact()

   elif command == 'add':
      add_contact()

   elif command == 'edit':
      edit_contact()

   elif command == 'del':
      delete_contact()

   elif command == 'q':
      break

   else:
      print('Введите команду правильно! \n') 

