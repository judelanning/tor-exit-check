#Used to grab list of Tor exit node IPs from Tor Project
import urllib.request

#Used to grab user-provided IPs to check
import sys

#Grabs list of current Tor exit node IPs and returns them as a list
def get_exit_node_ips():
    with urllib.request.urlopen('https://check.torproject.org/torbulkexitlist') as f:
        ips_string = f.read().decode('utf-8')

        ips_list = list(ips_string.split("\n"))

        return ips_list

#Checks if the user provided IPs are in the Tor exit node IP list
def check_ip(ip):
    if ip in get_exit_node_ips():
        print("Yes, " + ip + " is a Tor exit node.")
    else:
        print("No, " + ip + " is not a Tor exit node.")

#Gathers all user-provided IPs and sends them to be checked
def start_check():
    #Filters out index 0 as it is always the file name
    ips = sys.argv[1:]

    for ip in ips:
        check_ip(ip)

#Starts script
start_check()