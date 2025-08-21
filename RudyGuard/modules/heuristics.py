class HeuristicAnalyzer:
    def is_suspicious(self, conn, geo):
        suspicious_ports = {6667, 23, 3389, 4444, 5555, 8080, 31337}
        bad_countries = {"North Korea", "Iran", "Russia", "China"}
        if conn['remote_port'] in suspicious_ports:
            return True
        if geo.get("country") in bad_countries:
            return True
        return False