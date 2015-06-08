#for i in [1, 2, 3, 4, 5]:
#    print i
#    for j in [1, 2, 3, 4, 5]:
#        print j
#        print i + j
#    print i
#print "done looping"

from __future__ import division
import re as regex

my_regex = regex.compile("[0-9]+", regex.I)

print 5 / 2

def double(x):
    """this where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2"""
    return x * 2

def my_print(message='my default message'):
    print message

my_print()
my_print(double(10))

def subtract(a=0, b=0):
    return a - b

print subtract(10, 5)
print subtract(0, 5)
print subtract(b=5)
