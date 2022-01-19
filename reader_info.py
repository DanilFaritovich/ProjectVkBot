import pickle
import time

with open("information_of_user\info_about_143543086.pickle", "rb") as f:
    while 0 != 1:
        try:
            print(pickle.load(f))
        except:
            print("Информация прочитана!")
            break