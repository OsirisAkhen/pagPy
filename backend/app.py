from flask import Flask, render_template # pacote instalado de roteamento (similar ao express no node) 
from flask_socketio import SocketIO, send # pacote instalado de sinalização socket (tempo real)

app = Flask(__name__) # cria o app, daqui podemos derivar rotas por exemplo. O parâmetro __name__ é uma variável especial do Python que tem por valor o nome do arquivo em si. aqui no caso "app"
app.config['SECRET_KEY'] = 'segredo' # SECRET_KEY é um código secreto usado para proteger cookies, sessões e dados sensíveis no seu app Flask.
socketio = SocketIO(app, cors_allowed_origins="*") # Ela cria uma instância do Socket.IO integrada ao Flask.

@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem: {msg}')
    send(msg, broadcast=True)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5050, debug=True)
