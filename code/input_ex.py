""" input_ex.py: input test  """
numberlist = []
done = 0
while done == 0:
    x = input("enter number [q]: ")
    if x != 'q':
        try:
            nx = int(x)
        except ValueError:
            pass
        else:    
            numberlist.append(nx)
    else:
         done=1    
sum=0
for n in numberlist:
    sum += n
print(f"sum = {sum}")