import urllib.request
import sys

def get_exit_node_ips():
    with urllib.request.urlopen('https://check.torproject.org/torbulkexitlist') as f:
        ips_string = f.read().decode('utf-8')

        ips_list = list(ips_string.split("\n"))
        
        return ips_list

def check_ip(ip):
    if ip in get_exit_node_ips():
        print("Yes, " + ip + " is a Tor exit node.")
    else:
        print("No, " + ip + " is not a Tor exit node.")

def manual_check():
    ip_to_check = input("Enter the IP address you would like to check: ")

    check_ip(ip_to_check)

def check_for_cli_arguments():
    ips = sys.argv[1:]

    if ips == []:
        manual_check()
    else:
        for ip in ips:
            check_ip(ip)

check_for_cli_arguments()