from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder='views')

# URL do seu repositório Servidor
API_URL = "http://127.0.0.1:5000/api"


@app.route('/', methods=['GET', 'POST'])
def index():
    termo = request.form.get('termo_busca', '') if request.method == 'POST' else ""

    # O Cliente "pede" os livros para a API
    resp_livros = requests.get(f"{API_URL}/livros?termo={termo}")
    livros = resp_livros.json() if resp_livros.status_code == 200 else []

    # O Cliente "pede" o carrinho para saber o total
    resp_carrinho = requests.get(f"{API_URL}/carrinho")
    carrinho = resp_carrinho.json() if resp_carrinho.status_code == 200 else []

    return render_template('index.html', livros=livros, termo_pesquisado=termo, total_carrinho=len(carrinho))


@app.route('/categoria/<nome>')
def categoria(nome):
    resp_livros = requests.get(f"{API_URL}/categoria/{nome}")
    livros = resp_livros.json() if resp_livros.status_code == 200 else []

    resp_carrinho = requests.get(f"{API_URL}/carrinho")
    carrinho = resp_carrinho.json() if resp_carrinho.status_code == 200 else []

    return render_template('index.html', livros=livros, termo_pesquisado=f"Categoria: {nome}",
                           total_carrinho=len(carrinho))


@app.route('/adicionar/<titulo>', methods=['POST'])
def adicionar(titulo):
    # Envia um POST para a API adicionar
    requests.post(f"{API_URL}/carrinho", json={"titulo": titulo})
    return redirect(url_for('index'))


@app.route('/carrinho')
def ver_carrinho():
    resp_carrinho = requests.get(f"{API_URL}/carrinho")
    carrinho = resp_carrinho.json() if resp_carrinho.status_code == 200 else []
    return render_template('carrinho.html', livros_carrinho=carrinho, total_carrinho=len(carrinho))


@app.route('/remover/<titulo>', methods=['POST'])
def remover(titulo):
    # Envia um DELETE para a API remover
    requests.delete(f"{API_URL}/carrinho", json={"titulo": titulo})
    return redirect(url_for('ver_carrinho'))


@app.route('/checkout')
def checkout():
    resp_carrinho = requests.get(f"{API_URL}/carrinho")
    carrinho = resp_carrinho.json() if resp_carrinho.status_code == 200 else []

    if not carrinho:
        return redirect(url_for('ver_carrinho'))
    return render_template('checkout.html', total_itens=len(carrinho))


@app.route('/pagamento', methods=['POST'])
def pagamento():
    metodo = request.form.get('metodo_pagamento')
    # Solicita para a API esvaziar o carrinho
    requests.post(f"{API_URL}/carrinho/limpar")
    return render_template('sucesso.html', metodo=metodo)


if __name__ == '__main__':
    # O Cliente roda na porta 5001 para não dar conflito com o Servidor
    app.run(port=5001, debug=True)