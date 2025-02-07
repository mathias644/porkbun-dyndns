from requests import post,get
from dotenv import load_dotenv
from os import getenv

load_dotenv()

secretapikey = getenv('secretapikey')
apikey = getenv('apikey')
domain = getenv('domain')


myip = get("http://ipinfo.io/ip").text

print(f"My external IP is: {myip}")

print(f"Checking if the domain {domain} is currently set to {myip}")

current_record_config = post(f"https://api.porkbun.com/api/json/v3/dns/retrieveByNameType/{domain}/A",json={"secretapikey":secretapikey, "apikey":apikey}).json()
current_record_ip = current_record_config.get("records")[0].get("content")

print(f"currently {domain} is set to {current_record_ip}")

if myip not in current_record_ip:
    print("Detected that current configuration is not correct; Attempting to update current configuration")

    post(f"https://api.porkbun.com/api/json/v3/dns/editByNameType/{domain}/A", json={"secretapikey":secretapikey, "apikey":apikey, "content": myip})

    print("Configuration updated.")