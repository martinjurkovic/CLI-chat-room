import requests
import time
from datetime import datetime

server_url = 'http://127.0.0.1:8000/'
last_timestamp = 0

def convert_timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

def get_messages():
    global last_timestamp
    response = requests.get(f'{server_url}/get_messages')
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        for message in messages:
            message_time = message['timestamp']
            if message_time > last_timestamp:
                time_str = convert_timestamp_to_time(message_time)
                print(f"{message['username']} ({time_str}): {message['message']}")
                last_timestamp = message_time
    else:
        print('Failed to retrieve messages')

if __name__ == '__main__':
    while True:
        get_messages()
        time.sleep(1) 