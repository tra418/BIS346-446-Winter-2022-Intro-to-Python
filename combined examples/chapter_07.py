# Section 7.2 snippets
import numpy as np

numbers = np.array([2, 3, 5, 7, 11])

type(numbers)

numbers

# Multidimensional Arguments
np.array([[1, 2, 3], [4, 5, 6]])

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
# Section 7.2 Self Check snippets

# Exercise 2
import numpy as np

np.array([x for x in range(2, 21, 2)])

# Exercise 3
np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]])

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
# Section 7.3 snippets
import numpy as np

integers = np.array([[1, 2, 3], [4, 5, 6]])

integers

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

floats

# Determining an array’s Element Type
integers.dtype

floats.dtype

# Determining an array’s Dimensions
integers.ndim

floats.ndim

integers.shape

floats.shape

# Determining an array’s Number of Elements and Element Size
integers.size

integers.itemsize

floats.size

floats.itemsize

# Iterating through a Multidimensional array’s Elements
for row in integers:
    for column in row:
        print(column, end='  ')
    print()

for i in integers.flat:
    print(i, end='  ')
    


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
# Section 7.3 Self Check snippets

# Exercise 1
import numpy as np

a = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]])

a.ndim

a.shape



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
# Section 7.4 snippets
import numpy as np

np.zeros(5)

np.ones((2, 4), dtype=int)

np.full((3, 5), 13)

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
# Section 7.5 snippets

# Creating Integer Ranges with arange 
import numpy as np

np.arange(5)

np.arange(5, 10)

np.arange(10, 1, -2)

# Creating Floating-Point Ranges with linspace
np.linspace(0.0, 1.0, num=5)

# Reshaping an array
np.arange(1, 21).reshape(4, 5)

# Displaying Large arrays 
np.arange(1, 100001).reshape(4, 25000)

np.arange(1, 100001).reshape(100, 1000)


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
# Section 7.5 Self Check snippets

# Exercise 2
import numpy as np

np.arange(2, 41, 2).reshape(4, 5)

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
# Section 7.6 snippets

# Timing the Creation of a List Containing Results of 6,000,000 Die Rolls 
import random

%timeit rolls_list = \
   [random.randrange(1, 7) for i in range(0, 6_000_000)]

# Timing the Creation of an array Containing Results of 6,000,000 Die Rolls  
import numpy as np

%timeit rolls_array = np.random.randint(1, 7, 6_000_000)

# 60,000,000 and 600,000,000 Die Rolls  
%timeit rolls_array = np.random.randint(1, 7, 60_000_000)

%timeit rolls_array = np.random.randint(1, 7, 600_000_000)

# Customizing the %timeit Iterations  
%timeit -n3 -r2 rolls_array = np.random.randint(1, 7, 6_000_000)

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
# Section 7.6 Self Check snippets

# Exercise 1
import numpy as np

%timeit sum([x for x in range(10_000_000)])

%timeit np.arange(10_000_000).sum()



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
# Section 7.7 snippets

# Arithmetic Operations with arrays and Individual Numeric Values
import numpy as np

numbers = np.arange(1, 6)

numbers

numbers * 2

numbers ** 3

numbers  # numbers is unchanged by the arithmetic operators

numbers += 10

numbers

# Broadcasting 

# Arithmetic Operations Between arrays 
numbers2 = np.linspace(1.1, 5.5, 5)

numbers2

numbers * numbers2

# Comparing arrays
numbers

numbers >= 13

numbers2

numbers2 < numbers

numbers == numbers2

numbers == numbers



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
# Section 7.7 Self Check snippets

# Exercise 2
import numpy as np

np.arange(1, 6) ** 2


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
# Section 7.8 snippets
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
                   
grades

grades.sum()

grades.min()

grades.max()

grades.mean()

grades.std()

grades.var()

# Calculations by Row or Column
grades.mean(axis=0)

grades.mean(axis=1)




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
# Section 7.8 Self Check snippets

# Exercise 2
import numpy as np

grades = np.random.randint(60, 101, 12).reshape(3, 4)

grades

grades.mean()

grades.mean(axis=0)

grades.mean(axis=1)




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
# Section 7.9 snippets
import numpy as np

numbers = np.array([1, 4, 9, 16, 25, 36])

np.sqrt(numbers)

numbers2 = np.arange(1, 7) * 10

numbers2

np.add(numbers, numbers2)

# Broadcasting with Universal Functions
np.multiply(numbers2, 5)

numbers3 = numbers2.reshape(2, 3)

numbers3

numbers4 = np.array([2, 4, 6])

np.multiply(numbers3, numbers4)



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
# Section 7.9 Self Checksnippets

# Exercise 2
import numpy as np

numbers = np.arange(1, 6)

np.power(numbers, 3)



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
# Section 7.10 snippets

# Indexing with Two-Dimensional arrays
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
                   
grades

grades[0, 1]  # row 0, column 1

# Selecting a Subset of a Two-Dimensional array’s Rows
grades[1]

grades[0:2]

grades[[1, 3]]

# Selecting a Subset of a Two-Dimensional array’s Columns
grades[:, 0]

