filename="pi_million_digits.txt"

with open(filename) as f:
    lines = f.readlines()
    
#for line in lines:
#    print(line.rstrip())

pi_val = ''
for line in lines:
    pi_val += line.strip()
    
print(f"pi str = {pi_val[:52]}")



birthday = input('enter birthday ')

if birthday in pi_val:
    print(f"birthday {birthday} IN PI")
else:
    print(f"birthday {birthday} NOT IN PI")
