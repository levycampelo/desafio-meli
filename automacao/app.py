from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='interface')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vlan = request.form.get('vlan')
        hostname = request.form.get('hostname')
        return f"VLAN: {vlan}, Hostname: {hostname}"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

