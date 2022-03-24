#References:
# Contents: 0 to 7
# Data Analysis with Python for Excel Users - Full Course 
# Course developed by Frank Andrade. 
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )

# Content: 7
# Python Documentation contents
# The official documentation for Python 3.10.3.
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )

########################### Dictionaries ######################################

# Contents: 
# 0) Introduction 
# 1) How to create Dictionaries (Dictionaries Structure)
# 2) Operations on Dictionaries

# 0) Introduction 
# In Python, a dictionary is an unordered collection of items 
# used to store data values, and a dictionary contains a key and a value. 
# So this is what you will often see in a dictionary. 

# 1) How to create Dictionaries (Dictionaries Structure)

my_dict = {'key1':'value1','key2':'value2'}

# So now let's create a dictionary that contains 
# some basic informations: 
    
my_data = {"name":"Matt","age":26}


# 2) Operations on Dictionaries

# Keys
# With this method we can get the keys of the dictionary: 

my_data.keys()
# Out[6]: dict_keys(['name', 'age'])

# Values
# With this method we can get the values of the dictionary: 

my_data.values()
# Out[7]: dict_values(['Matt', 26])

# Items
# With this method we can get the items of the dictionary: 

my_data.items()
# Out[8]: dict_items([('name', 'Matt'), ('age', 26)])

# Adding Values 
# We can add items to dictionary following this structure : 

my_data["height"]=1.7
# Out[10]: {'name': 'Matt', 'age': 26, 'height': 1.7}

# Update
# With this method we can update the items of the dictionary.
# Inside parentheses, we have to open curly braces to update this new item.
# So, i'm gonna write the key, which is height. 
#And then I'm going to set the new height, which is 1.8.


my_data.update({"height":1.8})
# Out[12]: {'name': 'Matt', 'age': 26, 'height': 1.8}

# Copy of dictionaries 

# Copy
# With this method we can get copies of the dictionary: 
new_dict=my_data.copy();new_dict
#Out[14]: {'name': 'Matt', 'age': 26, 'height': 1.8}

# Remove Elements

# Pop
# With this method we can remove an element of the dictionary: 

my_data.pop("name")
# Out[15]: 'Matt'

# Del function 
del my_data["age"]
# Out[17]: {'height': 1.8}

#clear 
# With this method we remove all the elements of the dictionary: 
my_data.clear()
# Out[20]: {}