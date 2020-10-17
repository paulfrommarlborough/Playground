# exerises for lists and dictonaries

p0 = { 'username': 'paul',
           'first':  'paul',
           'last':   'douglas',
           'favs':   ['c', 'c++', 'python']
}
p1 = { 'username': 'joe',
           'first':  'joe',
           'last':   'doe',
           'favs':   ['java']
}
p2 = { 'username': 'sally',
            'first':  'sally',
            'last':   'doe',
            'favs':   ['javascript', 'php']

}

people = [ p0, p1, p2]

print(people)


print('----------------------------')
for px in people[:2]:
    print (px['favs'])

print('NESTED----------------------------')

# nested
users = { 
    'douglas': {
        'first': 'paul',
        'last': 'douglas',
        'favs': ['c', 'c++', 'python']
    },
    'sdoe': {
            'first':  'sally',
            'last':   'doe',
            'favs':   ['javascript', 'php']
    },
    'jdoe': {
            'first':  'joe',
            'last':   'doe',
            'favs':   ['java']
    }
}

print('-------------------------')
print('USERS-------------------')
for uname, userinfo in users.items():
    print(userinfo['favs'])