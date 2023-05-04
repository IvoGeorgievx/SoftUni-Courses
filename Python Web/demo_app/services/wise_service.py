import uuid

import requests

key = '70e6f295-b1e9-4c24-a2b1-e098d77b4489'


class WiseService:
    def __init__(self):
        self.main_url = 'https://api.sandbox.transferwise.tech/'
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }
        self.profile_id = '16693348'

    def _get_profile_id(self):
        url = self.main_url + 'v2/profiles'
        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(url, json={}, headers=headers)
        return response.json()

    def create_quota(self, amount):
        url = self.main_url + f'/v3/profiles/{self.profile_id}/quotes'
        body = {
            "sourceCurrency": "EUR",
            "targetCurrency": "BGN",
            "sourceAmount": amount,
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()['id']

    def create_recipient_account(self, full_name, iban):
        url = self.main_url + 'v1/accounts'
        headers = self.headers
        body = {
            "currency": "BGN",
            "type": "IBAN",
            "profile": self.profile_id,
            "ownedByCustomer": False,
            "accountHolderName": full_name,
            "details": {
                "legalType": "PRIVATE",
                "iban": iban
            }}
        response = requests.post(url, json=body, headers=headers)
        return response.json()['id']

    def create_transfer(self, quota_id, recipient_id, custom_transaction_id):
        url = self.main_url + 'v1/transfers'
        body = {
            "targetAccount": recipient_id,
            "quoteUuid": quota_id,
            "customerTransactionId": custom_transaction_id,
            "details": {}
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()['id']

    def approve_transfer(self, transfer_id):
        url = self.main_url + f"v3/profiles/{self.profile_id}/transfers/{transfer_id}/payments"
        body = {"type": "BALANCE"}
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()

    def reject_transfer(self, transfer_id):
        url = self.main_url + f"v1/transfers/{transfer_id}/cancel"
        response = requests.put(url, json={}, headers=self.headers)
        return response.json()


if __name__ == '__main__':
    wise_service = WiseService()
    # quota_id = wise_service.create_quota(150)
    # recipient_id = wise_service.create_recipient_account("ivo test", 'BG68IORT80941459891118')
    # transaction_id = str(uuid.uuid4())
    # create_transfer = wise_service.create_transfer(quota_id, recipient_id, transaction_id)
    # approve_transfer = wise_service.approve_transfer(51785651)
    reject_transfer = wise_service.reject_transfer(51785638)
    print(reject_transfer)
