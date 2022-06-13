from flask import Flask ,render_template
app = Flask(__name__)

# @ decorator é uma função que vem antes de um função, 
# para atribuir uma nova funcionalidade para a função seguinte
# no nosso caso, atribuir um link para cada uma das funções que estamos
# declarando

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contatos')
def contato():
    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)

# site estático
# site dinamico
# vai variar conforme a necessidade
