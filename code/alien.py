alien_colors = [ 'green', 'yellow', 'red']

ac = 'redx'

if ac ==  'green':
    print("5 points")
elif ac == 'yellow':
    print("10 points")
elif ac == 'red':    
    print("15 points")
else:
    print("-1 point")

    alien_0 = {}

    alien_0['color'] = 'green'
    alien_0['points'] = 5

    print(alien_0)


    alien_0['position_x'] = 0
    alien_0['position_y'] = 25
    alien_0['speed']='medium'

    print(alien_0)


    if alien_0['speed'] == 'slow':
        x_inc = 1
    elif alien_0['speed'] == 'medium':
        x_inc = 2
    else:
        x_inc = 3

    alien_0['position_x'] = alien_0['position_x'] + x_inc
    print(f"new postion: {alien_0['position_x']}")

    del alien_0['points']

    print(alien_0)


    cv = alien_0.get('color')

    print(cv)
    
#dictionary

person = {
    'first_name': 'paul',
    'last_name': 'dougas',
    'address': '29 fowler street',
    'city': 'marlborough',
    'state': 'MA',
    'zipcode': '01752',
 #   'fav_numbers': [2,3,44]
}
0
print(f"for keyvalue loop in items...")
for key,value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print(f"\nperson keys()")
for name in person.keys():
    print(name)

print(f"\nperson values()")
for name in set(person.values()):
    print(name)