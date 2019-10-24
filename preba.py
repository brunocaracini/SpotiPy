email = '@gmail.com'
if (email.find('@gmail.com') != -1) or (email.find('@hotmail.com') != -1):
    if email.find('@') < 3 or len(email) > 30:
        print(False)
    else:
        print(True)
else:
    print(False)

