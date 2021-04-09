class resturant:
    def __init__(self, name, genre, capacity):
        self.name = name 
        self.genre = genre 
        self.capacity= capacity

    def order(self):
        print(f"ordering at {self.name}")

    def describe_resturant(self):
        print(f"restuarant name { self.name}")
        print(f"restuarant genre { self.genre}")
        print(f"restuarant genre { self.capacity}")
        

resturants = []

r = resturant ('joes', 'diner', 12)
resturants.append(r)

r = resturant('papa ginos', 'pizza', 52)
resturants.append(r)

r = resturant('wellys', 'american', 33)
resturants.append(r)

print("---------------------------------")
print('for loop...')
for r in resturants:
    r.describe_resturant()

print("---------------------------------")
print('for while...')

while resturants:
    r.describe_resturant()
    r = resturants.pop()