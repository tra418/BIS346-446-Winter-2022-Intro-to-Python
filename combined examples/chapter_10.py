# Section 10.2.1 and 10.2.2 Snippets

# Importing Classes Account and Decimal
from account import Account

from decimal import Decimal

# Create an Account Object with a Constructor Expression
account1 = Account('John Green', Decimal('50.00'))

# Getting an Account’s Name and Balance
account1.name

account1.balance

# Depositing Money into an Account
account1.deposit(Decimal('25.53'))

account1.balance

# Account Methods Perform Validation
account1.deposit(Decimal('-123.45'))
    
# Section 10.2.2
# Defining a Class 
Account?


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
# Section 10.2.3 Self Check snippets

# Exercise 3
from account import Account

from decimal import Decimal

account1 = Account('John Green', Decimal('50.00'))

account1.withdraw(Decimal('20.00'))

account1.balance

account1.withdraw(Decimal('100.00'))

account1.withdraw(Decimal('-10.00'))



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
# Section 10.3 snippets

from account import Account

from decimal import Decimal

account1 = Account('John Green', Decimal('50.00'))

account1.balance

account1.balance = Decimal('-1000.00')

account1.balance



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
# Section 10.4.1 snippets

from timewithproperties import Time

# Creating a `Time` Object
wake_up = Time(hour=6, minute=30)

# Displaying a `Time` Object
wake_up

print(wake_up)

# Getting an Attribute Via a Property 
wake_up.hour

# Setting the `Time` 
wake_up.set_time(hour=7, minute=45)

wake_up

# Setting an Attribute via a Property 
wake_up.hour = 6

wake_up

# Attempting to Set an Invalid Value 
wake_up.hour = 100



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
# Section 10.4.2 Self Check snippets

# Exercise 3
from timewithproperties import Time

t = Time()

t

t.time = (12, 30, 45)

t

t.time

        


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
# Section 10.4.3 snippets

# Attributes Are Always Accessible
from timewithproperties import Time

wake_up = Time(hour=7, minute=45, second=30)

wake_up._hour

wake_up._hour = 100

wake_up


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
# Section 10.5 snippets

from private import PrivateClass

my_object = PrivateClass()

my_object.public_data

my_object.__private_data

# Self Check Exercise 3
my_object._PrivateClass__private_data

my_object._PrivateClass__private_data = 'modified'

my_object._PrivateClass__private_data



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
# Section 10.6.1 snippets

# Creating, Shuffling and Dealing the Cards 
from deck import DeckOfCards

deck_of_cards = DeckOfCards()

print(deck_of_cards)

deck_of_cards.shuffle()

print(deck_of_cards)

# Dealing Cards
deck_of_cards.deal_card()

# Class Card’s Other Features
card = deck_of_cards.deal_card()

str(card)

card.image_name



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
# Section 10.6.4 snippets

from deck import DeckOfCards

deck_of_cards = DeckOfCards()

# Enable Matplotlib in IPython
%matplotlib

# Create the Base `Path` for Each Image
from pathlib import Path

path = Path('.').joinpath('card_images')

# Import the Matplotlib Features
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

# Create the `Figure` and `Axes` Objects
figure, axes_list = plt.subplots(nrows=4, ncols=13)

# Configure the `Axes` Objects and Display the Images
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

# Maximize the Image Sizes
figure.tight_layout()

### Shuffle and Re-Deal the Deck
deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)



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
# Section 10.6.4 Self Check snippets

# Exercise 3
deck_of_cards.shuffle()

figure, axes_list = plt.subplots(nrows=2, ncols=5)

for axes in axes_list.ravel():
     axes.get_xaxis().set_visible(False)
     axes.get_yaxis().set_visible(False)
     image_name = deck_of_cards.deal_card().image_name
     img = mpimg.imread(str(path.joinpath(image_name).resolve()))
     axes.imshow(img)

figure.tight_layout()
        


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
# Section 10.8.1 snippets

# 10.8.1 Base Class CommissionEmployee

# Testing Class CommissionEmployee
from commissionemployee import CommissionEmployee

from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-3333', 
    Decimal('10000.00'), Decimal('0.06'))

c

print(f'{c.earnings():,.2f}')

c.gross_sales = Decimal('20000.00')

c.commission_rate = Decimal('0.1')

print(f'{c.earnings():,.2f}')

# 10.8.2 Subclass SalariedCommissionEmployee 

# Testing Class SalariedCommissionEmployee

from salariedcommissionemployee import SalariedCommissionEmployee

s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
         Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
         
print(s.first_name, s.last_name, s.ssn, s.gross_sales, 
       s.commission_rate, s.base_salary)

print(f'{s.earnings():,.2f}')

s.gross_sales = Decimal('10000.00')

s.commission_rate = Decimal('0.05')

s.base_salary = Decimal('1000.00')

