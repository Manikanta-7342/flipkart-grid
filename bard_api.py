from bardapi import Bard
from PIL import Image

# creating a image object

"""
img_url = r'C:Users\manik\Downloadsflowchart.png'
with open(img_url, "rb") as image:
  f = image.read()
  b = bytearray(f)

token = 'ZwivMJybAIBnD9Rac-NsPx3_q1rsRLV1Sj4YfbJ9c5c0PafMtmOAjo0jHJkUG7Oq9o051A.'
bard = Bard(token=token)
print(bard.ask_about_image("what is this image describes",b)['content'])
"""

# token = 'ZwivMJybAIBnD9Rac-NsPx3_q1rsRLV1Sj4YfbJ9c5c0PafMtmOAjo0jHJkUG7Oq9o051A.'
# bard = Bard(token=token)
# print(bard.get_answer("Diwali outfit for a women of age 25")['content'])

# from bardapi import Bard,ChatBard
# token = 'aAivMKCNwgcd3Zw_A9qZXH_jGbhL0pb3AXRYK4wbg7FbfAx9j4CwtTwGCLf4tnk5iTOf2w.'
# bard = Bard(token=token)
# res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
# print(res['links']) # Get image links (list)
# print(res['images']) # Get images (set)
# chat = ChatBard()
# chat.start(prompt="What is your name?")

# from bardapi import Bard,ChatBard
# import os
# import requests
# os.environ['_BARD_API_KEY'] = 'aAivMIuoF2CSnKufZt1sY66FfN0dcVxlPjqw6kOXfA2Q44glKErO27KlfLoK30G-cGY0JA.'
# token='aAivMIuoF2CSnKufZt1sY66FfN0dcVxlPjqw6kOXfA2Q44glKErO27KlfLoK30G-cGY0JA.'
#
# session = requests.Session()
# session.headers = {
#             "Host": "bard.google.com",
#             "X-Same-Domain": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#             "Origin": "https://bard.google.com",
#             "Referer": "https://bard.google.com/",
#         }
# session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))
# # session.cookies.set("__Secure-1PSID", token)
# #conversation_id = c_42b2627f2011351e
# bard = Bard(token=token, session=session, timeout=30)
# print(bard.get_answer("trending outfit")['links'])

# Continued conversation without set new session


# chat = ChatBard()
# chat.start(prompt="What is your name?")


import requests
from bardapi.constants import SESSION_HEADERS
import bardapi
from bardapi import ChatBard
import json
import os

def load_cookie(element_name):
    with open(os.getcwd() + "/" + "bard.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:
                if item.get("name") == element_name:
                    return item.get("value")
        return None

_1PSID = load_cookie("__Secure-1PSID")
_1PSIDTS = load_cookie("__Secure-1PSIDTS")
_1PSIDCC = load_cookie("__Secure-1PSIDCC")
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", _1PSID)
session.cookies.set("__Secure-1PSIDTS", _1PSIDTS)
session.cookies.set("__Secure-1PSIDCC", _1PSIDCC)

#bard = bardapi.core.Bard(token=_1PSID, session=session)
chat_bard = ChatBard(token=_1PSID,session=session)
# with open("data.txt", "w") as f:
#     f.write(str(bard.get_answer("what is a session and timeout?")))
#url = bard.export_conversation(bard.get_answer("what is a session and timeout?"))
print(chat_bard.display_chat_history())