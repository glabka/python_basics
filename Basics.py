# -*- coding: utf-8 -*-
"""
Python basics
sources: https://www.youtube.com/watch?v=xLovcfIugy8
and http://python4java.necaiseweb.org/Fundamentals/DefiningFunctions
and https://www.geeksforgeeks.org/inheritance-in-python/
"""
print("\n********************************************\nsomething for begining\n********************************************")
print("hello", end = "")
print("hello2")
x = 4
print("x =", x)
print("x =",x, sep ="")
x = 3/4
print(x)
y = 3//4 # floor division
print(y)
x = int(3/5) # casting

# Strings (are immutable)
print("\n********************************************\nstrings\n********************************************")
s = "012345"
print("length:", len(s))
print("subsrting1", s[:2])
print("subsrting2", s[1:3])
print("substring3", s[-3:]) # last three characters
print("substring4", s[:-1]) # all but last character
print("substring5", s[::2]) # every second character
print("contains:", "23" in s) # does s contains "23"
print("last char:", s[-1])

# Constants
print("\n********************************************\nConstants\n********************************************")
print("Nothing enforce constants but capital letters are convention.")

# Sequences: lists
print("\n********************************************\nSequences: lists\n********************************************")
list1 = []
list1.append("house")
list1.append("mouse")
list1.append("object")
list1.append("something")
print(list1)
print("length", len(list1))
print("index 1 =", list1[1])
list1.insert(1, "grouse")
print(list1)
del(list1[1:3])
print(list1)
list2 = []
list2.append("floor")
list3 = list1 + list2
print("list3 =", list3)
list3 = []
list3.append(list1)
list3.append(list2)
print(list3)
print(list3[0][2])
list1[0] = "door"
list4 = [11, 4, 7]

list5 = [ 0 ] * 10 # creating list of ten zero elements
print(list5)

multi_dim_list = [[0, 1, 2], [2, 3]]
print(multi_dim_list[0][0] == multi_dim_list[0, 0]) # efficiently the same but first option is more inefficient as a new temporary array is created.
# Sequences: (immutable) tuples
print("\n********************************************\nSequences: tuples\n********************************************")
x = 1, 2, 3, 4
print(x)
y = x, 'yes', 5
print(y)
print(y[0][1])
x = 5, # creating tuple with single element
print(7 in y)

# swapping two values with tuple
a = 5
b = 20
a, b = (b, a)  # this unpacks tuple we just created into two variables a and b
print('a = ' + str(a) + ', b = ' + str(b))

# Collections: dictionary (hash)
print("\n********************************************\nCollections: dictionary(or hash)\n********************************************")
dict1 = {1 : "Tom", 2 : "Sally"}
dict1[3] = 'Andy'  # adding key and value
print(dict1[1])
dict1.update({1:"Thomas", 4:"Kenneth"})
print(dict1)
del dict1[3]
test_dict = {"a": 1, "b": 2, "a": 3}
print(test_dict["a"])  # returns 3

for key in dict1:
    print(key)
for key in dict1.keys():
    print(key)
for val in dict1.values():
    print(val)
for item in dict1.items():
    print(item)  # acctualy a tuple

# Collections: set
print("\n********************************************\nCollections: set\n********************************************")
set1 = set([1, 2, 3, 3])
print(set1)
set2 = {'a', 'b', 'c'}
print('each item in set can be only once. Sets are iterrable, but dont have indexes')
set2.add('d')
set2.update({'e', 'f'}, {'g'})
print(set2)
set2.remove('e')
set2.discard('e')  # does not raise an exception as remove when discarded object is not present

set3 = {3, 4, 5}

# union
set4 = set1.union(set3)
# is equivalent to 
set4 = set1 | set3

# intersection
set4 = set1.intersection(set3)
# is equivalent to
set4 = set1 & set3

# difference
set4 = set1.difference(set3)
# is equivalent to
set4 = set1 - set3

# symetric difference
set4 = set1.symmetric_difference(set3)
# is equivalent to
set4 = set1 ^ set3



# operators
print("\n********************************************\noperators\n********************************************")
# == check if values are equal
# is check if it is the same instance
x = 4
y = 4
print(x == y)
print(x is y)
x = [1]
y = [1]
print(x == y)
print(x is y)

print(not (4 < 5))
print(((4 < 5) or True) and (4 > 5))

x = 1
x += 5

print("\n********************************************\noperator overloading\n********************************************")
class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False

    def __add__(self, other):
        return self.a + other.a

a1 = A(1)
a2 = A(2)
print(f"is A(1) greater then A(2): {a1 > a2}")
print(f"A(1) + A(2): {a1 + a2}")
# if statement
print("\n********************************************\nif statement\n********************************************")
name1 = "Smith, John";
name2 = "Smith, Jane";

