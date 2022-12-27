# Section 8.2.1 snippets

f'{17.489:.2f}'

# Integers
f'{10:d}'

# Characters
f'{65:c} {97:c}'

# Strings
f'{"hello":s} {7}'

# Floating-Point and Decimal Values
from decimal import Decimal

f'{Decimal("10000000000000000000000000.0"):.3f}'

f'{Decimal("10000000000000000000000000.0"):.3e}'



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.1 Self Check snippets

# Exercise 3
print(f'{58:c}{45:c}{41:c}')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.2 snippets

f'[{27:10d}]'

f'[{3.5:10f}]'

f'[{"hello":10}]'

# Explicitly Specifying Left and Right Alignment in a Field 
f'[{27:<15d}]'

f'[{3.5:<15f}]'

f'[{"hello":>15}]'

# Centering a Value in a Field 
f'[{27:^7d}]'

f'[{3.5:^7f}]'

f'[{"hello":^7}]'


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.2 Self Check snippets

# Exercise 2
print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.3 snippets

# Formatting Positive Numbers with Signs
f'[{27:+10d}]'

f'[{27:+010d}]'

# Using a Space Where a + Sign Would Appear in a Positive Value
print(f'{27:d}\n{27: d}\n{-27: d}')

# Grouping Digits
f'{12345678:,d}'

f'{123456.78:,.2f}'



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.3 Self Check snippets

# Exercise 2
print(f'{10240.473:+10,.2f}\n{-3210.9521:+10,.2f}')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.4 snippets

# 8.2.4 String’s format Method
'{:.2f}'.format(17.489)

# Multiple Placeholders
'{} {}'.format('Amanda', 'Cyan')

# Referencing Arguments By Position Number
'{0} {0} {1}'.format('Happy', 'Birthday')

# Referencing Keyword Arguments
'{first} {last}'.format(first='Amanda', last='Gray')

'{last} {first}'.format(first='Amanda', last='Gray')



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.2.4 Self Check snippets

# Exercise 1
print('{:c} {:c} {:c}'.format(58, 45, 41))

print('[{0:>10}]\n[{0:^10}]\n[{0:<10}]'.format('Amanda'))

print('{:+10,.2f}\n{:+10,.2f}'.format(10240.473, -3210.9521))

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.3 snippets
s1 = 'happy'

s2 = 'birthday'

s1 += ' ' + s2

s1

symbol = '>'

symbol *= 5

symbol



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.3 Self Check snippets

# Exercise 1
name = 'Pam'

name += ' Black'

bar = '*'

bar *= len(name)

print(f'{bar}\n{name}\n{bar}')




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.4 snippets

# Removing Leading and Trailing Whitespace
sentence = '\t  \n  This is a test string. \t\t \n'

sentence.strip()

# Removing Leading Whitespace
sentence.lstrip()

# Removing Trailing Whitespace
sentence.rstrip()






##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.4 Self Check snippets

# Exercise 1
name = '     Margo Magenta     '

name.strip()

name.lstrip()

name.rstrip()




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.5 snippets

# Capitalizing Only a String’s First Character
'happy birthday'.capitalize()

# Capitalizing the First Character of Every Word in a String
'strings: a deeper look'.title()




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.5 Self Check snippets

# Exercise 1
test_string = 'happy new year'

test_string.capitalize()

test_string.title()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.6 snippets
 
print(f'A: {ord("A")}; a: {ord("a")}')

'Orange' == 'orange'

'Orange' != 'orange'

'Orange' < 'orange'

'Orange' <= 'orange'

'Orange' > 'orange'

'Orange' >= 'orange'



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.7 snippets

# Counting Occurrences
sentence = 'to be or not to be that is the question'

sentence.count('to')

sentence.count('to', 12)

sentence.count('that', 12, 25)

# Locating a Substring in a String
sentence.index('be')

sentence.rindex('be')

# Determining Whether a String Contains a Substring 
'that' in sentence

'THAT' in sentence

'THAT' not in sentence

# Locating a Substring at the Beginning or End of a String
sentence.startswith('to')

sentence.startswith('be')

sentence.endswith('question')

sentence.endswith('quest')




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.7 Self Check snippets

# Exercise 3
for word in 'to be or not to be that is the question'.split():
    if word.startswith('t'):
        print(word, end=' ')
        


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.8 snippets
values = '1\t2\t3\t4\t5'

values.replace('\t', ',')




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.8 Self Check snippets

# Exercise 1
'1 2 3 4 5'.replace(' ', ' --> ')






##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.9 snippets

# Splitting Strings
letters = 'A, B, C, D'

letters.split(', ')

letters.split(', ', 2)

# Joining Strings
letters_list = ['A', 'B', 'C', 'D']

','.join(letters_list)

','.join([str(i) for i in range(10)])

# String Methods partition and rpartition 
'Amanda: 89, 97, 92'.partition(': ')

url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

rest_of_url, separator, document = url.rpartition('/')

document

rest_of_url

# String Method splitlines 
lines = """This is line 1
This is line2
This is line3"""

