import urlparse

import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

def get_request_token():
  """ Get a token allowing us to request user authorization"""
  oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
  response = requests.post(REQUEST_TOKEN_URL, auth=oauth)
  credentials = urlparse.parse_qs(response.content)
  
  request_token = credentials.get("oauth_token")[0]
  request_secret = credentials.get("oauth_token_secret")[0]
  return request_token, request_secret

def authorize():
  """ A complete OAuth authentication flow"""
  request_token, request_secret = get_request_token()
  verifier = get_user_authorization(request_token)
  
  
def get_user_authorization(request_token):
  """
  Redirect the user to authorize the client, ang get them to give us the verification code.
  """
  authorize_url = AUTHORIZE_URL
  authorize_url = authorize_url.format(request_token=request_token)
  print "Please go here and authorize: " + authorize_url
  return raw_input("Please input the verifier: ")