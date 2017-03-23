import Instagram_auto_liker

import Instagram_Auto_Tag_Liker

from sys import argv

#script, post_url = argv


print "Login Details \n"
uid = raw_input('Username :')
passd = raw_input('Password : ')


caption_text_2 = ''
choice = 0
print "\n\n WARNING: This project is currently not stable (Beta Version)."

print 'Press 1 to like posts of the people you follow on Instagram'
print 'Press 2 to like posts of a specific tag on Instagram'

choice = int(raw_input('Input: '))



if choice==1:
    print "You may run this once in a while, because it may start unliking the posts back if ran twice within a short period of time :)"
    n = raw_input("Number of posts:")
    try:
        init = Instagram_auto_liker.main(uid, passd,n)
    except:
        print"Err Check Values"

elif choice==2:
    tag = raw_input('Enter the tag name :')
    n = raw_input("Number of posts (if you enter 10, it means 10*3):")

    try:
        init = Instagram_Auto_Tag_Liker.main(uid, passd,tag,n)
    except:
        print"Err Check Values"

else: pass