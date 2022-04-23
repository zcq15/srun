import os
import time
from UCASSrunLogin.LoginManager import LoginManager

def always_login(username, password, checkinterval):
    lm = LoginManager()
    login = lambda : lm.login(username=username, password=password)
    timestamp = lambda : print(time.asctime(time.localtime(time.time())))

    while 1:
        timestamp()
        try:
            login()
        except Exception:
            pass
        print('Sleeping ...')
        time.sleep(checkinterval)
        
if __name__ == "__main__":
    username = "xxxx"
    password = "xxxx"
    checkinterval = 5 * 60

    always_login(username, password, checkinterval)
