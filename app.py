from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-beige-horse-m0qsly8z.ws-us18.gitpod.io"

vendas = [
    {"id": 1, "name": "Lucas Alixame", "product": "Camiseta Azul - G", "price": 25.00 },
    {"id": 2, "name": "Ana Maria", "product": "Camiseta Rosa - M", "price": 25.00},
]

@app.route('/')
def index():
    """
        Renderizando Tela: INDEX
        Passando variavel: lista(tipo lista de dados)
    """
    return render_template('index.html', lista=vendas)

@app.route('/create')
def create():
    """
        Renderizando Tela: CREATE
    """
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    """
        Pegando Dados do Formulario
    """
    name = request.form['name']          # <input name="name"/>
    product = request.form['product']    # <input name="product"/>
    price = request.form['price']        # <input name="price"/>

    """
        Aplicando REPLACE no preço (trocando , por .)
    """
    price = price.replace(",", ".")

    """
        Verificando se a lista esta vazia e Identificando ultimo elemento dentro da lista
    """
    if vendas:
        ultimo = vendas[-1]
    else:
        ultimo = {"id": 0}

    """
        Moldando Lista e definindo dados
        OBS: Ao definir o 'id' do registro, utilizamos o ultimo elemento da lista somando o valor de seu id + 1
    """
    venda = {"id": ultimo["id"] + 1,"name": name, "product": product, "price": float(price)}

    """
        Adicionando elemento a lista
    """
    vendas.append(venda)

    """
        Redirecionando para a pagina principal
    """
    return redirect(URL + '/')

@app.route('/delete/<id>')
def delete(id):
    """
        Percorrendo a lista, trazendo indice e elemento para excluir o elemento certo
    """
    for indice, venda in enumerate(vendas):
        if venda["id"] == int(id):
            del vendas[indice]
    
    return redirect(URL + '/')

@app.route('?search', methods=['POST'])
def search():
    search = request.form['search']          # <input name="name"/>

    listaPesquisa = []

    for indice, venda in enumerate(vendas):
        if search in venda["name"] or search in venda["product"]:
            listaPesquisa.append(venda)

    return render_template('index.html', lista=listaPesquisa)


app.run(debug=True)



# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)
