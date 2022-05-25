# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# from curses import newwin


# from curses import newwin


# from curses import newwin


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
    line = text.strip().lower().split(" ")
    for newWord in line: 
        if newWord in d:
            d[newWord] = d[newWord] + 1
        else:
                d[newWord] = 1   
    return d

print(count_words('story'))