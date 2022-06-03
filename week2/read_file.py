file = open('htmlarticle.txt', 'r')
d = dict()
for line in file:
    line = line.strip().lower().split(" ")
    # line = line.lower()
    # words = line
    for word in line:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
#for key in list(d.keys()):
    # print(key, ":", d[key])
    print(d)
