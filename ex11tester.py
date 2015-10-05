my_list = {'yes', 'YES', 'Yes', 'Y', 'y'}
print "Who goes there?"
name = raw_input() 
print "hello", name, ". you must pay the toll to pass the gate. do you have coins?"
answer = raw_input()
if answer in my_list:
    coins = raw_input("Good, how much do you have?")
if coins >= 3:
    print ("Great %r, you have %r coins and you may pass") % (name, coins)
else:
    print ("GO AWAY!!!") 
    

    




