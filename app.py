from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join_chat', methods=['POST'])
def join_chat():
    room = request.form['room']
    return redirect(url_for('chat', room=room))

@app.route('/chat/<room>')
def chat(room):
    return render_template('chat.html', room=room)

@socketio.on('send_message')
def handle_send_message(data):
    room = data['room']
    message = data['message']
    emit('receive_message', {'room': room, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)