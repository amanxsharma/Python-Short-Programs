########## String Operations, Input from user ################

i = input("enter age ") ### integer input
name = raw_input("enter name ")  ###String input
print "Hello ",name  ## greeting message while concatenating with String

## calculate year when user will be 100 years
age=(2016 +(100-i))

## ask him how many times he wants to print the message
n = input("how many times you want to copy? ")

## create a string to print
## converting int to string using str() so that it can be concatenated with str
otpt = "you will trun 100 in the year " + str(age) +"\n"

## this will print otpt string n times
print (n* otpt)
