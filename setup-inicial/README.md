## Ambiente do desafio 

O desafio foi construído no meu ambiente local utilizando o Proxmox. Para isso, criei uma nova VM com o software **EVE-NG**.

O **EVE-NG CE (Community Edition)** é uma plataforma gratuita de emulação de redes, baseada em Linux, utilizada para criar laboratórios virtuais com equipamentos de rede, como roteadores, switches, firewalls, servidores e outros dispositivos.

## Setup Inicial

A seguir, os passos para configuração básica de acesso entre o ambiente virtual e a internet:

#### Configurando IP de Acesso

```shell
conf t
interface giga 0/0
no switchport
ip address 192.168.68.55 255.255.255.0
exit

ip route 0.0.0.0 0.0.0.0 192.168.68.1

ip domain-name desafiomeli
crypto key generate rsa 4096

username levy privilege 15 secret d3s@f10-m3li

line vty 0 15
transport input ssh
login local
exit
```
