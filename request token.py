#!/usr/bin/python

# Based  on the example for twitter API here
# http://requests-oauthlib.readthedocs.io/en/latest/oauth1_workflow.html


from requests_oauthlib import OAuth1Session

#Set client keys
client_key = 'GJQWG7G3CLAEYTQELURYAFEFFQDMWK'
client_secret = 'RKAJB1GFUBZFACOFYMDGU2PGFCRXU3'

#get request token
request_token_url = 'https://api.xero.com/oauth/RequestToken'
oauth = OAuth1Session(client_key, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

print(resource_owner_key)
print(resource_owner_secret)

#authorize
base_authorization_url = 'https://api.xero.com/oauth/Authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print ('Please go here and authorize,', authorization_url)
redirect_response = input('Paste the code here: ')

#get access token
access_token_url = 'https://api.xero.com/oauth/AccessToken'
oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=redirect_response)
oauth_tokens = oauth.fetch_access_token(access_token_url)
resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')

print(resource_owner_key)
print(resource_owner_secret)

#make API call
protected_url = 'https://api.xero.com/api.xro/2.0/Organisation'
oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)
r = oauth.get(protected_url)

print (r.content)
