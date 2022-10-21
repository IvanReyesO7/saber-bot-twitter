import requests

class TwitterBot:
    def __init__(self, peopleIWantToAnnoy, message):
        self.peopleIWantToAnnoy = peopleIWantToAnnoy
        self.message = message


    def send_message(self):
        headers = {
            'Authorization': 'OAuth oauth_consumer_key="",oauth_token="",oauth_signature_method="HMAC-SHA1",oauth_timestamp="",oauth_nonce="",oauth_version="1.0",oauth_signature=""',
            'Content-Type': 'application/json',
        }
        json_data = {
            'text': f'{" ".join(self.peopleIWantToAnnoy)} {self.message}',
        }
        print(json_data)
        response = requests.post('https://api.twitter.com/2/tweets', headers=headers, json=json_data)
        print(response)

