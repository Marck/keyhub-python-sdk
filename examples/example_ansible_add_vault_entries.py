#!/usr/bin/python
import keyhub
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: add_vault_entries

short_description: Add one or more vault entries into one or more KeyHub vault(s) using a KeyHub application

version_added: "1.0"

description:
    - "Use this module to add one or more vault entries into one or more KeyHub vault(s) using a KeyHub application"

options:
    keyhub_url:
        description:
            - The KeyHub URL
        type: str
        required: true
    keyhub_client_id:
        description:
            - The KeyHub application client ID used to connect to the API
        type: str
        required: true
    keyhub_client_secret:
        description:
            - The KeyHub application client secret used to connect to the API
        type: str
        required: true
    keyhub_group_uuid:
        description:
            - The UUID of the KeyHub group that has a vault
        type: str
        required: true
    name:
        description:
            - The name of the vault entry
        type: str
        required: true
    username:
        description:
            - The username you want to add to the vault. This is by default empty.
        type: str
        required: false
    password:
        description:
            - The password you want to add to the vault. This is by default empty.
        type: str
        required: false
    url:
        description:
            - The url of the vault entry. This is by default empty.
        type: str
        required: false
    comment:
        description:
            - The comment of the vault entry. This is by default empty.
        type: str
        required: false
    file:
        description:
            - The base64 encoded file of the vault entry. This is by default empty.
        type: str
        required: false
    filename:
        description:
            - The filename of the vault entry. This is by default empty.
        type: str
        required: false
    color:
        description:
            - The color of the vault entry. This is by default 'NONE'. Available options: PINK_LAVENDER, RED, ANDROID_GREEN, DARK, NONE, BLUE, SAGE, ARTICHOKE, CRIMSON_RED, GREEN, MIDDLE_YELLOW
        type: str
        required: false
    endDate:
        description:
            - The endDate of the vault entry. This is by default empty.
        type: str
        required: true
    warningPeriod:
        description:
            - The warningPeriod of the vault entry. This is by default 'NEVER'. Available options: AT_EXPIRATION, TWO_WEEKS, ONE_MONTH, TWO_MONTHS, THREE_MONTHS, SIX_MONTHS, NEVER
        type: str
        required: true

author:
    - Marck
'''

EXAMPLES = '''
add_vault_entries:
    keyhub_url: "https://my-keyhub-instance"
    keyhub_client_id: 12a3456b-a12b-a12b-a12b-12a3456bc789
    keyhub_client_secret: 12a3456b-a12b-a12b-a12b-12a3456bc789
    keyhub_group_uuid: 12a3456b-a12b-a12b-a12b-12a3456bc789
    name: "Example record"
    username: my-username
    password: super-secure-password123
    url: "https://my-website.org"
    comment: "This is an example record, nothing special"
    file: "V293LCBkaWQgeW91IGFjdHVhbGx5IGRlY29kZSB0aGlzPw=="
    filename: "testfile.png"
    color: "PINK_LAVENDER"
    endDate: "2023-05-25"
    warningPeriod: "ONE_MONTH"
'''

RETURN = '''
additionalObjects:
    description: the added entry is returned at success.
    type: str
uuid:
    description: the UUID of the added entry.
    type: str
'''

def keyhub_vault():
    try:
        # Define available arguments/parameters that a user can pass to the module
        module_args = dict(
            keyhub_url=dict(type='str', required=True),
            keyhub_client_id=dict(type='str', required=True, no_log=True),
            keyhub_client_secret=dict(type='str', required=True, no_log=True),
            keyhub_group_uuid=dict(type='str', required=True),
            name=dict(type='str', required=True),
            username=dict(type='str', required=False, default=None),
            password=dict(type='str', required=False, no_log=True),
            url=dict(type='str', required=False, default=None),
            comment=dict(type='str', required=False),
            file=dict(type='str', required=False),
            filename=dict(type='str', required=False),
            color=dict(type='str', required=False, default='NONE'),
            endDate=dict(type='str', required=False, default=None),
            warningPeriod=dict(type='str', required=False, default='NEVER'),
        )

        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )

        keyhub_client_auth = keyhub.client_auth(uri=module.params['keyhub_url'], client_id=module.params['keyhub_client_id'], client_secret=module.params['keyhub_client_secret'])
        keyhub_vault = keyhub.vault(authentication=keyhub_client_auth)

        entry_definition = {
            'items': [
                {
                "$type": "vault.VaultRecord",
                'additionalObjects': {
                    'secret': {
                        '$type': 'vault.VaultRecordSecrets',
                        'password': module.params['password'],
                        "comment": module.params['comment'],
                        "file": module.params['file']
                    }
                },
                'name': module.params['name'], 
                'username': module.params['username'], 
                'filename': module.params['filename'], 
                'color': module.params['color'], # PINK_LAVENDER, RED, ANDROID_GREEN, DARK, NONE, BLUE, SAGE, ARTICHOKE, CRIMSON_RED, GREEN, MIDDLE_YELLOW
                'url': module.params['url'],
                'endDate': module.params['endDate'],
                'warningPeriod': module.params['warningPeriod'] # AT_EXPIRATION, TWO_WEEKS, ONE_MONTH, TWO_MONTHS, THREE_MONTHS, SIX_MONTHS, NEVER
                }
            ]
        }
        post_vault_record = keyhub_vault.post_vault_record(group_uuid=module.params['keyhub_group_uuid'], payload=entry_definition)
        
        result = { 'changed': 'True', 'uuid': post_vault_record.uuid, 'additionalObjects': post_vault_record.additionalObjects }
        module.exit_json(**result)

    except Exception as error:
        module.fail_json(msg=f'Error on trying to add entry to KeyHub vault. Error: {error}')


def main():
    keyhub_vault()


if __name__ == '__main__':
    main()
