import requests
from requests.auth import HTTPBasicAuth

sandbox_acc = 'sb-jostg25329699@business.example.com'
access_token = 'access_token$sandbox$b3znspjd5cvcgkt3$244637985979ef49a552e6f85e0ecd37'

client_id = 'Ad6BvU1rkjbgpzR0INMkYfr6tRUGD6q6RQROszedMndj_b_R9dErZatQiKu79XjOVB6UQGivGd1MqECZ'
secret_key = 'EKHkuuDQrg2ti7S_3YseDa_EAI3x7N6myua5F1VtICd4SMHUFWbmvA2Q_IegPehXl0vSKVTsMf8Puz-3'

access_token_from_postman = "A21AAKSAz0ApCU469OgTZn4QR4GlENRJ4_tiF40l1dIqpDrNBJcfQssFuuaOfN2IJv2LWov-LB9XX7sRcZVQ9s--zIJcESO4A"

auth = HTTPBasicAuth(client_id, secret_key)


class PayPalService:
    def __init__(self):
        self.url = 'https://api-m.sandbox.paypal.com/'
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token_from_postman}",
        }

    def generate_token(self):
        url = f'{self.url + "v1/oauth2/token"}'
        data = {"grant_type": "client_credentials"}
        headers = {"Accept": "application/json", "Accept-Language": "en_US"}
        response = requests.post(url, auth=(client_id, secret_key), data=data, headers=headers)
        return response.json()

    def make_payment(self, user_card):
        url = f'{self.url + "v1/payments/payment"}'
        pass


if __name__ == '__main__':
    paypal = PayPalService()
    token = paypal.generate_token()
    print(token['access_token'])
