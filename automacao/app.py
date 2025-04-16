from flask import Flask, render_template, request
from scripts.configurar_vlan import aplicar_vlan

app = Flask(__name__, template_folder='interface')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vlan', methods=['GET', 'POST'])
def configurar_vlan():
    if request.method == 'POST':
        id_vlan = request.form['id_vlan']
        nome_vlan = request.form['nome_vlan'].upper()
        resultado = aplicar_vlan(id_vlan, nome_vlan)
        return f"<h3>{resultado}</h3><br><a href='/'>Voltar</a>"
    return render_template('vlan.html')

@app.route('/hostname')
def configurar_hostname():
    return render_template('hostname.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

