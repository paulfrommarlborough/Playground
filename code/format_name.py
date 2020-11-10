def format_name(first_name, last_name):
    fullname = f"{first_name} {last_name}"
    return fullname.title()

def format_name1(first_name, last_name):
#    fullname = f"{first_name} {last_name}"
    person  = {'first' : {first_name},  'last': {last_name}}
    return person



me = format_name('paul','Douglas')
print(f" Me = {me}") 

me = format_name1('paul','Douglas')
print(f" Me = {me}")   