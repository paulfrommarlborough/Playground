file_object  = open("pi_numbers.txt", "r")
content = file_object.read()
print(f"content = {content.rstrip()}")


with open('pi_numbers.txt') as f:
    c = f.read()
print(f"content = {c.rstrip()}")
