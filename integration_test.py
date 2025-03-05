from ekacare import EkaCareClient
from io import BytesIO
import json

client_id='<Your ID>'
txn_id = 'test-transaction-id-9'
extra_data = {'mode':'dictation'}
action = 'ekascribe'
audio_files = [
    '/Users/Vikalp/Downloads/recording_PT85312001.mp3'
]
client = EkaCareClient(
	client_id=client_id,
	client_secret='<Your Secret>'
)
response = client.files.upload(
    file_paths=audio_files,
    txn_id=txn_id,
    action=action,
    extra_data=extra_data
)
