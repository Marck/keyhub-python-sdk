from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests

class KeyHubClientAuthentication(object):
    def __init__(self, uri, client_id, client_secret):
        self.uri = uri

        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=uri+'/login/oauth2/token?authVault=access', client_id=client_id, client_secret=client_secret)

        session = OAuth2Session(client_id, token=token)
        session.headers.update({'Accept': 'application/vnd.topicus.keyhub+json;version=latest'})
        session.headers.update({'topicus-Vault-session': token['vaultSession']})
        self.session = session
    
    def info(self):
        # TODO: return info object instead of json
        response = self.session.get(self.uri + "/keyhub/rest/v1/info")
        return response.json()

    def docs(self):
        response = requests.get(self.uri + "/keyhub/rest/v1/openapi.json")
        return response.json()

class KeyHubAccountAuthentication(object):
    def __init__(self, uri):
        self.uri = uri
        # Add proper authentication using your browser (or other way for that matter)
        return print('here comes auth for personal use')
        pass

def client_auth(uri, client_id, client_secret):
    return KeyHubClientAuthentication(uri=uri, client_id=client_id, client_secret=client_secret)

def account_auth(uri):
    return KeyHubAccountAuthentication(uri=uri)
