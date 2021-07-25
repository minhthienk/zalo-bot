import requests
import json
from preprocessing import Grammar

class Zalo(object):
    """docstring for Zalo"""
    def __init__(self):
        self.headers = {
            'authority': 'openapi.zalo.me',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'content-type': 'text/plain;charset=UTF-8',
            'accept': '*/*',
            'sec-gpc': '1',
            'origin': 'https://developers.zalo.me',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://developers.zalo.me/',
            'accept-language': 'en-US,en;q=0.9',
        }
        self.access_token = 'bMlFE0q_v32HOCe-2ZNdDPLWppuC8ff6bXYqJNO_pYMkDUTpJs6kDgj-vq56M9SqemJoV7yAe7QcFl87PsQCSOOomnXM5kjCgYkc0t9_p0YnTRXHQI7WEOe_oMbnOendjJZUD7e4XMAMFCfhIMM83RGyzWfmQTq7dtoASrbPzJx1PQnUE4Bx1C1ntqewQRKymppXO0idp3V70kXwB0d4A_0BYtOq4wOR-oZh5nelnKdu1ByR6ZtiHS4di1GSEknO-W6qFJOVc6Jw0y0G5rxeTzH5Z74GPzqusaUMQgbi7JyFAUOs'
    

    def get_followers(self):
        params = (
            ('data', '{"offset":0,"count":50}'),
            ('access_token', self.access_token),
        )
        response = requests.get('https://openapi.zalo.me/v2.0/oa/getfollowers', 
            headers=self.headers, params=params)
        print(response.text)


    def get_profile(self, user_id):
        params = (
            ('data', '{{"user_id":"{}"}}'.format(user_id)),
            ('access_token', self.access_token),
        )

        response = requests.get('https://openapi.zalo.me/v2.0/oa/getprofile', 
            headers=self.headers, params=params)
        print(response.text)


    def message(self, user_id, text):
        params = (('access_token', self.access_token),)
        data = {}
        data['recipient'] = {"user_id":"{}".format(user_id)}
        data['message'] = {"text":"{}".format(text)}
        data = json.dumps(data)
        response = requests.post('https://openapi.zalo.me/v2.0/oa/message', 
            headers=self.headers, params=params, data=data)
        print(response.text)



zalo = Zalo()
user_id_list = ['1927785561028610281']

user_id = '1927785561028610281'
text = 'This is automatic message'
zalo.message(user_id=user_id, text=text)
