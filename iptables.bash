
sysctl -w net.ipv4.ip_forward=1
iptables -A FORWARD -o wlan0 -s 192.168.0.0/16 -m conntrack --ctstate NEW -j ACCEPT
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE



