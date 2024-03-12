from pickle import dump

# Fill each variable with your details

secretapikey = ""
apikey = ""
id = ""
domain = ""

with open('variables', 'wb') as f:
    dump([secretapikey, apikey, id, domain], f)
