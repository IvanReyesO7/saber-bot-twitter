import requests

class TwitterBot:
    def __init__(self, peopleIWantToAnnoy, message):
        self.peopleIWantToAnnoy = peopleIWantToAnnoy
        self.message = message


    def send_message(self):
        headers = {
            'Authorization': f'OAuth oauth_consumer_key="{ENV[OATH_CONSUMER]}",oauth_token="{ENV[OATH_TOKEN]}",oauth_signature_method="HMAC-SHA1",oauth_timestamp="{ENV[TIMESTAMP]}",oauth_nonce="{ENV[OATH_NONCE]}",oauth_version="1.0",oauth_signature="{ENV[OATH_CONSUMER]}"',
            'Content-Type': 'application/json',
        }
        json_data = {
            'text': f'{" ".join(self.peopleIWantToAnnoy)} {self.message}',
        }
        print(json_data)
        response = requests.post('https://api.twitter.com/2/tweets', headers=headers, json=json_data)
        print(response)

