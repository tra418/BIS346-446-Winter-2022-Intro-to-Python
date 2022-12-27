# -*- coding: utf-8 -*-
"""
Spyder Editor

SOlutions to BUAN 446 Summer 2022 Midterm Applied Question
"""
# Method 1

import random 

Jack = 10 
Queen = 10 
King = 10 
Ace = 11

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace] 

cards = random.choices(deck, k = 2)

print(f'Names of Cards: {cards}\nValue of Cards: {sum(cards)}')


# Method 2 
import random 

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] 

cardone = deck[random.randrange(0, 13)]

cardtwo = deck[random.randrange(0, 13)]

if cardone == 'Jack' or cardone == 'Queen' or cardone == 'King': 
    cardone = 10 
elif cardone == 'Ace': 
    cardone = 11 
    print(f'Names of Cards: {cardone} and {cardtwo}\nValue of Cards: {cardone + cardtwo}')
    
if cardtwo == 'Jack' or cardtwo == 'Queen' or cardtwo == 'King': 
    cardtwo = 10 
elif cardtwo == 'Ace': 
    cardtwo = 11 
    print(f'Names of Cards: {cardone} and {cardtwo}\nValue of Cards: {cardone + cardtwo}')
    
print(f'Names of Cards: {cardone} and {cardtwo}\nValue of Cards: {cardone + cardtwo}')


# Method 3
import random

deck = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
    "Queen": 10, "King": 10, "Ace": 11}

names = []
values = []

for x in range(2):
    name, value = random.choice(list(deck.items()))
    names.append(name)
    values.append(value)

print(f"1st Card: {names[0]} \n2nd Card: {names[1]} \nTotal: {values[0] + values[1]:>5}")
