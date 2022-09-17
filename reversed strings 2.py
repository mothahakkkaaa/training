def spin_words(sentence):

    a = sentence.split()
    x = []
    for i in a:
        if len (i) >= 5:
            x.append(i[:: -1])
        else:
            x.append(i)
    new = ' '.join(x)
    return new



a = "Coffee is quite hot"
print (spin_words(a))