# RudyGuard
Advanced, modular network monitor for Linux/Parrot OS.  Shows live TCP/UDP connections, geolocation, ISP, traceroute, alerts, logging, and more—with a stylish, colorful UI.  Made by Rudy Cooper (@FrozenBarbie01).

# 🛡️ RudyGuard: Advanced Network Security Monitor 🚀

## What is RudyGuard?

**RudyGuard** is a blazing-fast, modular, and visually advanced network monitoring/security toolkit for Linux and Parrot OS.  
Built from scratch by **Rudy Cooper (@FrozenBarbie01)**, this tool is for hackers, sysadmins, and anyone who wants deep insight into their network traffic—with style, colors, emojis, geo info, and more.

---

## Features

- 🔥 **Live Network Monitoring** (TCP/UDP, LAN/Public)
- 🌍 **True Geolocation** (Country, Region, ISP, Domain)
- 🏠 **LAN Detection** with special labels
- 🚨 **Real-Time Alerts** (Terminal, Desktop, Sound)
- 🚦 **Traceroute** (Colorful, emoji-powered hops)
- 📊 **Advanced Logging** (JSON logs for all activity)
- 🧠 **Heuristics/AI Ready** (Suspicious IPs, anomaly scoring, future ML support)
- 🎨 **Modern UI** (ASCII logo, colors, emojis, banners)
- 💡 **Easy to Extend** (Modular code, plug in your own logic)
- 🛡️ **Security Focused** (Ready for Parrot OS, root-friendly)
- 🕒 **Timestamped Events**

---

## Screenshots

![Demo Screenshot](https://raw.githubusercontent.com/FrozenBarbie01/RudyGuard/main/assets/rudysec1.cleaned.png)
---

## Installation

**Clone the repository:**
```bash
git clone https://github.com/FrozenBarbie01/RudyGuard.git
cd RudyGuard
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run RudyGuard:**
```bash
python3 RudyGuard.py
```

---

## Usage

- **Requires Python 3.8+**
- **Best run as root** for full network visibility
- **Works on Parrot OS, Kali Linux, Ubuntu, Debian**

---

## Directory Structure

```text
RudyGuard/
│
├── RudyGuard.py
├── requirements.txt
├── rudyg_suspicious_ips.json
├── modules/
│   ├── connection_scanner.py
│   ├── geolocator.py
│   ├── heuristics.py
│   ├── logger.py
│   ├── notifier.py
│   ├── suspicious_db.py
│   └── traceroute.py
```

---

## Contributing

Pull requests, issues, and feature suggestions are welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

---

## Credits

Made 100% by **Rudy Cooper (@FrozenBarbie01)**.  
No Copilot, no generators—just pure skill and passion for security.

---

## License

MIT License.  
See [LICENSE](LICENSE) for details.

---

## Contact

- Twitter: [@FrozenBarbie01](https://twitter.com/FrozenBarbie01)
- Email: frozenbarbie01@protonmail.com

---

## Support

If you love RudyGuard, star ⭐ the repo and share it!
