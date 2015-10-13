i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
    

print "\nConverting while loop to a function, drill_1"
def drill_1(n):
    i = 0 
    numbers1 = [ ]
    while i < n:
        print "Item %d" % i 
        numbers.append(i)
        i = i + 1
    print numbers1
    

print "\nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill 1 with n = 8"
drill_1(8)

#Add another variable to the function arguments that you can pass 
#in that lets you change 
#the + 1 on line 8 so you can change how much it increments by.

print "\nCreating a functiondrill_3 to allow variable step size"
def drill_3(n, s):
    i = 0
    numbers3 = [ ]
    while i < n:
        print "Item : %d" % i
        numbers3.append(i)
        i = i + s
    print numbers3
    
print "\nUsing drill 3 with n = 12 and s = 3"
drill_3(12, 3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    