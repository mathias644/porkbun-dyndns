# porkbun dyndns
Used for updating a DNS record on porkbun.com in case the servers external IP changed

# How to use:
* You can create a virtual environment before installing the packages with "python -m venv .venv" for full details visit https://docs.python.org/3/library/venv.html
1. pip install -r requirements.txt
2. Create a file named .env or set your environment variables with "secretapikey" and "apikey" from Porkbun and "domain"
     the .env should look like:
       secretapikey=sk1_000000000000000
       apikey=pk1_000000000000000
       domain=example.com
3. Run retrieve_dns_id.py to get the ID of the you will want to update, and add it to .env "id=00000000"
4. All that is left is to run update_dns.py, and you're done!

The update_dns.py can be triggered using cron job or when a monitoring system detects a problem with connectivity to the server.
