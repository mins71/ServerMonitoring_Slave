import psutil
import schedule
from time import time

class Schedular:

    def SetEvery5Sec(self, user_func, *args):
        # 스케쥴 입력
        schedule.every().minute.at(":00").do(user_func, args)
        schedule.every().minute.at(":05").do(user_func, args)
        schedule.every().minute.at(":10").do(user_func, args)
        schedule.every().minute.at(":15").do(user_func, args)
        schedule.every().minute.at(":20").do(user_func, args)
        schedule.every().minute.at(":25").do(user_func, args)
        schedule.every().minute.at(":30").do(user_func, args)
        schedule.every().minute.at(":35").do(user_func, args)
        schedule.every().minute.at(":40").do(user_func, args)
        schedule.every().minute.at(":45").do(user_func, args)
        schedule.every().minute.at(":50").do(user_func, args)
        schedule.every().minute.at(":55").do(user_func, args)
