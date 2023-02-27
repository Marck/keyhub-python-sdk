# keyhub-python-sdk

SDK for KeyHub written in Python

Python client for the Topicus KeyHub Vault API, supported under python 3 (only tested with 3.6).

## Basic usage

Create a *creds.json* file with the following format:

```json
{
    "url": "",
    "account_username": "",
    "vault_uuid": "",
    "client_id": "",
    "client_secret": ""
}
```

Create your Python script:

```python
    import keyhub
    import json

    settings = json.load(open('creds.json', 'r'))

    keyhub_client = keyhub.client(uri=settings['url'], client_id=settings['client_id'], client_secret=settings['client_secret'])

    print(keyhub_client.info())

    keyhub_client.get_group('<group uuid>')

    keyhub_client.get_vault_records('<group uuid>')

    keyhub_client.get_vault_record('<group uuid>', '<vault record uuid>')

    keyhub_client.get_account_record(account_uuid='<useraccount uuid>')

    keyhub_client.get_account_record(account_username='<useraccount username>')
```

## Examples

See the _examples_ folder for some examples.

> This repository is a cherry pick from the original authors repo [here](https://github.com/topicusonderwijs/keyhub-sdk) and modified to fit some more specific needs
