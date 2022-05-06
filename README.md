# keyhub-python-sdk

SDK for KeyHub written in Python

Python client for the Topicus KeyHub Vault API, supported under python 3 (only tested with 3.6).

Basic usage:

```python
    import keyhub

    keyhub_client = keyhub.client(uri='<your KeyHub uri>', client_id='<KeyHub application id>', client_secret='<KeyHub application secret>')

    print(keyhub_client.info())

    keyhub_client.get_group('<group uuid>')

    keyhub_client.get_vault_records('<group uuid>')

    keyhub_client.get_vault_record('<group uuid>', '<vault record uuid>')

    keyhub_client.get_account_record(account_uuid='<useraccount uuid>')

    keyhub_client.get_account_record(account_username='<useraccount username>')
```

> This repository is a cherry pick from the original authors repo: https://github.com/topicusonderwijs/keyhub-sdk and modified to fit some more specific needs
