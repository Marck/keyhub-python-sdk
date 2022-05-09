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

class Group(object):
    def __init__(self, json):
        self.uuid = json['uuid']
        self.name = json['name']
        self.href = json['links'][0]['href']

class VaultRecord(object):
    def __init__(self, json):
        self.uuid = json['uuid']
        self.name = json['name']
        self.color = json['color'] if 'color' in json else ''
        self.username = json['username'] if 'username' in json else ''
        self.url = json['url'] if 'url' in json else ''
        self.password = json['additionalObjects']['secret']['password'] if 'secret' in json['additionalObjects'] and 'password' in json['additionalObjects']['secret'] else ''
        self.totp = json['additionalObjects']['secret']['totp'] if 'secret' in json['additionalObjects'] and 'totp' in json['additionalObjects']['secret'] else ''
        self.filename = json['filename'] if 'filename' in json else ''
        self.file = json['additionalObjects']['secret']['file'] if 'secret' in json['additionalObjects'] and 'file' in json['additionalObjects']['secret'] else ''


class KeyHubProfile(object):
    def __init__(self, authentication):
        self._session = authentication.session
        self._uri = authentication.uri

  
    def get_temporary_password(self):
        return print('here comes temp pw functionality')
        # return Account(response.json()['items'][0])


def profile(authentication):
    return KeyHubProfile(authentication=authentication)

