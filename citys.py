# dictionary test

citys = { 
    'boston':  { 'country': 'usa', 'population': 122123, 'density': 2},
    'new york': { 'country': 'usa', 'population': 9992123, 'density': 8},
}


print(citys)

for c, i in citys.items():
    print( f"{c} in {i['country']}  density {i['density']}")