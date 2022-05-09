class Account(object):
    def __init__(self, json):
        self.href = json['links'][0]['href']
        self.validity = json['validity']
        self.uuid = json['uuid']
        self.username = json['username']
        self.displayName = json['displayName']
        self.lastActive = json['lastActive']
        self.active = json['active']
        self.reregistrationRequired = json['reregistrationRequired']
        self.validInDirectory = json['validInDirectory']
        self.canRequestGroups = json['canRequestGroups']
        self.tokenPasswordEnabled = json['tokenPasswordEnabled']
        self.keyHubPasswordChangeRequired = json['keyHubPasswordChangeRequired']
        self.directoryPasswordChangeRequired = json['directoryPasswordChangeRequired']
        self.licenseRole = json['licenseRole']


class KeyHubAccount(object):
    def __init__(self, authentication):
        self._session = authentication.session
        self._uri = authentication.uri
    
    def get_account_record(self, account_uuid = False, account_username = False):
        if account_uuid:
            response = self._session.get(self._uri + "/keyhub/rest/v1/account?uuid=" + account_uuid)
        elif account_username:
            response = self._session.get(self._uri + "/keyhub/rest/v1/account?username=" + account_username)
        else:
            raise Exception('one of the following variables must be defined: account_uuid or account_username')
        return Account(response.json()['items'][0])

def account(authentication):
    return KeyHubAccount(authentication=authentication)

