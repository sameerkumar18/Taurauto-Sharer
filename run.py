from sys import argv
from AutoShareFacebook import AutoShare

script, post_url = argv
#can access variable post_url

auto = AutoShare()

auto.auth(uname='', passd='')
caption_text_2 = ''
choice = 0

choice = int(raw_input("Press 1 for One Line Caption or Press 2 for Two Line Caption"))

if choice==2:

    caption_text_1 = raw_input("Type the caption here for Line 1: ")
    caption_text_2 = raw_input("Type the caption here for Line 2: ")
    auto.process(post_url=post_url, caption_text_1=caption_text_1, caption_text_2=caption_text_2, choice=choice)

else:
    caption_text_1 = raw_input("Type the caption here: ")
    auto.process(post_url=post_url, caption_text_1=caption_text_1, caption_text_2=caption_text_2, choice=choice)





