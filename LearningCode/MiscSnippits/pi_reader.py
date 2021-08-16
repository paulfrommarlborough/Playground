""" file readers with pi """

filename="pi_numbers.txt"
filename1="pi_million_digits.txt"

file_object  = open(filename, "r")
content = file_object.read()
print(f"content = {content.rstrip()}")

print('read whole file')
with open(filename) as f:
    c = f.read()
print(f"content = {c.rstrip()}")

print('read by line')
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print('read by lines')
with open(filename1) as f:
    lines = f.readlines()
    
#for line in lines:
#    print(line.rstrip())

pi_val = ''
for line in lines:
    pi_val += line.strip()
    
print(f"pi str = {pi_val[:52]}")
print(f"pi length {len(pi_val)}")

FPI = float(pi_val)
print(f" float pi = {FPI}")
