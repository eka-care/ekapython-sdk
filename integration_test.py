from ekacare import EkaCareClient
from io import BytesIO
import json

client_id='EC_174022407354131'
txn_id = 'test-transaction-id-9'
extra_data = {'mode':'dictation'}
action = 'ekascribe'
json_filepath = f'/Users/Vikalp/Downloads/{txn_id}.json'
audio_files = [
    '/Users/Vikalp/Downloads/recording_PT85312001.mp3'
]

client = EkaCareClient(
	client_id=client_id,
	client_secret='32d471f4-f0b9-4a6e-a4ba-1f22ad1a94c9'
)

response = client.files.upload(
    file_paths=audio_files,
    txn_id=txn_id,
    action=action,
    extra_data=extra_data
)