import datetime

myfood=['pizza', 'icecream', 'chicken', 'toast']

yourfood=['carrot', 'corn', 'tomato', 'potato']

print("my food")
print (myfood)
print("your food")
print (yourfood)

#friend_food = myfood[:]
friend_food = myfood
print ("friend food")
print (friend_food)

myfood.append('cookies')
friend_food.append('zucchini')

print("my food")
print (myfood)
print("your food")
print (yourfood)
print ("friend food")
print (friend_food)

msg = f"first 3 items {myfood[:3]} "
print (msg.title())

tlist = [ {'beer','budlite'}, {'beer','miller'}, {'wine','boogle'}]
print (tlist)

print(tlist[0])

print('tuple')
dim = (200,5)
print (dim[0])
print (dim[1])