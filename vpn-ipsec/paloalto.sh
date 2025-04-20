# Interface Tunnel
set network interface tunnel units tunnel.1 ip 169.255.1.2/30
set network interface tunnel units tunnel.1 mtu 1400

# IKE Gateway
set network ike gateway VPN-FORTI-GW interface ethernet1/1 local-address 189.212.0.2 peer-address 200.210.199.2
set network ike gateway VPN-FORTI-GW ikev2-profile default
set network ike gateway VPN-FORTI-GW authentication pre-shared-key key D3S@FIO-M3RC@D0L1BR3

# IKE
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE encryption aes-256
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE hash sha256
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE dh-group group14
set network ike crypto-profiles ike-crypto-profile VPN-IKE-PROFILE lifetime 28800

# IPsec
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE esp encryption aes-256
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE esp authentication sha256
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE dh-group group14
set network ipsec crypto-profiles ipsec-crypto-profile VPN-IPSEC-PROFILE lifetime 3600

# Bind
set network tunnel ipsec VPN-FORTI-TUNNEL tunnel-interface tunnel.1 ike-gateway VPN-FORTI-GW ipsec-crypto-profile VPN-IPSEC-PROFILE

# Rotas
set network virtual-router default routing-table ip static-route to-FORTI destination 192.168.100.0/26 interface tunnel.1

# Politicas
set rulebase security rules allow-VPN from trust to untrust source 172.16.0.0/27 destination 192.168.100.0/26 application any action allow

