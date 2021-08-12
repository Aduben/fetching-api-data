#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

#Option 1

a='Thirty'
b='Days'
c='of'
d='Python'
e= a+''+b+''+c+''+d
print(e)


#Option 2

Scattered_one = ('Thirty', 'Days', 'Of', 'Python')
concat_one=" ".join(Scattered_one)
print(concat_one)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

#Option 1

a='Code'
b='For'
c='All'
d= a+''+b+''+c
print(d)



#Option 2

Scattered_one = ('Coding','For','All')
concat_one=" ".join(Scattered_one)
print(concat_one)


#3. Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"

#4. Print the variable company using print().

company="Coding For All"
print(company)

#5. Print the length of the company string using len() method and print().

company="Coding For All"
print(len(company))

#6Change all the characters to uppercase letters using upper() method.
company="Coding For All"
print(company.upper())




#7 Change all the characters to lowercase letters using lower() method.

company="Coding For All"
print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

company="Coding For All"
print(company.capitalize())

print(company.title())

print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string.

company="Coding For All"
print(company[0:6])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.

company="Coding For All"
print(company.find('coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.
company="Coding For All"
company2=company.replace("coding","python")
print(company2)

#12 Change Python for Everyone to Python for All using the replace method or other methods.

original_script="Python For Everyone"
updated_script= original_script.replace("Everyone","All")
print(updated_script)

#13 Split the string 'Coding For All' using space as the separator (split()).

A ="Coding For All"
B=A.split()
print(B)

#13 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

A="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
B=A.split(",")
print(B)



#14 What is the character at index 0 in the string Coding For All.

A ="Coding For All"
B=A[0]
print(B)

#15 What is the last index of the string Coding For All.
A ="Coding For All"
B=A[-1]
print(B)

#16 What character is at index 10 in "Coding For All" string.
A ="Coding For All"
B=A[10]
print(B)

#17 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym_used ={"PFE":"Python For Everyone"}

#18 Create an acronym or an abbreviation for the name 'Coding For All'.

acronym_used ={"CFA":"Coding For All"}

#19 Use index to determine the position of the first occurrence of C in Coding For All.
A ="Coding For All"
B=A.find('C')
print(B)

#20 Use index to determine the position of the first occurrence of F in Coding For All.

A ="Coding For All"
B=A.find('F')
print(B)

#21 Use rfind to determine the position of the last occurrence of l in Coding For All People.

A ="Coding For All People"
B=A.rfind('l')
print(B)

#22 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

A='You cannot end a sentence with because because because is a conjunction'
B=A.find('because')
print(B)

#23 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

A='You cannot end a sentence with because because because is a conjunction'
B=A.rfind('because')
print(B)

#24 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

A='You cannot end a sentence with because because because is a conjunction'
B=A[33:-18]
print(B)

#25 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

A='You cannot end a sentence with because because because is a conjunction'
B=A.find('because')
print(B)

#26 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

A='You cannot end a sentence with because because because is a conjunction'
B=A[33:-18]
print(B)

#27 Does ''Coding For All' start with a substring Coding?
A="Coding For All"
B=A.startswith("Coding")
print(B)


#28Does 'Coding For All' end with a substring coding?

A="Coding For All"
B=A.endswith("Coding")
print(B)


#29 '   Coding For All      '  , remove the left and right trailing spaces in the given string.

A='   Coding For All      '
B=A.strip()
print(B)

#30 Which one of the following variables return True when we use the method isidentifier():
'''30DaysOfPython
thirty_days_of_python'''

A='30DaysOfPython'
C=A.isidentifier()
print(C) #False

B='thirty_days_of_python'
D=B.isidentifier()
print(D) #True


#31 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
A=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
B="#".join(A)
print(B)

#32 Use the new line escape sequence to separate the following sentences.

'''I am enjoying this challenge.
I just wonder what is next.'''

A='I am enjoying this challenge.\nI just wonder what is next.'
print(A)

#33 Use a tab escape sequence to write the following lines.

'''Name      Age     Country   City
Asabeneh  250     Finland   Helsinki'''

B='Name      Age     Country   City\tAsabeneh  250     Finland   Helsinki'
print(B)

#34 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2

#The area of a circle with radius 10 is 314 meters square.
print('The area of a circle with radius {} is {} meters square'.format(radius,area))


35# Make the following using string formatting methods:
'''8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''

a=8
b=6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

