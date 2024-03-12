# porkbun dyndns
Used for updating a DNS record on porkbun.com in case the servers external IP changed (similar to dynamic DNS)

# How to use:
* You can create a virtual environment before installing the packages with "python -m venv .venv" for full details visit https://docs.python.org/3/library/venv.html
1. pip install -r requirements.txt
2. Using the update_variables.py update your variables with the api key and the domain you want to keep track of (to get api key go to https://porkbun.com/account/api)
3. run the update_dns.py, and you're done!

The update_dns.py can be triggered using cron job or when a monitoring system detects a problem with connectivity to the server.
