import keyhub
import json

settings = json.load(open('creds.json', 'r'))

print('- Post vault record -')
payload = {
    'additionalObjects': {
        'secret': {
            '$type': 'vault.VaultRecordSecrets',
            'password': 'test2',
            "comment": "This is an example record, nothing special"
        }
    },
    'name': 'Python scripting test', 
    'username': 'test', 
    'color': 'green',
    'url': 'https://topicus-keyhub.com',
    'endDate': '2023-05-25',
    'warningPeriod': 'ONE_MONTH'
}
post_vault_record = keyhub_vault.post_vault_record(group_uuid=settings['vault_uuid'], payload=payload)
print(post_vault_record)
print('')