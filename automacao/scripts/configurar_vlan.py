from netmiko import ConnectHandler

def aplicar_vlan(id_vlan, nome_vlan):
    device = {
        'device_type': 'cisco_ios', 
        'ip': '192.168.68.11',
        'username': 'levy',
        'password': 'levy',
    }

    try:
        conn = ConnectHandler(**device)
        comandos = [
            f'vlan {id_vlan}',
            f'name {nome_vlan}',
            'exit',
        ]
        output = conn.send_config_set(comandos)
        conn.disconnect()
        return f"VLAN {id_vlan} - {nome_vlan} configurada com sucesso!<br><pre>{output}</pre>"
    except Exception as e:
        return f"Erro ao configurar VLAN: {str(e)}"

