#!/usr/bin/env python3
"""
Simple Network Scanner
Scans your local network for active hosts and open ports
Author: Jeff Diener
Date: February 10, 2026
"""

import socket
import ipaddress
from datetime import datetime

def get_local_ip():
    """Get your computer's local IP address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def scan_port(ip, port, timeout=1):
    """Check if a specific port is open on an IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0  # 0 means port is open
    except:
        return False

def scan_host(ip, common_ports):
    """Scan a single host for common ports"""
    open_ports = []
    for port in common_ports:
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

def get_hostname(ip):
    """Try to get the hostname for an IP address"""
    try:
        hostname = socket.gethostbyaddr(str(ip))[0]
        return hostname
    except:
        return "Unknown"
    
def main():
    print("=" * 60)
    print("NETWORK SCANNER - Jeff Diener")
    print("=" * 60)
    
    # Get your local IP
    local_ip = get_local_ip()
    print(f"\n[*] Your IP: {local_ip}")
    
    # Figure out your network (assumes /24 subnet)
    network_parts = local_ip.split('.')
    network = f"{network_parts[0]}.{network_parts[1]}.{network_parts[2]}.0/24"
    print(f"[*] Scanning network: {network}")
    
    # Common ports to check
    common_ports = [21, 22, 23, 25, 80, 443, 445, 3389, 8080]
    print(f"[*] Checking ports: {common_ports}")
    
    print(f"\n[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    active_hosts = 0
    
    # Scan each IP in the network
    for ip in ipaddress.IPv4Network(network, strict=False):
        if scan_port(ip, 80, timeout=0.5) or scan_port(ip, 443, timeout=0.5):
            active_hosts += 1
            hostname = get_hostname(ip)
            print(f"\n[+] Host found: {ip}")
            print(f"    Hostname: {hostname}")
            
            open_ports = scan_host(ip, common_ports)
            if open_ports:
                print(f"    Open ports: {open_ports}")  
    print("\n" + "=" * 60)
    print(f"[*] Scan complete!")
    print(f"[*] Active hosts found: {active_hosts}")
    print(f"[*] Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

if __name__ == "__main__":
    main()