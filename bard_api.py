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

token = 'ZwivMJybAIBnD9Rac-NsPx3_q1rsRLV1Sj4YfbJ9c5c0PafMtmOAjo0jHJkUG7Oq9o051A.'
bard = Bard(token=token)
print(bard.get_answer("Diwali outfit for a women of age 25")['content'])