print(s)

print(f'{s.earnings():,.2f}')

# Testing the "is a" Relationship 
issubclass(SalariedCommissionEmployee, CommissionEmployee)

isinstance(s, CommissionEmployee)

isinstance(s, SalariedCommissionEmployee)

# Processing CommissionEmployees and SalariedCommissionEmployees Polymorphically
employees = [c, s]

for employee in employees:
     print(employee)
     print(f'{employee.earnings():,.2f}\n')
     

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
# Section 10.9 snippets

class WellPaidDuck:
    def __repr__(self):
        return 'I am a well-paid duck'
    def earnings(self):
        return Decimal('1_000_000.00')
    
from decimal import Decimal

from commissionemployee import CommissionEmployee

from salariedcommissionemployee import SalariedCommissionEmployee

c = CommissionEmployee('Sue', 'Jones', '333-33-3333',
                       Decimal('10000.00'), Decimal('0.06'))
                       
s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
    Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
    
d = WellPaidDuck()

employees = [c, s, d]

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

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
# Section 10.10.1 snippets

from complexnumber import Complex

x = Complex(real=2, imaginary=4)

x

y = Complex(real=5, imaginary=-1)

y

x + y

x

y

x += y

x

y



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
# Section 10.10.2 Self Check snippets

# Exercise 3
from complexnumber2 import Complex

x = Complex(real=2, imaginary=4)

y = Complex(real=5, imaginary=-1)

x - y

x -= y

x

y



        


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
# Section 10.12 snippets

from collections import namedtuple

Card = namedtuple('Card', ['face', 'suit'])

card = Card(face='Ace', suit='Spades')

card.face

card.suit

card

# Other Named Tuple Features
values = ['Queen', 'Hearts']

card = Card._make(values)

card

card._asdict()



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
# Section 10.12 Self Check snippets

# Exercise 2
from collections import namedtuple

Time = namedtuple('Time', ['hour', 'minute', 'second'])

t = Time(13, 30, 45)

print(t.hour, t.minute, t.second)

t

        


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
# Section 10.13.1 snippets

from dataclasses import dataclass

@dataclass
class Demo:
    x  # attempting to create a data attribute x



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
# Section 10.13.2 snippets

from carddataclass import Card
from carddataclass import Card

c1 = Card(Card.FACES[0], Card.SUITS[3])

c1

print(c1)

c1.face

c1.suit

c1.image_name

c2 = Card(Card.FACES[0], Card.SUITS[3])

c2

c3 = Card(Card.FACES[0], Card.SUITS[0])

c3

c1 == c2

c1 == c3

c1 != c3

from deck2 import DeckOfCards  # uses Card data class

deck_of_cards = DeckOfCards()

print(deck_of_cards)



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
# Section 10.13.2 Self Check snippets

# Exercise 1
from carddataclass import Card

c = Card('Ace', 'Spades')

c

type(c.face)

c.face = 100

c

type(c.face)



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
# Section 10.15 snippets
z = 'global z'

def print_variables():
    y = 'local y in print_variables'
    print(y)
    print(z)   

print_variables()

y

z

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
# Section 10.16 Snippets
# This file includes the Self Check snippets which continue from the section body.

# Time Series
# Simple Linear Regression
# Linear Relationships

c = lambda f: 5 / 9 * (f - 32)

temps = [(f, c(f)) for f in range(0, 101, 10)]

import pandas as pd

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])

axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')

y_label = axes.set_ylabel('Celsius')

# Components of the Simple Linear Regression Equation
# SciPy’s stats Module
# Pandas
# Seaborn Visualization
# Getting Weather Data from NOAA

# Loading the Average High Temperatures into a DataFrame
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')

nyc.head()

nyc.tail()

# Cleaning the Data
nyc.columns = ['Date', 'Temperature', 'Anomaly']

nyc.head(3)

nyc.Date.dtype

nyc.Date = nyc.Date.floordiv(100)

nyc.head(3)

# Calculating Basic Descriptive Statistics for the Dataset
pd.set_option('precision', 2)

nyc.Temperature.describe()

# Forecasting Future January Average High Temperatures
from scipy import stats

linear_regression = stats.linregress(x=nyc.Date,
                                     y=nyc.Temperature)

linear_regression.slope

linear_regression.intercept

linear_regression.slope * 2019 + linear_regression.intercept

linear_regression.slope * 1850 + linear_regression.intercept

# Plotting the Average High Temperatures and a Regression Line
import seaborn as sns

sns.set_style('whitegrid')

axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)

axes.set_ylim(10, 70)

# Getting Time Series Datasets

# Self Check Exercises 
# Exercise 3
year = 2019

slope = linear_regression.slope

intercept = linear_regression.intercept

temperature = slope * year + intercept

while temperature < 40.0:
    year += 1
    temperature = slope * year + intercept

year


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