grades[:, 1:3]

grades[:, [0, 2]]

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
# Section 7.10 Self Checksnippets

# Exercise 1
import numpy as np

a = np.arange(1, 16).reshape(3, 5)

a

a[1]

a[[0, 2]]

a[:, 1:4]


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
# Section 7.11 snippets
import numpy as np

numbers = np.arange(1, 6)

numbers

numbers2 = numbers.view()

numbers2

id(numbers)

id(numbers2)

numbers[1] *= 10

numbers2

numbers

numbers2[1] /= 10

numbers

numbers2

# Slice Views
numbers2 = numbers[0:3]

numbers2

id(numbers)

id(numbers2)

numbers2[3]

numbers[1] /= 10

numbers

numbers2


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
# Section 7.12 snippets
import numpy as np

numbers = np.arange(1, 6)

numbers

numbers2 = numbers.copy()

numbers2

numbers[1] *= 10

numbers

numbers2



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
# Section 7.13 snippets

# reshape vs. resize
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades

grades.reshape(1, 6)

grades

grades.resize(1, 6)

grades

# flatten vs. ravel
grades = np.array([[87, 96, 70], [100, 87, 90]])

grades

flattened = grades.flatten()

flattened

grades

flattened[0] = 100

flattened

grades

raveled = grades.ravel()

raveled

grades

raveled[0] = 100

raveled

grades

# Transposing Rows and Columns

grades.T

grades

# Horizontal and Vertical Stacking
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

np.hstack((grades, grades2))

np.vstack((grades, grades2))



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
# Section 7.13 Self Check snippets

# Exercise 1
import numpy as np

a = np.arange(1, 7).reshape(2, 3)

a = np.hstack((a, a))

a = np.vstack((a, a))

a


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
# Section 7.14.1 snippets

# Creating a Series with Default Indices
import pandas as pd

grades = pd.Series([87, 100, 94])

# Displaying a Series
grades

# Creating a Series with All Elements Having the Same Value
pd.Series(98.6, range(3))

# Accessing a Series’ Elements
grades[0]

# Producing Descriptive Statistics for a Series
grades.count()

grades.mean()

grades.min()

grades.max()

grades.std()

grades.describe()

# Creating a Series with Custom Indices
grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])

grades

# Dictionary Initializers
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

grades

# Accessing a Series’ Elements Via Custom Indices
grades['Eva']

grades.Wally

grades.dtype

grades.values

# Creating a Series of Strings 
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

hardware

hardware.str.contains('a')

hardware.str.upper()


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
# Section 7.14.1 Self Check snippets

# Exercise 1
import numpy as np

import pandas as pd

temps = np.random.randint(60, 101, 6)

temperatures = pd.Series(temps)

temperatures

temperatures.min()

temperatures.max()

temperatures.mean()

temperatures.describe()

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
# Section 7.14.2 snippets

# Creating a DataFrame from a Dictionary
import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
               'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
               
grades = pd.DataFrame(grades_dict)

grades

# Customizing a DataFrame’s Indices with the index Attribute 
grades.index = ['Test1', 'Test2', 'Test3']

grades

# Accessing a DataFrame’s Columns 
grades['Eva']

grades.Sam

# Selecting Rows via the loc and iloc Attributes
grades.loc['Test1']

grades.iloc[1]

# Selecting Rows via Slices and Lists with the loc and iloc Attributes
grades.loc['Test1':'Test3']

grades.iloc[0:2]

grades.loc[['Test1', 'Test3']]

grades.iloc[[0, 2]]

# Selecting Subsets of the Rows and Columns 
grades.loc['Test1':'Test2', ['Eva', 'Katie']]

grades.iloc[[0, 2], 0:3]

# Boolean Indexing
grades[grades >= 90]

grades[(grades >= 80) & (grades < 90)]

# Accessing a Specific DataFrame Cell by Row and Column
grades.at['Test2', 'Eva']

grades.iat[2, 0]

grades.at['Test2', 'Eva'] = 100

grades.at['Test2', 'Eva']

grades.iat[1, 2] = 87

grades.iat[1, 2]

# Descriptive Statistics
grades.describe()

pd.set_option('precision', 2)

grades.describe()

grades.mean()

# Transposing the DataFrame with the T Attribute
grades.T

grades.T.describe()

grades.T.mean()

# Sorting By Rows by Their Indices
grades.sort_index(ascending=False)

# Sorting By Column Indices
grades.sort_index(axis=1)

# Sorting By Column Values
grades.sort_values(by='Test1', axis=1, ascending=False)

grades.T.sort_values(by='Test1', ascending=False)

grades.loc['Test1'].sort_values(ascending=False)


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
# Section 7.14.2 Self Check snippets

# Exercise 1
import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}
         
temperatures = pd.DataFrame(temps, index=['Low', 'High'])  # (a)

temperatures  # (a)

temperatures.loc[:, 'Mon':'Wed']  # (b)

temperatures.loc['Low']  # (c)

pd.set_option('precision', 2)  # (d)

temperatures.mean()  # (d)

temperatures.mean(axis=1)  # (e)


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
