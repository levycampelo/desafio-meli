### Levantamento de requisitos para automação de uma VPN com IPSEC entre FW Fortigate e PaloAlto. 
Tópicos principais:

- Definição de parametros:
- Identificação de Ferramentas/API:
- Brief automação:
- Considerações/Validações:

### Definição VPN com IPSEC:
Uma VPN IPsec é uma Rede Virtual Privada que utiliza o protocolo IPsec (Internet Protocol Security) para criar um túnel seguros entre dois dispositivos ou uma rede. O IPsec fornece criptografia e autenticação, garantindo que as comunicações entre os dispositivos sejam protegidas e não possam ser interceptadas. 

### Levantamento dos parâmetros da VPN:

| Endereços WAN dos FW | IP-ADDRESS | 
| -------------------- | ---------- |
| FortiGate            | 200.210.199.1/30        |
| Palo Alto            | 189.212.0.1/30        |

| Redes Locais | IP-ADDRESS |
| ------------ | ---------- |
| FortiGate    | 192.168.100.1/26       |
| PaloAlto    | 172.16.0.1/27       |

| Túnel IPSEC | IP-ADDRESS |
| ----------- | ---------- |
| FortiGate | 169.255.1.1/30 |
| PaloAlto | 169.255.1.2/30 |

| Proposta Fase 1 | Security |
| --------------- | -------- | 
| Criptografia    |   AES256       |
| Autenticacao    |   SHA256       |
| Lifetime        |   28800      |
| DH Group        |    14  |

| Proposta Fase 2 | Security | 
| --------------- | -------- |
| Criptografia      |  AES256       |
| Autenticacao      |  SHA256      |
| Lifetime          |   3600     |
| DH Group          |    14      |
| Protocol          |   ESP     |

Estudar a possibilidade de implementar criptografia SHA384 e DH group 19 para aumentar o nível de segurança.


### Ferramentas/APIs:

| Dispositivo | Interfaces | Ferramentas | 
| ----------- | ---------- | ----------- |
| FortiGate   | API REST, SSH/CLI | request, paramiko |
| PaloAlto   | API REST, SSH/CLI | paramiko, ansible, terraform |

### Possibilidade de gerenciamento centralizado:

- FortiManager
- Panorama (PaloAlto)

### Passos lógicos para automação:

- Mapear todas as conectividades físicas;
- Mapear todas as conexões lógicas;
- Mapear todos os endereços WAN, LAN, interfaces e IP do Túnel IPSEC;
- Mapear conexões de API e Firewall necessárias para atingir as redes locais;
- Mapear as politicas necessárias para permitir o trafego entre as redes e sub-redes;
- Mapear a necessidade de criar politicas para liberar e negar trafego entre as redes;
- Mapear a necessidade de roteamento estático ou dinamico entre as redes de diferentes regiões via tunel;

- Criar rotina de validações (ping, tunnel status e logs) via check do zabbix;
> Validar o status do tunel = ike-sa e ipsec-sa
- Criar dashboard para monitoramento de latencia, status do tunel e logs.

### Check após configurações:

FortiGate = get vpn ipsec tunnel, diagnose vpn tunnel<br>
PaloAlto = show vpn ike-sa, show vpn ipsec-sa


