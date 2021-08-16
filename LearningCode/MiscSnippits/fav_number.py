import json
def get_fav_color():
    c = input('enter favorite color:')
    return c


def report_color():
    c=""
    try:
        with open('favcolor.json', 'r')  as f:
            c = json.load(f)
            print(f"favorite color is {c}")    
    except FileNotFoundError:
         pass
    return c

# main
fav = report_color()
if fav == "":
    c = get_fav_color()
    try:
        with open('favcolor.json', 'w') as f:
            json.dump(c, f)
    except FileNotFoundError:
         pass