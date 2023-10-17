from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Initialize a list to store chat messages
messages = []


@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    username = data['username']
    message = data['message']
    timestamp = time.time()
    messages.append({'username': username, 'message': message,
                     'timestamp': timestamp})
    return jsonify({'message': 'Message sent successfully\n'})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run()