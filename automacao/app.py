from flask import Flask, render_template, request
from scripts.configurar_vlan import aplicar_vlan
from scripts.configurar_hostname import aplicar_hostname
from scripts.salvar_config import wr_config 
from scripts.backup_config import bkp_config

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

@app.route('/hostname', methods=['GET', 'POST'])
def configurar_hostname():
    if request.method == 'POST':
        hostname = request.form['hostname'].upper()
        resultado = aplicar_hostname(hostname)
        return f"<h3>{resultado}</h3><br><a href='/'>Voltar</a>"
    return render_template('hostname.html')

@app.route('/salvar')
def salvar_config():
    resultado = wr_config()
    return resultado

@app.route('/backup')
def backup_config(): 
    resultado = bkp_config()
    return resultado

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

