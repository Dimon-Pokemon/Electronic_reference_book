from os import getcwd
direc = getcwd()
direc_users = direc + '/Пользователи1_0.txt'

with open(direc_users, 'a') as file:#Данная инструкция нужна для того, чтобы создать файл, если он не был создан.
    pass

def clean():
    with open(direc_users) as file:
        list_direc_user = file.readlines()
        for i in list_direc_user:
            list_direc_user[list_direc_user.index(i)] = i.split('|')
            try:
                list_direc_user.remove('\n')
            except ValueError:
                pass
        for i in list_direc_user:
            try:
                i.remove('\n')
            except ValueError:
                pass
    return list_direc_user


def creats() -> None:
    """В небольшом блоке кода внизу мы получаем сведенья о индентификационном номере последнего контакта. Где в list_nomer_1 считывается весь файл, а в list_nomer запис
    сывается все то, что есть в list_nomer_1, но только в виде чисел, т.е. типа int"""
    with open(direc_users) as file:
        list_users_2 = file.readlines()
        for i in list_users_2:
            if i == ('\n'):
                list_users_2.remove('\n')
        nomer = len(list_users_2)
    nomer = nomer + 1
    nomer = str(nomer)
    name = input('Введите имя контакта:')#name - имя
    if name == (''):
        name = 'Не указано'
    l_name = input('Введите фамилию контакта:')#l_name - last name - фамилия
    if l_name == (''):
        l_name = 'Не указано'
    name_f = input('Введите отчество контакта:')#name_f - name father - имя отца, т.е. отчество
    if name_f == (''):
        name_f = 'Не указано'
    t_name = input('Введите псевдоним контакта:')#t_name - two name - второе имя, т.е. псевдоним
    if t_name == (''):
        t_name = 'Не указано'
    phone = input('Введите номер телефона:')#номер телефона
    if phone == (''):
        phone = 'Не указано'
    age = input('Введите возраст контакта:')#age - возраст
    if age == (''):
        age = 'Не указано'
    dr = input('Введите дату рождения контакта в формате день/месяц/год:')#dr:d - день, r - рождения т.е. день рождения
    if dr == (''):
        dr = 'Не указано'
    email = input('Введите электронную почту контакта:')#электронная почта
    if email == (''):
        email = 'Не указано'
    user = '|'.join([nomer, name, l_name, name_f, t_name, phone, age, dr, email])
    """В блоке кода ниже происходит вот что: сначала открывается файл с пользователями
    , затем туда, в конец файла, записывается контакт в виде длинной строки:'идентификационный номер|имя пользователя|фамилия|отчество|псевдоним|номер телефона|возраст|дата рождения|электронная почта'
    Далее сразу записыается символ перевода на новую строку. Так как в аргументе 'print' указано, что end = '', то это значит, что переноса на новую строку не было. Поэтому символ перевода на новую строку
    записывается не на следующей строке, а на этой же строке, где расположена информация о контакте. Это было создано, чтобы легче удалять символ перевода строки, так как при поиске нужного  контакта, в список пользователй также добывляется к последнему элементу списка
    символ перевода строки, а блягодаря такому подходу, который показан ниже, символ перевода строки записывается как отдельный элемент и он легко удаляется с помощью функции 'remove'.
    Далее открывается файл, в котором содержатся только номера уникальные номера контактов. Они нужны, чтобы пользователь мог самостоятельно выбирать конкретный номер. В этом файле содержатся только номера,
    поскольку при создании нового контакта нужна знать последний номер созданного контакта, а так как они записываются в порядке возрастания, то последний номер - максимальный нмоер. Поэтому для получения этого номера достаточно использовть
    функию 'max', а прибавив еденицу, получить новый номер нового контакта."""
    with open(direc_users, 'a') as file:
        print(user, file = file, end = '')#Запись информации о новом контакте
        print('|', file = file, end = '')
        print('\n', file = file, end='')#Символ переноса строки, чтобы следующий номер записывался на следю строки, т.е. чтобы все номер были на разных строчках
    print('Контакт успешно создан! Вы будете возвращены в главное меню.')


