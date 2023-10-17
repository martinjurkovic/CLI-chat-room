import requests

server_url = 'http://127.0.0.1:8000/'

def send_message(username, message):
    data = {'username': username, 'message': message}
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
    username = input('Enter your username: ')
    while True:
        action = input('Enter 1 to send a message, 2 to get messages: ')
        if action == '1':
            message = input('Enter your message: ')
            send_message(username, message)
        elif action == '2':
            get_messages()
        else:
            print('Invalid choice')




