import requests

class Data:

    def __init__(self):
        self.r = requests.get("https://api.npoint.io/ea4f864e4916bafd3265/blog_posts/").json()
