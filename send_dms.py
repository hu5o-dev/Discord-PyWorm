import os
from threading import Thread
from time import sleep
from json import loads, dumps
from requests import get, post
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    # Hide the root window
    Tk().withdraw()

    token = input("Enter your Discord token: ")
    message = input("Enter the message you want to send: ")
    send_file = input("Do you want to send a file as well? (yes/no): ").strip().lower()
    file_path = None
    if send_file == "yes":
        file_path = askopenfilename(title="Select file to send")
        if not file_path:
            print("No file selected. Exiting.")
            return

    delay = float(input("Enter the delay between messages in milliseconds: ")) / 1000

    Thread(target=spread, args=(token, message, file_path, delay)).start()

def get_headers(token=None, content_type='application/json'):
    headers = {
        'Content-Type': content_type,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Authorization': token
    }
    return headers

def get_friends(token):
    response = get('https://discordapp.com/api/v6/users/@me/relationships', headers=get_headers(token))
    if response.status_code == 200:
        return loads(response.content.decode())
    else:
        return []

def get_chat(token, uid):
    try:
        return post('https://discordapp.com/api/v6/users/@me/channels', headers=get_headers(token), data=dumps({'recipient_id': uid}).encode()).json()['id']
    except:
        return None

def spread(token, message, file_path, delay):
    for friend in get_friends(token):
        try:
            chat_id = get_chat(token, friend['id'])
            if chat_id:
                if file_path:
                    with open(file_path, 'rb') as f:
                        file_name, file_ext = os.path.splitext(file_path)
                        file_name = os.path.basename(file_name)

                        boundary = '-----------------------------325414537030329320151394843687'
                        payload = (
                            f'{boundary}\n'
                            f'Content-Disposition: form-data; name="file"; filename="{file_name}{file_ext}"\n'
                            f'Content-Type: application/octet-stream\n\n'
                        ).encode() + f.read() + (
                            f'\n{boundary}\n'
                            f'Content-Disposition: form-data; name="content"\n\n'
                            f'{message}\n'
                            f'{boundary}\n'
                            f'Content-Disposition: form-data; name="tts"\n\n'
                            f'false\n'
                            f'{boundary}--'
                        ).encode()

                        headers = get_headers(token, 'multipart/form-data; boundary=---------------------------325414537030329320151394843687')
                        post(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=headers, data=payload).raise_for_status()
                else:
                    payload = {
                        'content': message,
                        'tts': False
                    }
                    post(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=get_headers(token), data=dumps(payload).encode()).raise_for_status()
                print(f"Sent message to friend: {friend['user']['username']}")
            sleep(delay)
        except Exception as e:
            print(f"Failed to send to {friend['user']['username']}: {e}")

if __name__ == "__main__":
    main()
