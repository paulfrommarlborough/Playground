# dictionary

pets = {
    'fluffy' : {
        'species': 'cat',
        'type': 'tabby',
        'age': '10',
        'color': 'brown',
        },
    'goliath' : {
        'species': 'dog',
        'type': 'great dane',
        'age': '1',
        'color': 'brindle',
        },
    'bill' : {
        'species': 'cat',
        'type': 'unknown',
        'age': '2',
        'color': 'orange',
        }
}


for name, info in pets.items():
    print (f"pet: {name} : {info['species']} is {info['age']}  years ")