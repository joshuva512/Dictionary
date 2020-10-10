import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            f'''are you searching this : "{get_close_matches(w, data.keys())[0]}" Enter 'y' if YES or 'n' if NO  ''').upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "search other words"

    else:
        return "there is no word like this"


while True:
    get = input('''\nTo Exit enter : 1
                   Enter Word   ''')
    if get != "1":
        op = meaning(get)
        if type(op) == list:
            for pnt in op:
                print("\n * " + pnt)
        else:
            print("  * "+op)
        continue
    else:
        break



