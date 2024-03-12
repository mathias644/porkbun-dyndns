from requests import post,get
from pickle import load

myip = get("http://ipinfo.io/ip").text

print(f"My external IP is: {myip}")

with open('variables', 'rb') as f:
    secretapikey, apikey, id, domain = load(f)

print(f"Checking if the domain {domain} is currently set to {myip}")

with open('saved_ip', 'r+') as saved_ip:
    if myip not in saved_ip.read():
        
        current_record_config = post(f"https://porkbun.com/api/json/v3/dns/retrieve/{domain}/{id}",json={"secretapikey":secretapikey, "apikey":apikey}).text

        if myip not in current_record_config:
            print("Detected that current configuration is not correct; Attempting to update current configuration")
            post(f"https://porkbun.com/api/json/v3/dns/edit/{domain}/{id}", json={"secretapikey":secretapikey, "apikey":apikey, "type": "A", "content": {myip}})

        print("Configuration updated, will update the saved_ip file now.")
        saved_ip.write(myip)