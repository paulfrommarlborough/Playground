""" read excecption testing"""

def count_words(filename):
    flen=0
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
            pass
      #  print(f"File {filename} not found")
    else:
        words = contents.split()
        flen = len(words)
    finally:
        return flen

def count_word(filename, word):
    flen=0
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
            pass
      #  print(f"File {filename} not found")
    else:
        flen = contents.lower().count(word)
    finally:
        return flen



#=================
# main

filenames= ['C:\\develop\\alice.txt','C:\\develop\\alicse.txt','C:\\develop\\mask_of_red_death_Poe_1064-0.txt'] 
for filename in filenames:
    c = count_words(filename)
    if c > 0:
        print (f"File: {filename} has {c} words")


findword='the '
for filename in filenames:
    c = count_word(filename, findword)
    if c > 0:
        print (f"File: {filename} has {findword} count {c} words")

