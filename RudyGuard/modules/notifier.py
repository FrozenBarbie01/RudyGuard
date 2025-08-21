import subprocess

class Notifier:
    def alert(self, conn, geo):
        title = "🚨 RudyGuard Alert!"
        message = (
            f"{conn['local_ip']}:{conn['local_port']} -> {conn['remote_ip']}:{conn['remote_port']} "
            f"[{conn['protocol']}] | {geo.get('country', '')} | {geo.get('isp', '')}"
        )
        print(f"\033[91m🚨 ALERT: {message}\033[0m")
        try:
            subprocess.Popen(['notify-send', title, message])
            subprocess.Popen(['paplay', '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'])
        except Exception:
            pass