if name1 < name2 :
    print("Name1 comes first.")
elif name1 > name2 :
    print("Name2 comes first.")
else :
    print("The names are the same.")

if 4 < 5:
    print('1')
elif 4 > 3:
    print('2')
else:
    print('3')

# loops 
print("\n********************************************\nloops\n********************************************")    
x = 0
while x < 5:
    print(x, end = " ")
    x+=1
print("")

for x in range(5): # range => 0 .. 4
    print(x, end = " ")
print("")

for x in range(2, 10, 3): # from 2 to 10 with increment 3
    print(x, end = " ")
print("")

for x in list1:
    print(x, end = " ")
print()

list1 = ["something", "something2", "something3"]
for index, item in enumerate(list1):
    print(str(index) + ". " + item)

x = 0
while True:
    x += 1
    if x == 3:
        continue
    print(x, end = " ")
    if x == 5:
        break
print()

for x in range(5):
    if x == 6:
        break
else:
    print("else statement executes when foor loop ends naturally")
    
for i in range( 5, 0, -1 ) :
  print(i)
  
    
# functions
print("\n********************************************\nfunctions\n********************************************")
print("functions are close to java static functions")
def sum(a, b ,c = 0): # parameter c has default value 
    return a + b + c
print(sum(1, 2))

mystery = sum
print(mystery(1, 2, 3))

print("more values can be return using a tuple.")

# classes
print("\n********************************************\nclasses\n********************************************")
class Dog:
    def __init__(self, name, age):
        self._name = name # the underscore lets other users know that this is considered private variable
        self._age = age
    
    def get_age(self): # self indicates it is an instance method, otherwise it would be class method (like static in java)
        return self._age
    
    def get_name(self):
        return self._name
    
    def set_age(self, age):
        self._age = age
    
    def set_name(self, name):
        self._name = name
    
    def __str__(self):
        return "Dog:\nName: " + self._name + "\nAge: " + str(self._age)

    @staticmethod
    def random(): # class method
        return 7
d1 = Dog("Scruffy", 5)
print(d1)
print(Dog.random())
print("age = ", d1.get_age())

print("A class may only contain a single constructor.")
print(" __str__() corresponds to toString() in java.")

# Modules
print("\n********************************************\nModules\n********************************************")
print("module is single python file containing defintions of functions and classes")
print("there is a difference between \"from math import *\" and \"import math\"")
print("if the first is used, sqrt(5) is valid statement, if the latter is used the Math.sqrt(5) have to be used.")

# input
print("\n********************************************\ninput\n********************************************")
#x = input("enter number:")
#x = float(x)
#print("You entered x =", x)

# Null Reference
print("\n********************************************\nNull reference\n********************************************")
name1 = None
result = name1 is None
result2 = name1 == None
print("result =", result)
print("result2 =", result2)

# Variable Scope
print("\n********************************************\nVariable Scope\n********************************************")
print("there are 4 scope classes: built-in, global/module, local, instance")
var_x = 5
def fun_see_global_var():
    print("var_x =", var_x)
fun_see_global_var()

var_a = 40
def wont_change_var_a():
    var_a = 0

wont_change_var_a()
print("var_a =", var_a)

def do_change_var_a():
    global var_a
    var_a = 0

do_change_var_a()
print("var_a =", var_a)

def myfunc():
  x = 300
  def myinnerfunc():
    print("x =", x)
  myinnerfunc()

myfunc()

class Variable_showcase:
    static_var = 42
    def __init__(self):
        self.instance_var = 1
    

# Exceptions
print("\n********************************************\nExceptions\n********************************************")
# catching exception
try:
  myList = [ 12, 50, 5, 17 ]
  print(myList[4])
  
except IndexError:
  print("Error: Index out of range.")

try:
  x = 0
  myList = [ 12, 50, 5, 17 ]
  print(myList[ 3 ] / x)

except IndexError:
  print("Error: Index out of range.")

except ZeroDivisionError:
  print("Error: Attempt to divide by zero.")

except:
  print("Error: An exception was raised.")

# raising exception
def min( value1, value2 ) :
   if value1 == None or value2 == None :
      raise TypeError
   if value1 < value2:
      return value1
   else:
      return value2

# assert
def average( valueList ) :
   total = 0
   assert len( valueList ) > 0, "Empty list in average()."
   for x in valueList :
      total = total + x

   try:
      avg = total / len( valueList )
      return avg
   except:
       print("some exception")
#list1 = []
#average(list1)

# inheritance
print("\n********************************************\nInheritance\n********************************************")
# Example of inheritance
class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_age(self):
        return self._age
    
    def get_name(self):
        return self._name
# class Employee inherits from class Person
class Employee(Person):
    
    def __init__(self, name, age, company):
        self._company = company
        Person.__init__(self, name, age)
    
    def get_company(self):
        return self._company

