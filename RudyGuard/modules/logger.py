import json

class LogManager:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = []

    def log_connection(self, conn, status, geo, hops):
        log_entry = {
            "local_ip": conn["local_ip"],
            "local_port": conn["local_port"],
            "remote_ip": conn["remote_ip"],
            "remote_port": conn["remote_port"],
            "protocol": conn["protocol"],
            "timestamp": conn["timestamp"],
            "status": status,
            "country": geo.get("country"),
            "region": geo.get("region"),
            "isp": geo.get("isp"),
            "domain": geo.get("domain"),
            "traceroute": hops
        }
        self.logs.append(log_entry)

    def save_logs(self):
        with open(self.log_file, "w") as f:
            json.dump(self.logs, f, indent=2)