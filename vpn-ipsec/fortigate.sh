# Interface Tunnel
config system interface
    edit "VPN-PALO-ALTO"
        set ip 169.255.1.1 255.255.255.252
        set type tunnel
        set remote-ip 169.255.1.2
        set interface "wan1"
    next
end

# IKE
config vpn ipsec phase1-interface
    edit "VPN-PALO-ALTO-P1"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set net-device disable
        set proposal aes256-sha256
        set dhgrp 14
        set lifetime 28800
        set remote-gw 189.212.0.2
        set psksecret "D3S@FIO-M3RC@D0L1BR3"
    next
end

# IPsec
config vpn ipsec phase2-interface
    edit "VPN-PALO-ALTO-P2"
        set phase1name "VPN-PALO-ALTO-P1"
        set proposal aes256-sha256
        set pfs enable
        set dhgrp 14
        set lifetime 3600
        set src-subnet 192.168.100.0 255.255.255.192
        set dst-subnet 172.16.0.0 255.255.255.224
    next
end

# Politica
config firewall policy
    edit 10
        set name "VPN-TO-PALO-ALTO"
        set srcintf "lan"
        set dstintf "VPN-PALO-ALTO"
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
        set dst 172.16.0.0/27
        set device "VPN-PALO-ALTO"
        set gateway 169.255.1.2
    next
end