empl1 = Employee("Jon", 25, "Google")
print("empl1's age == ", empl1.get_age())

# Example of multiple inheritance
class Base1(object): 
    def __init__(self): 
        self.str1 = "Geek1"
        print("Base1")
  
class Base2(object): 
    def __init__(self): 
        self.str2 = "Geek2"        
        print("Base2")
  
class Derived(Base1, Base2): 
    def __init__(self): 
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print("Derived")
          
    def printStrs(self): 
        print(self.str1, self.str2) 
         
  
ob = Derived() 
ob.printStrs()

print("the constructor of parent class has to be called")

# sandbox
print("\n********************************************\nsandbox\n********************************************")
list1 = ["neco", "nekdo", "word"]
list2 = [list1, [], "nejak"]
print("word" in list2)

#dict1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

# packing and unpacking
print("\n********************************************\npacking and unpacking\n********************************************")
# unpacking of list
def fun(a, b, c, d): 
    print(a, b, c, d)

my_list = [1, 2, 3, 4] 
fun(*my_list) # unpacking arguments from list to function

# unpacking of dictionary 
dict1 = {"a":1, "b":2, "c":3, "d":10}
fun(*dict1) # unpacks keywords
fun(**dict1) # keywords have to match to function parameters
# btw
fun(a=1, c=3, b=2, d=10)

# packing 'tuple' (packs arguments as tuple)
def mySum(*args): # unknown number of arguments 
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 

print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20))

# packing dictionary
def fun(**kwargs): 
    print(type(kwargs)) 
    for key in kwargs: 
        print("%s = %s" % (key, kwargs[key])) 

fun(name="geeks", ID="101", language="Python") 

def fun2(name=None, **kwargs):
    print(kwargs)  # does not print name

fun2(name='Kenneth', num=42, something=None)

# dunder name == double underscore name
print("\n********************************************\ndunder name\n********************************************")
print(__name__)
print("__name__ is main if the script is run or it equals module name if script is imported")


# docstrings
print("\n********************************************\ndoc strings\n********************************************")
def do_something(arg):
    """My handy documentation to do_something"""
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("do_something only takes int, float or string.")
        
help(do_something)


# logging
print("\n********************************************\nlogging\n********************************************")
import logging
logging.basicConfig(filename='my_log.log', level=logging.DEBUG)
print('logging levels are CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET')
logging.info('my info')
logging.debug('my debug info')


# debugging
print("\n********************************************\ndebugging\n********************************************")
# import pdb
# pdb.set trace 
# command next or n for executing next line
# continue or c for running the rest of the script
# quit or q for quitting (I think)


# lambda
print("\n********************************************\nlambda\n********************************************")
def ntimes(n):
  return lambda a : a * n

my_doubler = ntimes(2)
my_tripler = ntimes(3)

print(my_doubler(5))
print(my_tripler(5))

list1 = ["ahoj", None, "x", 5]
print(list(filter(lambda x: x is not None, list1)))

      

# other
print("\n********************************************\nother\n********************************************")
str1 = "tuples are tuples. it is what it is. You should wait for it."
a = str1.count('tuples')
print(a)
index = str1.index('tuple')
print(index)

# more list methods
my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']
del my_pets[0:2]
print(my_pets)
my_pets.insert(1, 'Snuffles')
print(my_pets)
pet2 = my_pets.pop(1) # returns and removes from the list
my_pets.remove('Squash') # removes the first occurance
list1 = ['hoj', 'hello', 'hi']
print(bool(list1))  # checking if list is empty
print(bool([]))  # checking if list is empty

print('PEP 8 = python enhancement proposal 8')
print('To check if your code is PEP8 compatible and more run flake8 <module_name>.py')
print('PEP 20 - The Zen of Python = run import this to see')

# deleting list while looping over it ==> unexpected error
for item in list1:
    list1.remove(item)
print(list1)  # != [] but is equal to ['hello']
# correct way of doing that
list1 = ['hoj', 'hello', 'hi']
for item in list1.copy():
    list1.remove(item)
print(list1) # == []

# time module and split method
import time
quote = "Some arbitrary text"
words = quote.split() # splits on white spaces
for word in words:
    print(word)
    time.sleep(.5)

# join
list1 = ['Thomas', 'Dough', 'Elizabeth']
my_str = ', '.join(list1)
print(my_str)

# cleaning screen
import os
def cleen_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def even(my_input):
    if len(my_input) >= 1:
        return my_input[0::2]
    else:
        raise Exception()

def sillycase(str_arg):
    middle = len(str_arg) // 2
    new_str = str_arg[:middle].lower()
    new_str += str_arg[middle:].upper()
    return new_str


print(sillycase('ahoj'))

print(list(enumerate("abcdefg")))



