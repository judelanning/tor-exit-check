import urllib.request

def get_exit_node_ips():
    with urllib.request.urlopen('https://check.torproject.org/torbulkexitlist') as f:
        ips_string = f.read().decode('utf-8')
        ips_list = list(ips_string.split("\n"))
        return ips_list

def check_ip(ip):
    if ip in get_exit_node_ips():
        return True
    else:
        return False

def manual_check():
    ip_to_check = input("Enter the IP address you would like to check: ")
    
    if check_ip(ip_to_check) == True:
        print("Yes, " + ip_to_check + " is a Tor exit node.")
    else:
        print("No, " + ip_to_check + " is not a Tor exit node.")

manual_check()