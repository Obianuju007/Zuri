# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


from audioop import reverse


def find_anagrams(x):
    # [assignment] Add your code here
    if (x[::-1] == x):
        print('True')
    else:
        print('False')
    return x
    


find_anagrams('racecar')
find_anagrams('mallam')
find_anagrams('house')