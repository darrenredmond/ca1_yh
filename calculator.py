#10273765
#B8IT105 Assignment 1
#10 Function Calculators

import math

def add(first,second):
    return first + second
	
def subtract(first,second):
    return first - second    
	
def multiply(first,second):
    return first * second  
	
def divide(first,second):
    if second == 0:
        return 'Invalid'
    else:
        return first/second
	
def exponent(first,second):
    return first**second
    
def square(first):
    return first*first

def cube(first):
    return first*first*first
    
def sqrt(first):
    if first == 0:
        return 'Invalid'
    else:
        return math.sqrt(first)

def sinh(first):
    return round(math.sinh(first),2)
    
def log10(first):
    return round(math.log10(first),0)
    