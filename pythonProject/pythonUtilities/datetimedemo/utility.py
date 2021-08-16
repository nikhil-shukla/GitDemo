import datetime

def current_time():
    return datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
