# sentence = 'I love the idea that studying unlocks new levels of knowledge for me.'
# result = len(sentence.split())
# print("There are "+ str(result) +" words in the text")
print ('What function do you want to perform?')

def add(a, b):
    return(a+b)

def subtract(a, b):
    return(a-b)

def multiply(a, b):
    return(a*b)
    
def division(a, b):
    return(a/b)

def modulus(a, b): 
    return(a%b)

print(('a. Add'), ('b. Multiply'), ('c. Division'), ('d. Modulus'), ('e. Subtraction'))
selection = input('Please select option: ')

num_1 = int(input('What is the first number: '))
num_2 = int(input('What is the second number: '))

if selection == 'a':
    print(add(num_1,num_2))

elif selection == 'b':
    print(multiply(num_1,num_2))

elif selection == 'c':
    print(division(num_1,num_2))

elif selection == 'd':
    print(modulus(num_1,num_2))

elif selection == 'e':
    print(subtract(num_1,num_2))

else:
    print('You didn\'t make a valid selection....')