import requests
import time
from datetime import datetime
import argparse

def convert_timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

def get_messages(server_url, last_timestamp):
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
    return last_timestamp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('server_url', help='URL of the chat server')
    args = parser.parse_args()

    server_url = args.server_url
    last_timestamp = 0

    while True:
        last_timestamp = get_messages(server_url, last_timestamp)
        time.sleep(1)  # Adjust the polling interval as needed (e.g., 1 second)
