from pickle import dump

## fill out each variable with your details
secretapikey, apikey, id, domain = "","","",""

with open('variables', 'wb') as f:
    dump([secretapikey, apikey, id, domain], f)