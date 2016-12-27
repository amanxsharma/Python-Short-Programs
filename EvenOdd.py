##Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
##If the number is a multiple of 4, print out a different message.

num = input("Enter a number")
if num%2==0:
    if num%4==0:
        print "Number is multiple of 4 and even"
    else:
        print "Number is even"
else:
    print "Number is odd"
