import requests
import os

class TwitterBot:
    def __init__(self, peopleIWantToAnnoy, message):
        self.peopleIWantToAnnoy = peopleIWantToAnnoy
        self.message = message


    def send_message(self):
        headers = {
            'Authorization': f'OAuth oauth_consumer_key="{os.environ["OATH_CONSUMER_KEY"]}",oauth_token="{os.environ["OATH_TOKEN"]}",oauth_signature_method="HMAC-SHA1",oauth_timestamp="{os.environ["TIMESTAMP"]}",oauth_nonce="{os.environ["OATH_NONCE"]}",oauth_version="1.0",oauth_signature="{os.environ["OATH_CONSUMER"]}"',
            'Content-Type': 'application/json',
        }
        json_data = {
            'text': f'{" ".join(self.peopleIWantToAnnoy)} {self.message}',
        }
        print(json_data)
        response = requests.post('https://api.twitter.com/2/tweets', headers=headers, json=json_data)
        print(response)

