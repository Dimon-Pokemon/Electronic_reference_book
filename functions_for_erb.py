from json import load, dump


def read_or_write(path_file:str, mode:str, data:dict=None):
    if mode=="read":
        with open(path_file, 'r') as file:
            users = load(file)
            return users
    elif mode=="write":
        with open(path_file, 'w'):
            dump(data, path_file, indent=4)
        return None
            
def search(data:dict, search_obj:"str or int") ->list: #data - словарь, в котором нужно найти все элементы с search_obj(то, что надо найти)
    matches = [] #совпадения
    for i in data.values():
        if search_obj in i.values():
            matches.append(i)
    return matches

def add_contact(inpt_data:list, id_last_user:int): #inpt_data - введенные пользователем данные; id_last_user - номер последнего созданного контакта
    id_new_user = id_last_user + 1
    user_attribut = ["id", "name", "middle_name", "first_name",
            "telephone_number", "email", "additional_information"]
    user = {}
    for i in range(7):
        user[user_attribut[i]] = inpt_data[i]
    return user

if __name__ == "__main__":
    print(read_or_write("users.json", "read"))
    print(search(read_or_write("users.json", "read"), "Dima"))
    print(add_contact([]))
