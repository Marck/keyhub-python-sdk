import keyhub
import json

settings = json.load(open('creds.json', 'r'))

# Authentication definitions
## Create authenticated session using a KeyHub application
keyhub_client_auth = keyhub.client_auth(uri=settings['url'], client_id=settings['client_id'], client_secret=settings['client_secret'])

# Definitions
keyhub_account = keyhub.account(authentication=keyhub_client_auth)
account_record_uuid = keyhub_account.get_account_records(account_uuid=settings['account_uuid'])
keyhub_vault = keyhub.vault(authentication=keyhub_client_auth)

print('--- Clients ---')
print('- Client info -')
keyhub_client = keyhub.client(authentication=keyhub_client_auth)
client_info = keyhub_client.get_client_info()
print(client_info.name)

print(keyhub_client.post_client_vault())

print('--- Accounts ---')
print('- Active/inactive accounts -')
accounts_in_state = keyhub_account.get_accounts_in_state(active=False)
for account in accounts_in_state:
    print(f'Name: {account.displayName}, Active: {account.active}')
print('')

print('- Account uuid and username -')
account_record_username = keyhub_account.get_account_records(account_username=settings['account_username'])
print(f'username: {settings["account_username"]}')
for account in account_record_username:
    print(f'account uuid based on only username: {account.uuid}')
    account_id = account.links[0]['id']

print('--- Vaults ---')
print('- Vault records -')
vault_records = keyhub_vault.get_vault_records(settings['vault_uuid'])
for entry in vault_records:
    print(entry.name)
print('')

print('- Get vault ID -')
vault_info = keyhub_vault.get_group(settings['vault_uuid'])
print(vault_info['id'])
print('')

print('- Post vault record -')
payload = {
    'items': [
        {
        "$type": "vault.VaultRecord",
        'additionalObjects': {
            'secret': {
                '$type': 'vault.VaultRecordSecrets',
                'password': 'test2',
                "comment": "This is an example record, nothing special",
                 "file": "V293LCBkaWQgeW91IGFjdHVhbGx5IGRlY29kZSB0aGlzPw=="
            }
        },
        'name': 'Python scripting test', 
        'username': 'test', 
        'color': 'NONE', # PINK_LAVENDER, RED, ANDROID_GREEN, DARK, NONE, BLUE, SAGE, ARTICHOKE, CRIMSON_RED, GREEN, MIDDLE_YELLOW
        'filename': "testfile.png",
        # 'url': '',
        # 'endDate': '2023-05-25',
        # 'warningPeriod': 'ONE_MONTH' # AT_EXPIRATION, TWO_WEEKS, ONE_MONTH, TWO_MONTHS, THREE_MONTHS, SIX_MONTHS, NEVER
        }
    ]
}
post_vault_record = keyhub_vault.post_vault_record(group_uuid=settings['vault_uuid'], payload=payload)
print(post_vault_record.links[0]['href'])
print('')