def search(direc_users:'Пользователи1_0.txt', s_word:'Что/кого надо найти'='', kods:int=0) -> None:
    list_direc_user = clean()
    def printss(attribut:str, attribut_str:str) -> None:
        print(attribut_str, attribut)
    kod = 1
    attributs = ['Идентификационный номер:', 'Имя:', 'Фамилия:', 'Отчество:', 'Псевдоним:', 'Номер телефона:', 'Возраст:', 'Дата рождения:', 'Электронная почта:']
    if kods == 0:
        for user in list_direc_user:
            for user_atribute in user:
                if user_atribute == s_word:
                    attribut_ind = 0
                    for attribut in user:
#                        print('kuku')
                        printss(attribut = attribut, attribut_str = attributs[attribut_ind])
                        attribut_ind += 1
                    kod = 0
                    break
    else:
        for user in list_direc_user:
            attribut_ind = 0
            for attribit in user:
                printss(attribut = attribit, attribut_str = attributs[attribut_ind])
                attribut_ind += 1
                
        
    if kod == 1 and kods == 0:
        answer = input("Контакт не найден.Хотите создать?(Введите '1' - 'Да' или '2' - 'Нет')")
        if answer == ('1'):
            creats()

at = ['имя', 'фамилия', 'отчество', 'псевдоним', 'номер телефона', 'возраст', 'дата рождения', 'электронная почта']

print('Добро пожаловать! Это электронный справочник!Текущая версия:1.1.Список доступных команд:\n1.Создать контакт\n2.Найти контакт\n3.Редактировать контакт\n4.Удаление контакта\n5.Выход')
while True:
    com = input('Введите номер команды:')
    if com == ('1'):
        print("Нажмите 'Enter', чтобы пропустить ввод какого-либо пункта.")
        creats()
    if com == ('2'):
        s_word = input('Введите имя, фамилию, отчество, псевдоним, электронную почту или номер телефона контакта:')
        search(direc_users = direc_users, s_word = s_word)
    if com == ('3'):
        search(direc_users = direc_users, kods = 1)
        number = input("Для выбора контакта введите его идентификационный номер.Для отмены и перехода в главное меню введите '0':")
        if number != ('0'):
            with open(direc_users) as file:
                list_direc_users = file.readlines()
                for i in list_direc_users:
                    list_direc_users[list_direc_users.index(i)] = i.split('|')
                    try:
                        list_direc_users.remove('\n')
                    except ValueError:
                        pass
        
            for users in list_direc_users:
                if users[0] == number:
                    print("Если не хотите изменять изменять какие-либо данные контакта, то нажмите 'Enter'")
                    for i in at:
                        i = at.index(i)
                        x = i + 1
                        print('Текущее', at[i], ':', users[x])
                        new = input('Введите новое значение:')
                        if new != (''):
                            users[x] = new
                    with open(direc_users, 'w') as file:
                        for i in list_direc_users:
                            usr = '|'.join(i)
                            print(usr, file = file, end = '')
                            print('\n', file = file, end = '')
    if com == ('4'):
        search(direc_users = direc_users, kods = 1)
        number = input("Для выбора контакта, который вы хотите НАВСЕГДА удалить, введите его идентификационный номер.Для отмены и перехода в главное меню введите '0':")
        if number != ('0'):
            list_direc_users = clean()
            warning = ("Вы действительно хотите удалить выбранный конакт под индентификационным номером" + number + "?" + "(Введите '1' - 'Да' , или '2' - 'Нет'):")
            answer = input(warning)
            if answer == ("1"):
                number = int(number); number = number - 1
                del list_direc_users[number]
                for i in list_direc_users[number::]:
                    i[0] = int(i[0])
                    i[0] = i[0] - 1
                    i[0] = str(i[0])
                list_direc_users_2 = []
                for i in list_direc_users:
                    list_direc_users_2.append('|'.join(i))
                with open(direc_users, 'w') as file:
                    for users in list_direc_users_2:
                        print(users, file = file, end = '')
                        print('\n', file = file, end = '')

#    if com == ('5'):
#        print("Меню 'Настройки' находится в разработке")
    if com == ('5'):
        exits = input("Вы действительно хотите выйти?(Введите 1 - 'Да' или 0 - 'Нет'.)")
        if exits == ('1'):
            break

