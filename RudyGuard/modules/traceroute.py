import subprocess

def is_public(ip):
    ip_parts = ip.split('.')
    return not (
        ip.startswith("10.") or
        ip.startswith("192.168.") or
        (ip_parts[0] == "172" and 16 <= int(ip_parts[1]) <= 31) or
        ip == "127.0.0.1"
    )

class Traceroute:
    def run(self, ip):
        if not is_public(ip):
            return ["LAN hop"]
        try:
            result = subprocess.check_output(["traceroute", "-m", "8", ip], stderr=subprocess.DEVNULL)
            lines = result.decode().split("\n")[1:9]
            hops = [line.strip() for line in lines if line]
            return hops or ["No hops"]
        except Exception:
            return ["Traceroute failed"]