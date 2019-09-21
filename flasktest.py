from flask import Flask, request, render_template
from flask_socketio import SocketIO, send
import pyautogui

app = Flask(__name__)
app.secret_key = "mysecret"
socket_io = SocketIO(app)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/mfd')
def mfd():
	return render_template('mfd.html')

@app.route('/chat')
def chatting():
	return render_template('chat.html')


@socket_io.on('message')
def request(message):
	print('Message:', message)
	to_client = dict()
	if message == 'new_connect':
		to_client['type'] = 'connect'
		to_client['message'] = 'new comming'
	else:
		to_client['type'] = 'normal'
		to_client['message'] = message
		pyautogui.keyDown(message)
		pyautogui.keyUp(message)
		
	send(to_client, broadcast=True)

if __name__ == '__main__':
	#app.run()
	socket_io.run(app, host='0.0.0.0', port=5000)

