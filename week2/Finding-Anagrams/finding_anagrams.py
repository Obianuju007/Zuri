# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# from audioop import reverse
# from ssl import Options


print('What function do you want to perform? \n(a) finding anagrams \n(b) Checking Palindrome')
selection = input('Option: ')


def finding_anagrams():
    a_list = list(input('What is the first word: '))
    b_list = list(input('What is the second word: '))
    if (a_list.sort() == b_list.sort()):
        print('True, both words are anagrams 🎉')
    else:
        print('False, not anagrams 🚩')

def is_palindrome():
    # [assignment] Add your code here
    x = input('What\'s the word: ')
    if (x[::-1] == x):
        print('True, a palindrome 🎉')
    else:
        print('False, not a palindrome 🚩')
    
if selection == 'a': 
    print(finding_anagrams())
elif selection == 'b':
    print(is_palindrome())
else:
    print('You didn\'t make a valid selection')



# is_palindrome('racecar')
# is_palindrome('mallam')
# is_palindrome('house')
# xxx = ['stop']
# yyy = ['tops']
# isAnagram(xxx,yyy)