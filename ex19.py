#this is the function. all functions start with def. the % 
#symbol is used to substitute the valuefor the variables
def cash_in_wallet(dollars_count, cents_count):
    print "You have %d dollars!" % cheese_count
    print "You have %d cents!" % cents_count
    print "You a rich dude!"
    print "Lets go party. \n"

#cheese and crackers is the variable that has cheese_count
# and boxes_of_crackers in it  
#cheese_and_crackers is the variable- the 20 is the variable cheese_count
# and 30 is the variable boxes_of_crackers  
print "you could just tell me how much you have?:"
cash_in_wallet(20, 30)

print "Or, we can use variables from our script:"
dollars_count = 123
cents_count = 77

cash_in_wallet(dollars_count, cents_count)

#this is adding the variables of 10 + 20 cheese_counts to 5 + 6 boxes_of_cheese
print "We can even do math inside too:"
cash_in_wallet(10 + 20, 5 + 6)

#this is adding the variables of 10 cheese_counts defined above to 100
# and the variable 50 in boxes_of_crackers defined above to 1000
#a mix of defined variable and math
print "And we can combine the two, variable and math:"
cash_in_wallet(dollars_count * 2, cents_count + 23)