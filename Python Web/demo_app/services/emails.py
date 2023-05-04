import requests

secret_key = 'md-Plmk6B0jpHjqYRj2xL73TA'


class EmailService:
    def __init__(self):
        self.url = 'https://mandrillapp.com/'
        self.headers = {
            'Content-Type': 'application/json',
        }

    def test(self):
        url = f"{self.url + 'api/1.0/users/ping'}"
        body = {
            "key": f"{secret_key}"
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()

    def send_simple_mail(self):
        url = f'{self.url + "api/1.0/messages/send"}'
        body = '{"key": "$YOUR_API_KEY", "message": {"from_email": "hello@example.com", "subject": "Hello World", "text": "Welcome to Mailchimp Transactional!", ' \
               '"to": [{ "email": "zyoshi123@gmail.com", "type": "to" }]}}'
        response = requests.post(url, json=body,headers=self.headers)
        return response


if __name__ == '__main__':
    emails = EmailService()
    result = emails.send_simple_mail()
    print(result)
