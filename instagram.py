import time
import json
import requests
import urllib.parse

from helper import text_utils


class InstagramLogin:
    def __init__(self):
        self.login_url = "https://i.instagram.com/api/v1/accounts/login/"
        self.headers = {
            'User-Agent': 'Instagram 133.0.0.32.120 Android (26/8.0.0; 320dpi; 768x1184; Genymotion/Android; '
                          'android8; vbox86p; vbox86; en_US; 204019456)',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
        }

    def generate_cookie(self, username, password):
        session = requests.Session()
        date_time = round(time.time())
        signed_body = {
            "jazoest": "22569",
            "country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]",
            "phone_id": "4e3ff9b8-96b8-4dad-b11f-e6e2814ac31c",
            "enc_password": "#PWD_INSTAGRAM:0:{}:{}".format(date_time, password),
            "_csrftoken": "YgkknpCHmSIbjyPDDO9fSjMToTYfhLPp",
            "username": username,
            "adid": "ccc4a842-75ce-4591-b050-e64efca5a8ba",
            "guid": "a2a59119-4663-43c8-89b0-6dc719cd1f90",
            "device_id": "android-{}".format(text_utils.random_string(16)),
            "google_tokens": "[]",
            "password": password,
            "login_attempt_count": "0"
        }

        payload = "signed_body={}.{}&ig_sig_key_version=4".format(
            text_utils.random_string(32),
            urllib.parse.quote_plus(json.dumps(signed_body))
        )
        user_agent = {
          'User-Agent': 'Instagram 133.0.0.32.120 Android (26/8.0.0; 320dpi; 768x1184; Genymotion/Android; '
                        'android8; vbox86p; vbox86; en_US; 204019456)'
        }
        self.headers.update(user_agent)
        response = session.request("POST", self.login_url, headers=self.headers, data=payload)

        return response.json(), session.cookies.get_dict()

    def generate_bearer(self, username, password):
        bearer = None
        session = requests.Session()
        signed_body = {
            "jazoest": "22330",
            "country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]",
            "phone_id": "46be30f7-d473-4441-b7c9-37b86602eac6",
            "enc_password": "#PWD_INSTAGRAM:0:1650529925:{}".format(password),
            "username": username,
            "adid": "ccc4a842-75ce-4591-b050-e64efca5a8ba",
            "guid": "ff870086-8663-4062-8666-c1cc6a86e26a",
            "device_id": "android-{}".format(text_utils.random_string(16)),
            "google_tokens": "[]",
            "login_attempt_count": "0"
        }

        payload = "signed_body={}.{}&ig_sig_key_version=4".format(
            text_utils.random_string(32),
            urllib.parse.quote_plus(json.dumps(signed_body))
        )
        user_agent = {
            'User-Agent': 'Instagram 212.0.0.38.119 Android (26/8.0.0; 320dpi; 768x1184; Genymotion/Android; '
                          'android8; vbox86p; vbox86; en_US; 329675731)'
        }
        self.headers.update(user_agent)
        response = session.request("POST", self.login_url, headers=self.headers, data=payload)

        if 'ig-set-authorization' in response.headers:
            bearer = response.headers['ig-set-authorization']

        return response.json(), bearer
