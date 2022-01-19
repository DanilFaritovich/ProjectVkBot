import vk_api
import os
import json
import pickle

kod = ["D", "a", "n", "c", "h", "i", "k", "t", "v", "3", "2", "1"]
login = ''
passw = ''
index = 0
with open("string.bin", "r") as f:
    for a in f.readlines()[-1]:
        if a not in kod:
            print("Fack")
            print(a)
        if a == "|":
            index = 1
        if index == 1 and a != "|":
            passw += a
        elif index == 0 and a != "|":
            login += a

with open("HelloKity", "w") as f:
    f.write(passw)
with open("HelloKity", "r") as f:
    passw = f.readline()
print(login)
print(passw)
print(type(passw))
vk_api.VkApi()
VK = vk_api.VkApi(login=login, password=passw, scope=215989462, app_id=6121396)
VK.auth()
VK = VK.get_api()
access_token = 0

try:
    User = VK.users.get()
except:
    print("Error")
else:
    print(f"\nHello {User[0]['first_name']}")

    with open('vk_config.v2.json', 'r') as data_file:
        data = json.load(data_file)
        print(data)

    for xxx in data[login]['token'].keys():
        for yyy in data[login]['token'][xxx].keys():
            access_token = data[login]['token'][xxx][yyy]['access_token']

    print('=' * 85)
    print(f"Твой ID {User[0]['id']}")
    print('=' * 85)
    print(f"Access_Token: {access_token}")
    print('=' * 85)

    os.remove('vk_config.v2.json')

Dict = {"User_id": User[0]['id'], "access_token": access_token}
file = open("AccesTokenUser.pickle", "wb")
pickle.dump(Dict, file)
file.close()


import save_info
save_info.start()
