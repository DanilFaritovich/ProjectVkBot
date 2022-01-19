import vk_api
import pickle
import datetime
import time

with open("AccesTokenUser.pickle", "rb") as f:
    data = pickle.load(f)

token = data["access_token"]
session = vk_api.VkApi(token=token)
vk = session.get_api()
User_id = data["User_id"]

def get_user_dialogs(user_id):

    def pick_all_messages():
        f = open("information_of_user\info_about_{}.pickle".format(user_id), "ab")
        pickle.dump({"Output-user": User_id}, f)
        pickle.dump(user_info[0], f)
        chat = session.method("messages.search", {"date": 20122300, "peer_id": user_info[0]["id"], "count": 100})
        dialogs = chat["items"]
        chek_date = 0
        print(chat["count"])
        start_time = time.time()
        while chat["count"] > 0:
            pickle.dump(chat, f)
            last_message = dialogs[len(chat["items"]) - 1]
            date_last_message = last_message["date"]
            if time.strftime("%d%m%Y", time.localtime(chek_date)) == time.strftime("%d%m%Y",
                                                                                   time.localtime(date_last_message)):
                date_last_message -= 86400
            chek_date = date_last_message
            chat = session.method("messages.search",
                                  {"date": time.strftime("%d%m%Y", time.localtime(date_last_message)),
                                   "peer_id": user_info[0]["id"], "count": 100})
            dialogs = chat["items"]
        end_time = time.time()
        print(end_time-start_time)
        f.close()

    messages_list = session.method("messages.searchConversations", {"count": 255})
    i = 0
    for a in messages_list["items"]:
        user_id = a["peer"]["id"]  # id пользователя из переписки
        user_info = session.method("users.get", {"user_ids": user_id})  # Информация о пользователе
        print(user_info)
        if i != 3:
            pick_all_messages()
        i += 1


print(time.time())
get_user_dialogs(User_id)
