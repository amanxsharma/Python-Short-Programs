a = [1,1,2,3,5,8,13,21,34,55,89] #input list
b = [] #empty list for result
num = input("Enter number")
for i in a:
    if i<num:
        b.append(i) #add all element of a which are less than 5 to b.
print "element less than ",num,"are ", b #print list
        
