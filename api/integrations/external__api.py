

import requests


class ExternalAPiCall():
    def __init__(self, url, headers, params):
        self.url = None
        self.headers = None
        self.params = None

    def get(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response

    def post(self, data):
        response = requests.post(self.url, headers=self.headers, params=self.params, data=data)
        return response

    def put(self, data):
        response = requests.put(self.url, headers=self.headers, params=self.params, data=data)
        return response

    def delete(self):
        response = requests.delete(self.url, headers=self.headers, params=self.params)
        return response