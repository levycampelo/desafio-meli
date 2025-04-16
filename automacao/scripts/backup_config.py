from netmiko import ConnectHandler
from datetime import datetime
import os

def bkp_config():
    device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.68.55',
        'username': 'levy',
        'password': 'd3s@f10-m3li',
    }

    try:
        conn = ConnectHandler(**device)

        hostname = conn.send_command("show running-config | include hostname").strip()
        if hostname.lower().startswith("hostname"):
            hostname = hostname.split()[1]
        else:
            hostname = "unknown"

        output = conn.send_command("show running-config")

        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"/tmp/{hostname}_{now}.txt"

        with open(filename, "w") as f:
            f.write(output)

        conn.disconnect()

        return f"""
        <h3>Backup realizado!</h3>
        <p>Arquivo salvo em: <code>{filename}</code></p>
        """

    except Exception as e:
        return f"<h3>Erro:</h3><pre>{str(e)}</pre>"

