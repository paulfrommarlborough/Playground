print('ODD')
odd_numbers = list(range(1, 100, 2))
print (odd_numbers)

print("SQUARES")
squares = [ value **2 for value in range(1,100)]
print (squares)

print("CUBES")
cubes = [ value ** 3 for value in range (1, 100)]
#for i in range(1,10):
#    print(cubes[i])
#cubes.append(12)
cubes.sort(reverse=True)
print (cubes[1:10])


intervals = [val for val in range(0,1440)]
print(intervals)