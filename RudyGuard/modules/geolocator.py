import requests
import socket

def is_public(ip):
    try:
        ip_parts = ip.split('.')
        return not (
            ip.startswith("10.") or
            ip.startswith("192.168.") or
            (ip_parts[0] == "172" and 16 <= int(ip_parts[1]) <= 31) or
            ip == "127.0.0.1"
        )
    except Exception:
        return False

class Geolocator:
    def get_info(self, ip):
        if not is_public(ip):
            return {
                "country": "LAN",
                "region": "Local",
                "isp": "Local Network",
                "domain": ip
            }
        try:
            resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=4)
            data = resp.json()
            country = data.get("country")
            region = data.get("regionName")
            isp = data.get("isp")
            if not country:
                country = "NoData"
            if not region:
                region = "NoData"
            if not isp:
                isp = "NoData"
            return {
                "country": country,
                "region": region,
                "isp": isp,
                "domain": self.get_domain(ip)
            }
        except Exception:
            return {
                "country": "API Error",
                "region": "API Error",
                "isp": "API Error",
                "domain": ip
            }

    def get_domain(self, ip):
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            if hostname == ip or hostname.endswith('.in-addr.arpa'):
                return ip
            return hostname
        except Exception:
            return ip