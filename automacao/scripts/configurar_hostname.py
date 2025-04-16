from netmiko import ConnectHandler

def aplicar_hostname(hostname):
    device = {
        'device_type': 'cisco_ios', 
        'ip': '192.168.68.55',
        'username': 'levy',
        'password': 'd3s@f10-m3li',
    }

    try:
        conn = ConnectHandler(**device)
        comandos = [
            f'hostname {hostname}',
            'exit',
        ]
        output = conn.send_config_set(comandos)
        conn.disconnect()
        return f"HOSTNAME {hostname} configurada com sucesso!<br><pre>{output}</pre>"
    except Exception as e:
        return f"Erro ao configurar {str(e)}"

