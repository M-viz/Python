#References:
# Data Analysis with Python for Excel Users - Full Course 
# Course developed by Frank Andrade. 
# Reachable at ( https://www.youtube.com/watch?v=WcDaZ67TVRo&t=1s )

########################### Variables #########################################

# We use the equal (=) sign to assing values to variables 
message_1="I'm learning Python"; 
message_1 # to see the content of the variable we have to invoke the variable

message_2="and it's fun"; message_2

# String concatenation via + operator 

message=message_1 + " " + message_2
# Out[15]: "I'm learning Python and it's fun"

# An alternative way to concatenate string is via F String
f'{message_1} {message_2}' 
