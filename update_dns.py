from requests import post,get
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET_API_KEY = getenv('secretapikey')
API_KEY = getenv('apikey')
DOMAIN = getenv('domain')

API_BASE_URL = "https://api.porkbun.com/api/json/v3"
IP_CHECK_URL = "http://ipinfo.io/ip"


myip = get(IP_CHECK_URL).text.strip()

print(f"My external IP is: {myip}")

print(f"Checking if the domain {DOMAIN} is currently set to {myip}")

auth_payload = {
    "secretapikey": SECRET_API_KEY,
    "apikey": API_KEY
}

current_record_config = post(
    f"{API_BASE_URL}/dns/retrieveByNameType/{DOMAIN}/A",
    json=auth_payload
).json()

if "records" not in current_record_config:
    raise Exception("Failed to retrieve DNS records")

current_record_ip = current_record_config["records"][0]["content"]

print(f"currently {DOMAIN} is set to {current_record_ip}")

if myip != current_record_ip:
    print("Detected that current configuration is not correct; Attempting to update current configuration")

    update_payload = {**auth_payload, "content": myip}
    response = post(
            f"{API_BASE_URL}/dns/editByNameType/{DOMAIN}/A",
            json=update_payload
        )
    
    if response.status_code != 200:
        raise Exception("Failed to update DNS record")
    
    print("Configuration updated successfully.")