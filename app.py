from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1=Jogo('Tetris', 'Puzzle', 'Atari')
jogo2=Jogo('God of war', 'Rack n Slash', 'PS2')
jogo3=Jogo('FIFA24', 'Esporte', 'PS5')

lista = [jogo1,jogo2, jogo3]

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route("/criar", methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)