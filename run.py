from sys import argv
from AutoShareFacebook import AutoShare

script, post_url = argv
#can access variable post_url
caption_text = raw_input("Type the caption here: ")

auto = AutoShare()

auto.auth(uname='', passd='')
auto.process(post_url=post_url, caption_text=caption_text)





