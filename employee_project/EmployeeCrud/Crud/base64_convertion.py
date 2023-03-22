import base64
import requests


def get_as_base64(url):

    return base64.b64encode(requests.get(url).content)

# print(get_as_base64('https://thepersonage.com/wp-content/uploads/2020/07/Pawan-Kalyan-Image.jpg'))