# from curses import newwin
import string


def read_file_content(filename):
    # [assignment] Add your code here 
    new_file = open(filename + '.txt', 'r')
    read_file = new_file.read()
    new_file.close()
    return read_file

d = dict()
def count_words(text):
    text = read_file_content(text)
    # [assignment] Add your code here
    char_punct = text.translate(str.maketrans('','', string.punctuation))
    line = char_punct.lower().split(" ")
    for newWord in line: 
        if newWord in d:
            d[newWord] = d[newWord] + 1
        else:
            d[newWord] = 1   
    return d

print(count_words('story'))
