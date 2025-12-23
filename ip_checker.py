print(r"""
███████╗██████╗  ██████╗ ██╗  ██╗
╚══███╔╝██╔══██╗██╔═══██╗╚██╗██╔╝
  ███╔╝ ██████╔╝██║   ██║ ╚███╔╝ 
 ███╔╝  ██╔══██╗██║   ██║ ██╔██╗ 
███████╗██║  ██║╚██████╔╝██╔╝ ██╗
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
        Z R O X   I P   C H E C K E R
""")
import requests
import ipaddress


def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False

def check_ip(ip=None):
    # თუ ცარიელია → შენი public IP
    if not ip:
        url = "http://ip-api.com/json/"
        data = requests.get(url).json()
    else:
        # ლოკალური IP შემოწმება
        if is_private_ip(ip):
            print("\n[ LOCAL IP DETECTED ]")
            print(f"IP: {ip}")
            print("Type: Private / Local Network")
            print("Location: Not available (Internal network)")
            print("Usage: Router, PC, Phone, LAN device")
            return
        else:
            url = f"http://ip-api.com/json/{ip}"
            data = requests.get(url).json()

    if data.get("status") == "success":
        print("\n[ IP CHECK RESULT ]")
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"ASN: {data['as']}")
    else:
        print("❌ IP ვერ მოიძებნა")

# Main loop
while True:
    ip = input("\nშეიყვანე IP (ცარიელი = შენი IP, exit = გასვლა): ")
    if ip.lower() == "exit":
        print("გამოსვლა...")
        break
    check_ip(ip.strip() if ip else None)



