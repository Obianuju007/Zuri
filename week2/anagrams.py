def isAnagram(a, b):
    a_list = list(a)
    b_list = list(b)
    if (a_list.sort() == b_list.sort()):
        print('True')
    else:
        print('False')

xxx = ['stop']
yyy = ['tops']
isAnagram(xxx,yyy)