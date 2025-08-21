import psutil
from datetime import datetime
import socket
import struct

def is_private_ip(ip):
    try:
        ip_parts = ip.split('.')
        return (
            ip.startswith("10.") or
            ip.startswith("192.168.") or
            (ip_parts[0] == "172" and 16 <= int(ip_parts[1]) <= 31) or
            ip == "127.0.0.1"
        )
    except Exception:
        return False

class ConnectionScanner:
    def get_connections(self):
        conns = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.raddr:
                proto = self.get_protocol(conn.type)
                remote_ip = conn.raddr.ip
                conns.append({
                    "local_ip": conn.laddr.ip,
                    "local_port": conn.laddr.port,
                    "remote_ip": remote_ip,
                    "remote_port": conn.raddr.port,
                    "protocol": proto,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "is_private": is_private_ip(remote_ip)
                })
        return conns

    def get_protocol(self, proto_type):
        if proto_type == 2:
            return "UDP"
        elif proto_type == 1:
            return "TCP"
        else:
            return "UNKNOWN"