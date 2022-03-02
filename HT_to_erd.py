import requests
import time 

URL = "https://api.elrond.com"

# Get ready with a list of hero tags (one per line)
hero_tags = open("addresses_giveaway_ht.txt").read().split("\n")

addresses = []
for ht in hero_tags : 
    
    # sending get request 
    addr_requests = requests.get(url = URL + "/usernames/" + ht)
    
    # Retrieving the address for the Hero tag ht
    addr_results = addr_requests.json()["address"]
    
    # Saving the address to the list of addresses
    addresses.append(addr_results)
    
    # Pause for 0.1s to not send too many requests at once to the API
    time.sleep(0.2) 
    
# Save the addresses in a separate file
with open("addresses_giveaway_erd.txt","w") as f : 
    f.write("\n".join(addresses)) 