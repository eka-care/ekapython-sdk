from ekacare import EkaCareClient
client = EkaCareClient(
	client_id='EC_174022407354131',
	client_secret='32d471f4-f0b9-4a6e-a4ba-1f22ad1a94c9'
)
response = client.files.upload(
    file_path='/Users/Vikalp/ekacare/eka-docs/api-reference/general-tools/file-upload/file-upload.yaml',
    txn_id='test-transaction-id',
    action='transcribe',
    extra_data={'mode':'dictation'}
)