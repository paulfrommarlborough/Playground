rivers = { 'colorado':  'usa',
          'nile': 'egypt',
          'mississippi': 'usa',
          'tiber': 'italy'
}

print(rivers)

print(rivers.keys())

print(set(rivers.values()))

print(f"-------------------------------")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages)


poll_takers = [ 'joe', 'john', 'sarah', 'phil', 'paul']

for name in poll_takers:
    if name in favorite_languages.keys():
        print(f"{name} took the poll, fav language is {favorite_languages.get(name)}")
    else:
        print(f"{name}  needs to poll!")


# print(poll_takers)