lines

lines.splitlines()

lines.splitlines(True)


    

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.9 Self Checksnippets

# Exercise 2
', '.join(reversed('Pamela White'.split()))

# Exercise 3
url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

protocol, separator, rest_of_url = url.partition('://')

host, separator, document_with_path = rest_of_url.partition('/')

host

path, separator, document = document_with_path.rpartition('/')

path


    


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.10 snippets
'-27'.isdigit()

'27'.isdigit()

'A9876'.isalnum()

'123 Main Street'.isalnum()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.11 snippets
file_path = 'C:\\MyFolder\\MySubFolder\\MyFile.txt'

file_path

file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'

file_path





##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.12.1 snippets

import re

# Matching Literal Characters
pattern = '02215'

'Match' if re.fullmatch(pattern, '02215') else 'No match'

'Match' if re.fullmatch(pattern, '51220') else 'No match'

# Metacharacters, Character Classes and Quantifiers
'Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid'

'Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid'

# Other Predefined Character Classes

# Custom Character Classes
'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid'

'Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid'

'Match' if re.fullmatch('[^a-z]', 'A') else 'No match'

'Match' if re.fullmatch('[^a-z]', 'a') else 'No match'

'Match' if re.fullmatch('[*+$]', '*') else 'No match'

'Match' if re.fullmatch('[*+$]', '!') else 'No match'

# * vs. + Quantifier
'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid'

'Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid'

# Other Quantifiers
'Match' if re.fullmatch('labell?ed', 'labelled') else 'No match'

'Match' if re.fullmatch('labell?ed', 'labeled') else 'No match'

'Match' if re.fullmatch('labell?ed', 'labellled') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '123') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '1234567890') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '12') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '123456') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '1234567') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '12') else 'No match'


##########################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################
# Section 8.12.1 Self Check snippets

# Exercise 4
import re

street = r'\d+ [A-Z][a-z]* [A-Z][a-z]*'

'Match' if re.fullmatch(street, '123 Main Street') else 'No match'

'Match' if re.fullmatch(street, 'Main Street') else 'No match'


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.12.2 snippets

# Function sub—Replacing Patterns 
import re

re.sub(r'\t', ', ', '1\t2\t3\t4')

re.sub(r'\t', ', ', '1\t2\t3\t4', count=2)

# Function split 
re.split(r',\s*', '1,  2,  3,4,    5,6,7,8')

re.split(r',\s*', '1,  2,  3,4,    5,6,7,8', maxsplit=3)



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.12.2 Self Check snippets

# Exercise 1
import re

re.sub(r'\t+', ', ', 'A\tB\t\tC\t\t\tD')

# Exercise 2
re.split('\$+', '123$Main$$Street')



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.12.3 snippets

### Function search—Finding the First Match Anywhere in a String
import re

result = re.search('Python', 'Python is fun')

result.group() if result else 'not found'

result2 = re.search('fun!', 'Python is fun')

result2.group() if result2 else 'not found'

### Ignoring Case with the Optional flags Keyword Argument
result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE)

result3.group() if result3 else 'not found'

### Metacharacters that Restrict Matches to the Beginning or End of a String
result = re.search('^Python', 'Python is fun')

result.group() if result else 'not found'

result = re.search('^fun', 'Python is fun')

result.group() if result else 'not found'

result = re.search('Python$', 'Python is fun')

result.group() if result else 'not found'

result = re.search('fun$', 'Python is fun')

result.group() if result else 'not found'

### Function findall and finditer—Finding All Matches in a String
contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'

re.findall(r'\d{3}-\d{3}-\d{4}', contact)

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

### Capturing Substrings in a Match
text = 'Charlie Cyan, e-mail: demo1@deitel.com'

pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'

result = re.search(pattern, text)

result.groups()

result.group()

result.group(1)

result.group(2)


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.12.3 Self Check snippets

# Exercise 2
import re

result = re.search(r'(\d+) ([-+*/]) (\d+)', '10 + 5')

result.groups()

result.group(1)

result.group(2)

result.group(3)



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.13 snippets

# Cleaning Your Data 

# Data Validation
import pandas as pd

zips = pd.Series({'Boston': '02215', 'Miami': '3310'})

zips

zips.str.match(r'\d{5}')

cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])

cities

cities.str.contains(r' [A-Z]{2} ')

cities.str.match(r' [A-Z]{2} ')

# Reformatting Your Data

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, 
                          columns=['Name', 'Email', 'Phone'])

contactsdf

import re

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Phone'].map(get_formatted_phone)

formatted_phone

contactsdf['Phone'] = formatted_phone

contactsdf






##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 8.13 Self Check snippets

# Exercise 2
import pandas as pd

import re

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, 
                          columns=['Name', 'Email', 'Phone'])

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    if result:
        part1, part2, part3 = result.groups()
        return '(' + part1 + ') ' + part2 + '-' + part3
    else:       
        return value

contactsdf['Phone'] = contactsdf['Phone'].map(get_formatted_phone)

contactsdf






##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
