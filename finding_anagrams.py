# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# from audioop import reverse

def isAnagram(a, b):
    a_list = list(a)
    b_list = list(b)
    if (a_list.sort() == b_list.sort()):
        print('True')
    else:
        print('False')

def is_palindrome(x):
    # [assignment] Add your code here
    if (x[::-1] == x):
        print('True')
    else:
        print('False')
    return x
    


is_palindrome('racecar')
is_palindrome('mallam')
is_palindrome('house')
xxx = ['stop']
yyy = ['tops']
isAnagram(xxx,yyy)
