import json
import os

class SuspiciousIPDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.load_db()

    def load_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                self.suspicious_ips = set(json.load(f))
        else:
            self.suspicious_ips = set()
            self.save_db()

    def save_db(self):
        with open(self.db_file, "w") as f:
            json.dump(list(self.suspicious_ips), f)

    def is_suspicious(self, ip):
        return ip in self.suspicious_ips

    def add_suspicious(self, ip):
        self.suspicious_ips.add(ip)
        self.save_db()