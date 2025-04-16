from netmiko import ConnectHandler

def wr_config():
    device = {
        'device_type': 'cisco_ios', 
        'ip': '192.168.68.55',
        'username': 'levy',
        'password': 'd3s@f10-m3li',
    }

    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("write memory")        
        conn.disconnect()
        return f"Configuração salva com sucesso!<br><pre>{output}</pre>"
    except Exception as e:
        return f"Erro ao tentar salvar as configurações: {str(e)}"

