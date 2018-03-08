#!/usr/bin/python

# Based  on the example for twitter API here
# http://requests-oauthlib.readthedocs.io/en/latest/oauth1_workflow.html


from requests_oauthlib import OAuth1Session

#set client keys
client_key = 'XXX'

with open("certs/privatekey.pem") as keyfile:
  private_key = keyfile.read()

print (private_key)

#make API call
protected_url = 'https://api.xero.com/api.xro/2.0/Organisation'
oauth = OAuth1Session(
	client_key,
	resource_owner_key=client_key,
	signature_method="RSA-SHA1",
	rsa_key=private_key)

r = oauth.get(protected_url)

print (r.content)
