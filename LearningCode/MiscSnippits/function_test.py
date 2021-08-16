def describe(name='joe', type='dog'):
    print(f"Input Name {name}   Type { type} ")
    print(f"done describe.")

def make_shirt(shirtsize='large', message='I love python'):
    print(f"Custom Printing a shirt....")
    print(f"size will be {shirtsize} ")
    print(f"Shirt will say '{message}'' ")
    

print(f"main entry ...") 
describe("sammy", "cat")
describe("hobbes", "cat")
describe("barkley", "dog")

describe(name='harry', type='hamster')

make_shirt('small', "VOTE!!!")
#keyword arguments
make_shirt(shirtsize='medium', message="BLM")
make_shirt(shirtsize='medium')
