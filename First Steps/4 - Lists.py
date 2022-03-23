#References:
# Contents: 0 to 7
# Data Analysis with Python for Excel Users - Full Course 
# Course developed by Frank Andrade. 
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )

# Content: 7
# Python Documentation contents
# The official documentation for Python 3.10.3.
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )

########################### Lists #############################################
# Contents: 
# 0) Introduction 
# 1) How to create lists (List Structure)
# 2) Indexing
# 3) Slicing 
# 4) Adding and Removing Elements to a list 
# 5) Lists concatenation 
# 6) Nested Lists
# 7) Sorting Lists
# 8) Update elements of the lists
# 9) How to copy lists

# 0) Introduction 
# In Python lists are used to store multiple items in a single variable 
# list are order and mutable containers. In Python,we call mutable,
# objects that can change their values

# 1) List structure 
# List_name = {Variable_1,Variable_2,Variable_3}
# Example
Integ=43
countries = ["United States","India",Integ,"India"];countries
# Out[6]: ['United States', 'India', 43, 'India']
# Notice that we can have different data type variables in a list
# and also repeted objects.  


# 2) Indexing 
# To get elements from lists we use indexing
# By indexing, we can obtain an element by its position. 
# So each item in a list has an index, which is the position in the list. 
# Python uses zero based indexing, that is the first element,so, United States
# has an index zero, the second is India which has as index one, and so on. 
# To access an element by its index, we need to use the square 
# brackets again. So let's see some examples.  

countries [0]
# Out[7]: 'United States'

# We can also use negative indexing 
countries[-1]
# Out[16]: 'India'
countries[3]
# Out[15]: 'India'

# these two lines of code have the same output, 
# we just change the way of indexing


# 3) Slicing 
# slicing means accessing parts of the list, 
# a slies is a subset of list elements  
# the slice notation takes the form of: 
# list_name[start:stop]

countries[0:2]
# Out[17]: ['United States', 'India']

# if we do not want to specify the stop point 
# (we want all the elements from start to the last in the list)
# we can omit the stop value 

countries[2:]
# Out[19]: [43, 'India']

# It works also the other way around 
countries[:3]
# Out[20]: ['United States', 'India', 43]


# 4) Adding and Removing Elements to a list 

# There are different methods that help us to add 
# a new element to lists. So let's have a look.

# Append (If you have to add just one variable)
# The Append Method add an element at the end of the list 

countries.append("Canada")
# Out[5]: ['United States', 'India', 43, 'India', 'Canada']


# Insert
# This method is useful when we want to add an element in a different position 
countries.insert(3, "Spain")
# Out[10]: ['United States', 'India', 43, 'Spain', 'Spain', 'India', 'Canada']


# There are different methods that help us to remove 
# a new element to lists. So let's have a look.

# Remove
countries.remove("United States")
# Out[20]: ['India', 43, 'Spain', 'India', 'Canada']

# Pop
# We use this method to remove elements by index
countries.pop(-1)
# Out[21]: 'Canada'
# Out[22]: ['India', 43, 'Spain', 'India']

# Del
# Another method to remove elements by index
del countries[0]
# Out[26]: [43, 'Spain', 'India']

# Unlike the Pop method del does not returns the removed element


# 5) List concatenation 

# We can join two list with the plus operator 
New_list=countries[3:]+countries[0:2];New_list
#Out[14]: ['Spain', 'Spain', 'India', 'Canada', 'United States', 'India']

# 6)Nested List

# By nested lists we intend lists composed by other lists 
# (and obviously if needed other variables)
nested_list=[countries,New_list]
# Out[17]: 
#[['United States', 'India', 43, 'Spain', 'India', 'Canada'], #First List
# ['Spain', 'India', 'Canada', 'United States', 'India']] # Second List 

# 7) Sorting Lists
Numbers= [2,-10,45,3,56,0] # Example List

# Sort
# The sort Method has 3 arguments
 
# Key -> Parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.
# Reverse -> Parameter with a boolean value. This is used to flag descending sorts.
Numbers.sort()
# Out[33]: [-10, 0, 2, 3, 45, 56]

Numbers= [2,-10,45,3,56,0]# Reinitialize the list
# Now we sort in reverse order
Numbers.sort(reverse=True);Numbers

#Out[37]: [56, 45, 3, 2, 0, -10]

# 8) Update elements of the lists

# To update values of the list we use indexing 
# Example 
Numbers= [2,-10,45,3,56,0]# Reinitialize the list
Numbers[0]=31;Numbers
# Out[42]: [31, -10, 45, 3, 56, 0]

# 9) How to copy lists

# There are different way to create copies of lists

# Slicing 
countries = ["United States","India",Integ,"India"];countries 
new_list=countries[:]
# Works also new_list=countries

#Copy
new_list= countries.copy()