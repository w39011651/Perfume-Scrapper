import time

def log(msg, end='\n'):
    if type(msg) != type(str):
        msg = str(msg)
    print(time.strftime("[%Y-%m-%d %H:%M:%S] ") + msg, end=end)

if __name__ =='__main__':
    log("Hello World")