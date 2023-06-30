# Tor Exit Check
## A script that checks if an IP is a Tor exit node. 

Despite Tor having a legitimate use case for individuals wanting to achieve anonymity & privacy when using the internet, threat actors can abuse those same aspects about the Tor network to carry out attacks while hiding their identity. Outside of niche use cases, signs of Tor activity in a business environment are red flags that should be investigated if Tor isn't outright blocked.

This script is designed to be fed with network traffic and user authentication logs, enabling the detection of likely malicious traffic. For instance, if an endpoint is directly communicating with a Tor exit node followed by communications with a Tor entry node, that may imply the endpoint is communicating with a C2 server obfuscated by Tor. If a user account was accessed from a Tor exit node, that could signal a threat actor accessing an account with compromised credentials while hiding the actual source of the authentication. 

## Disclaimer
**False Negatives**
This script gets it's list of Tor exit nodes directly from the Tor Project here: https://check.torproject.org/torbulkexitlist. Because this list provides a list of all ***current*** Tor exit nodes, if there is a significant delay between log creation time and the time this script ingests that log, it is possible that IP is no longer being used as a Tor exit node and false negative results would be returned. 

**This Covers Low Hanging Fruit**
Because activity originating from Tor stands out like a sore thumb in business environments, threat actors have shifted away from primarily using Tor for conducting attacks. Threat actors are now commonly using commercial VPNs to access user accounts as this activity may appear benign. More advanced Chinese threat actors have even been observed compromising SOHO network devices in close physical proximity to victims and launching attacks from those devices so traffic appears benign ([Source](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a)). This script's purpose is to detect potentially malicious activity of less sophisticated attacks using the Tor network.

## Usage
**Pass IPs Using CLI**
Input:

    python3 tor-exit-check.py 20.240.36.19 199.249.230.83 213.164.206.124

Output:

    No, 20.240.36.19 is not a Tor exit node.
    Yes, 199.249.230.83 is a Tor exit node.
    Yes, 213.164.206.124 is a Tor exit node.
    


