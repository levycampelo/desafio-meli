### Plano para automação de uma VPN com IPSEC entre FW Fortigate e Palo Alto. Topicos principais:

- Definição de parametros:
- Identificação de Ferramentas/API:
- Brief automação:
- Considerações/Validações:

### Definição VPN com IPSEC:
Uma VPN IPsec é uma Rede Virtual Privada que utiliza o protocolo IPsec (Internet Protocol Security) para criar um túnel seguro entre dois dispositivos ou redes. O IPsec fornece criptografia e autenticação, garantindo que as comunicações entre os dispositivos sejam protegidas e não possam ser interceptadas. 

### Levantamento dos parâmetros da VPN:
Endereços das WAN dos elementos:
FortiGate:
Palo Alto:

Redes Locais que vão se comunicar:
FortiGate:
Palo Alto:

Rede do Túnel IPSEC:
FortiGate
Palo Alto

Proposta Fase 1:
Criptografia
Autenticacao
Lifetime

Proposta Fase 2
Criptografia
Autenticacao
Lifetime
Protocol

#### Mapear ferramentas/APIs:

| Dispositivo | Interfaces | Ferramentas | 
| ----------- | ---------- | ----------- |
| FortiGate   | API REST, SSH/CLI | request, paramiko |
| Palo Alto   | API REST, SSH/CLI | paramiko, ansible, terraform |

Possibilidade de gerenciamento centralizado:

- FortiManager
- Panorama (Palo Alto)


