import subprocess

# List of IP addresses to test
ip_addresses = [
    "8.8.8.8",       # Google DNS
    "1.1.1.1",       # Cloudflare DNS
    "192.168.1.1",   # Local router (example)
    "10.0.0.5"       # Example internal IP
]

def ping_ip(ip):
    try:
        # macOS uses -c for count
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            # Extract response time
            for line in result.stdout.split("\n"):
                if "time=" in line:
                    time_ms = line.split("time=")[1].split(" ")[0]
                    return f"🟢 ONLINE | Response Time: {time_ms} ms"
            return "🟢 ONLINE | Response time unknown"
        else:
            return "🔴 OFFLINE"
    except Exception as e:
        return f"Error: {e}"

print("=== Network Diagnostic Tool ===\n")

for ip in ip_addresses:
    status = ping_ip(ip)
    print(f"{ip} → {status}")
