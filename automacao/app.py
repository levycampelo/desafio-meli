import os
import json
from flask import Flask, render_template, request
from scripts.configurar_vlan import aplicar_vlan
from scripts.configurar_hostname import aplicar_hostname
from scripts.salvar_config import wr_config 
from scripts.backup_config import bkp_config
from scripts.registro_config import salvar_vlan_json, salvar_hostname_json
from scripts.validar_config import validar_vlan, validar_hostname, ARQUIVO_JSON

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
        salvar_vlan_json(id_vlan, nome_vlan)
        return f"<h3>{resultado}</h3><br><a href='/'>Voltar</a>"
    return render_template('vlan.html')

@app.route('/hostname', methods=['GET', 'POST'])
def configurar_hostname():
    if request.method == 'POST':
        hostname = request.form['hostname'].upper()
        resultado = aplicar_hostname(hostname)
        salvar_hostname_json(hostname)
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

#@app.route('/validar-config', methods=['GET', 'POST'])
#def validar_config():
#    if request.method == 'POST':
#        resultado_vlan = validar_vlan()
#        resultado_hostname = validar_hostname()
#        return f"""
#            <h3>Validação da Configuração:</h3>
#            <p>{resultado_vlan}</p>
#            <p>{resultado_hostname}</p>
#            <br><a href='/'>Voltar</a>
#        """
#    return render_template('validar_config.html')

@app.route('/validar-config')
def validar_config():
    if not os.path.exists(ARQUIVO_JSON):
        return "<h3>Nenhuma configuração aplicada ainda.</h3><br><a href='/'>Voltar</a>"

    data = json.load(open(ARQUIVO_JSON))
    resultado_host = validar_hostname()
    vlan_results= []
    for vlan in data.get('vlans', []):
        vlan_results.append(validar_vlan(vlan['id']))

    html = ["<h2>Resultado da Validação</h2>"]
    html.append(f"<p>{resultado_host}</p>")
    html.append("<ul>")
    for res in vlan_results:
        html.append(f"<li>{res}</li>")
    html.append("</ul>")
    html.append("<br><a href='/'>Voltar</a>")

    return "\n".join(html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

