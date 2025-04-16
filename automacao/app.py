from flask import Flask, render_template

app = Flask(__name__, template_folder='interface')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vlan')
def configurar_vlan():
    return render_template('vlan.html')

@app.route('/hostname')
def configurar_hostname():
    return render_template('hostname.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

