# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:07:59 2018

@author: benjamin.l.solomon
"""
import numpy

"""Generalized version of a diceroll
n = what type of die is being used (e.g. 4-sided, 6-sided, 8-sided, etc.)
number = How many times the die is being rolled!"""

def n_sided(n, number):
    #Stores the rolls which the player receives
    rolls = []
    #Iterates through each roll, stores it, and prints the result
    for i in range(number):
        x=numpy.random.randint(1,n)
        rolls.append(x)
        print("For #", i+1, " diceroll you get ", x, '\n')
    #Gives a total number for the rolls
    sum_of_rolls = sum(rolls)
    return sum_of_rolls
