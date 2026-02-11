# Network Scanner

Python-based network reconnaissance tool for mapping local network topology and identifying open ports.

## Features
- Automatic local network detection
- Multi-host scanning across /24 subnet
- Hostname resolution via reverse DNS
- Common port enumeration (21, 22, 23, 25, 80, 443, 445, 3389, 8080)
- Clean, formatted output

## Usage
```bash
python network_scanner.py
```

## Example Output
```
[+] Host found: 123.456.7.890
    Hostname: jellyfin-server.attlocal.net
    Open ports: [80, 443, 8080]
```

## Technical Details
- **Language:** Python 3.13
- **Libraries:** socket, ipaddress, datetime
- **Scan Method:** TCP connect scan
- **Network:** Auto-detects /24 subnet from host IP

## Security Note
⚠️ Only scan networks you own or have explicit permission to test. Unauthorized network scanning may violate computer fraud laws.

## Author
Jeff Diener - February 2026

## Skills Demonstrated
- Python programming
- Network protocols (TCP/IP)
- Socket programming
- Network reconnaissance
- Security tool development
