# -*- coding: utf-8 -*-
from os import getcwd
import json
from functions_for_erb_V02 import *

gcwd = getcwd()

with open(gcwd+'/set.json', 'r') as sets:
    settings = json.load(sets)

with open(gcwd+'/resources/languages/%s.txt'%settings['language'], 'r') as language:
    lng = language.readlines()

print(''.join(lng[:5]).encode('cp1251').decode('utf-8'), end='')
enter = input("Введите номер команды и нажмите клавишу 'Enter':")
while True:
    if enter == "1":
        print(''.join(lng[5:7]).encode('cp1251').decode('utf-8'))
        users = read_or_write("users.json", "read")
        inpt_data = [int(users[list(users.keys())[-1]]['id'])] # хранение данных о новом пользователе
        for s in lng[7:13]: # перебираем текст приветствия
            inpt_data.append(input(s.replace('\n', '').encode('cp1251').decode('utf-8')))
        read_or_write('users.json', 'write', add_contact(inpt_data))
            
    elif enter ==  "2":
        pass
    elif enter ==  "3":
        pass
    elif enter ==  "4":
        break
    
