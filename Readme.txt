Nmap Commmands

nmap -sp <IP>   -    (Scan All Networks)
nmap -O <IP>    -   (OS Info of only One IP)
nmap -sn <IP>   -   (Scan All Networks)
nmap -p 1-65535 <IP>    -    (Scan All Ports)
nmap <IP_1>, <IP_2> -    (Multiple IP Scanned)
nmap --top-ports 20 <IP>
nmap -Pn -O <IP>    -    (For checking all ports)
nmap -iL <list.txt of IPs>
nmap -p 80 -n <IP> (Disable DNS)
nmap -sV <IP> (Detection Service & OS)
nmap -p- -sV <IP>
nmap -A -T4 -vv <IP>    -    (Detect OS, Service Version, Open Ports, Trace Route, A=Aggresive Scan, T4=Fast Scan, -vv=verbose)
nmap -sU <IP>   -    (Scan TCP)
nmap -sT <IP>   -    (Scan UDP)
nmap <IP> -max-parallelism 800 -Pn --script http-slowloris --script-args http-slowloris.runforever=true
nmap -sV --script=http-malware-host <IP>
nmap --spoof-mac -sp <IP> -  (This command will restrict to other device to scan our Network)
