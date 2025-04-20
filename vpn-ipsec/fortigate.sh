# Interface Tunnel
config system interface
    edit "VPN-PALO"
        set ip 169.255.1.1 255.255.255.252
        set type tunnel
        set remote-ip 169.255.1.2
        set interface "wan1"
    next
end

# IKE
config vpn ipsec phase1-interface
    edit "VPN-PALO-P1"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set net-device disable
        set proposal aes256-sha256
        set dhgrp 14
        set lifetime 28800
        set remote-gw 200.0.0.2
        set psksecret "SENHA-SEGURA"
    next
end

# IPsec
config vpn ipsec phase2-interface
    edit "VPN-PALO-P2"
        set phase1name "VPN-PALO-P1"
        set proposal aes256-sha256
        set pfs enable
        set dhgrp 14
        set lifetime 3600
        set src-subnet 192.168.10.0 255.255.255.0
        set dst-subnet 192.168.20.0 255.255.255.0
    next
end

# Política de Segurança
config firewall policy
    edit 10
        set name "VPN-TO-PALO"
        set srcintf "lan"
        set dstintf "VPN-PALO"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end

# Rota via túnel
config router static
    edit 1
        set dst 192.168.20.0/24
        set device "VPN-PALO"
        set gateway 169.255.1.2
    next
end

