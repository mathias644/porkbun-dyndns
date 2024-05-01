# porkbun dyndns
Used for updating a DNS record on porkbun.com in case the servers external IP changed

# How to use:
* You can create a virtual environment before installing the packages with "python -m venv .venv" for full details visit https://docs.python.org/3/library/venv.html
1. Install dependencies by running `pip install -r requirements.txt`
2. Create a file named .env or set your environment variables with "secretapikey" and "apikey" from Porkbun and "domain"
     the .env should look like:
   
       secretapikey=sk1_000000000000000
       apikey=pk1_000000000000000
       domain=example.com
4. Run `python retrieve_dns_id.py` to get the ID of the DNS record you want to update. Add this ID to your `.env` file with the following line `id=0000000`
5. Finally, run `python update_dns.py`. This script can be triggered using a cron job or when a monitoring system detects a problem with connectivity to the server.
