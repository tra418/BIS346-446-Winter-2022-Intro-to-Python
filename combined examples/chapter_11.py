# Section 11.2 snippets
factorial = 1

for number in range(5, 0, -1):
    factorial *= number
    
factorial


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
# Section 11.3 snippets
# Note that the self check #5 is included here as it
# continues the section's IPython session.

def factorial(number):
    """Return factorial of number."""
    if number <= 1:
        return 1
    return number * factorial(number - 1)  # recursive call
    
for i in range(11):
    print(f'{i}! = {factorial(i)}')

# Self Check Exercise 5
factorial(50)


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
# Section 11.4 snippets
# Note that the self check #3 is included here as it
# continues the section's IPython session.

# Function fibonacci 
def fibonacci(n):
    if n in (0, 1):  # base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Testing Function fibonacci
for n in range(41):
    print(f'Fibonacci({n}) = {fibonacci(n)}')

# Self Check Exercise 3
def iterative_fibonacci(n):
    result = 0
    temp = 1
    for j in range(0, n):
        temp, result = result, result + temp
    return result

%timeit fibonacci(32)

%timeit iterative_fibonacci(32)

%timeit fibonacci(33)

%timeit iterative_fibonacci(33)

%timeit fibonacci(34)

%timeit iterative_fibonacci(34)





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
# Section 11.7 snippets

# Linear Search Implementation
def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return -1

import numpy as np

np.random.seed(11)

values = np.random.randint(10, 91, 10)

values

linear_search(values, 78)

linear_search(values, 61)

linear_search(values, 66)




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
# 11 Exercise Snippets

# 11.1. What does the following code do?
def mystery(a, b):
    if b == 1:
        return a
    else:
        return a + mystery(a, b - 1)

mystery(2, 10)


# 11.2. Find the logic error(s) in the following recursive function, 
# and explain how to correct it (them). This function should find 
# the sum of the values from 0 to `n`.
def sum(n):
    if n == 0:
        return 0
    else: 
        return n + sum(n)

# 11.3. What does the following code do?
def mystery(a_array, size):
    if size == 1:
        return a_array[0]
    else: 
        return a_array[size - 1] + mystery(a_array, size - 1)
    
import numpy as np

numbers = np.arange(1, 11)

mystery(numbers, len(numbers))


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
