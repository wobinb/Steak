#!/usr/bin/python

from requests_oauthlib import OAuth1Session

client_key = 'GJQWG7G3CLAEYTQELURYAFEFFQDMWK'
client_secret = 'RKAJB1GFUBZFACOFYMDGU2PGFCRXU3'

request_token_url = 'https://api.xero.com/oauth/RequestToken'

oauth = OAuth1Session(client_key, client_secret=client_secret)

fetch_response = oauth.fetch_request_token(request_token_url)

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

print(resource_owner_key)
print(resource_owner_secret)

base_authorization_url = 'https://api.xero.com/oauth/Authorize'

authorization_url = oauth.authorization_url(base_authorization_url)
print ('Please go here and authorize,', authorization_url)

print ("Hello, Python!")
