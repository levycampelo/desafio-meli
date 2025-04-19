import os
import json
from netmiko import ConnectHandler
from datetime import datetime

PASTA_JSON = '/tmp/json'
ARQUIVO_JSON = os.path.join(PASTA_JSON, 'config_aplicada.json')

def validar_vlan(id_vlan):
    try:
        with open(ARQUIVO_JSON, 'r') as f:
            data = json.load(f)

        vlans = data.get('vlans', [])
        vlan_config = next((vlan for vlan in vlans if vlan['id'] == int(id_vlan)), None)

        if not vlan_config:
            return f"VLAN {id_vlan} não encontrada no arquivo de configuração."

        device = {
            'device_type': 'cisco_ios',
            'ip': '192.168.68.55',
            'username': 'levy',
            'password': 'd3s@f10-m3li',
        }

        conn = ConnectHandler(**device)
        output = conn.send_command("show vlan brief")
        conn.disconnect()

        # split para pegar a primeira coluna 
        for line in output.splitlines():
            if line.strip().startswith(str(id_vlan)):
                return f"VLAN {id_vlan} configurada corretamente no dispositivo!"

        return f"VLAN {id_vlan} NÃO configurada corretamente no dispositivo. Verifique."

    except Exception as e:
        return f"Erro ao validar VLAN {id_vlan}: {str(e)}"

def validar_hostname():
    try:
        with open(ARQUIVO_JSON, 'r') as f:
            data = json.load(f)

        hostname_config = data.get('hostname', {}).get('valor')

        if not hostname_config:
            return "Hostname não encontrado no arquivo de configuração."

        device = {
            'device_type': 'cisco_ios',
            'ip': '192.168.68.55',
            'username': 'levy',
            'password': 'd3s@f10-m3li',
        }

        conn = ConnectHandler(**device)
        output = conn.send_command("show running-config | include hostname")
        conn.disconnect()

        if f'hostname {hostname_config}' in output:
            return f"Hostname {hostname_config} configurado corretamente no dispositivo!"
        else:
            return f"Hostname {hostname_config} NÃO configurado corretamente no dispositivo. Verifique."

    except Exception as e:
        return f"Erro ao validar hostname: {str(e)}"

