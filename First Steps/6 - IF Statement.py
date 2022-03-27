#References:
# Contents: 0 to 
# Data Analysis with Python for Excel Users - Full Course 
# Course developed by Frank Andrade. 
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )


########################### IF Statement ######################################

# Contents: 
# 0) Introduction 


# 0) Introduction 
# The if statement is a conditional statement used  to decide whether 
# a certain statement or block of statements will be executed or not. 
# Here, you can see the syntax of this if statement. 


# if<condition>:
    #<code>
# 
# elif<confition>:
    #<code>
# ...
# else:
    #<code>
              
# The intentation is very important !        

# Examples 
age =18 
if age>=18: 
    print("You are an adult!")
else: 
    print("You are a kid")

# Out[] You are an adult!

# Example with elif

age =17.5 
if age>=18: 
    print("You are an adult!")
elif age>=13: 
    print("You are a teenager")
else: 
    print("You are a kid")
        
# Out[] You are a teenager
                                                                                                                                                                                                                                                                                                                                                     
