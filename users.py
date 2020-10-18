
unconfirmed_users = ['alice', 'bob', 'charles', 'betty', 'jim', 'jason']
confirmed_users = []

while unconfirmed_users:
    cuser = unconfirmed_users.pop()
    print(f"verify {cuser.title()}")
    confirmed_users.append(cuser)


print(f'confirmed users = {confirmed_users} ')