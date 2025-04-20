# Interface Tunnel
set network interface tunnel units tunnel.1 ip 169.255.1.2/30
set network interface tunnel units tunnel.1 mtu 1400

# IKE Gateway
set network ike gateway VPN-FORTI-GW interface ethernet1/1 local-address 200.0.0.2 peer-address 200.0.0.1
set network ike gateway VPN-FORTI-GW ikev2-profile default
set network ike gateway VPN-FORTI-GW authentication pre-shared-key key SENHA-SEGURA

# IKE (Phase 1)
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE encryption aes-256
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE hash sha256
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE dh-group group14
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE lifetime 28800

# IPsec (Phase 2)
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE esp encryption aes-256
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE esp authentication sha256
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE dh-group group14
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE lifetime 3600

# Tunnel Interface Bind
set network tunnel ipsec VPN-FORTI-TUNNEL tunnel-interface tunnel.1 ike-gateway VPN-FORTI-GW ipsec-crypto-profile VPN-IPSEC-PROFILE

# Rotas
set network virtual-router default routing-table ip static-route to-FORTI destination 192.168.10.0/24 interface tunnel.1

# Políticas de Segurança
set rulebase security rules allow-VPN from trust to untrust source 192.168.20.0/24 destination 192.168.10.0/24 application any action allow

