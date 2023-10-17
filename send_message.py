import requests
import argparse
import datetime

def send_message(username, message):
    data = {'username': username, 'message': message, "timestamp": datetime.datetime.now().timestamp()}
    response = requests.post(f'{server_url}/send', json=data)
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')

def get_messages():
    response = requests.get(f'{server_url}/get_messages')
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        for message in messages:
            print(f"{message['username']}: {message['message']}")
    else:
        print('Failed to retrieve messages')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('server_url', help='URL of the chat server')
    args = parser.parse_args()

    server_url = args.server_url
    username = input('Enter your username: ')
    while True:
        message = input('Enter your message: ')
        send_message(username, message)



