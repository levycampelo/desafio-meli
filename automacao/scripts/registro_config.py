import os
import json
from datetime import datetime

PASTA_JSON = '/tmp/json'
ARQUIVO_JSON = os.path.join(PASTA_JSON, 'config_aplicada.json')

os.makedirs(PASTA_JSON, exist_ok=True)

def salvar_vlan_json(vlan_id, vlan_nome):
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    if 'vlans' not in data:
        data['vlans'] = []

    data['vlans'].append({
        'id': int(vlan_id),
        'nome': vlan_nome,
        'data_aplicacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(data, f, indent=4)

def salvar_hostname_json(hostname):
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    data['hostname'] = {
        'valor': hostname,
        'data_aplicacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(data, f, indent=4)

