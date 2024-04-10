from requests import post,get
from dotenv import load_dotenv
from os import getenv

load_dotenv()

secretapikey = getenv('secretapikey')
apikey = getenv('apikey')
domain = getenv('domain')

a_record_for_domain = post(f"https://porkbun.com/api/json/v3/dns/retrieveByNameType/{domain}/A/",json={"secretapikey":secretapikey, "apikey":apikey}).json()
id_of_a_record = a_record_for_domain.get("records")[0].get("id")

print(f"The ID for {domain} is {id_of_a_record}")