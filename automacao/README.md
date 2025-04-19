

## Dependências

Para os primeiros testes, foi necessário instalar os pacotes abaixo no servidor:

```bash
apt install python3 python3-pip
apt install python3-venv -y
```
Criar um ambiente virtual:
```bash
python3 -m venv venv
```
Ativar ambiente:
```bash
source venv/bin/activate
```
Instalar restante das dependências:
```bash
pip install --upgrade pip
pip install flask netmiko testresources
```

Após a instalação, execute o seguinte comando para verificar as versões instaladas:
```bash
python -m flask --version
Python 3.8.10
Flask 3.0.3
Werkzeug 3.0.6
```
Backup do switch da automação está no servidor que roda a interface grafica:
```bash
192.168.68.108
/home/levycampelo/desafio-meli/automacao/backup
```
Para executar:
```bash
python3 /automacao/app.py
