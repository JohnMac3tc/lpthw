name = 'John McElligott'
age = 36 #not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm = height * 2.54
kg = weight * 0.453592

print "lets talk about %s." % name
print "He's %d inches tall." % height 
print "Which is %r cm's tall." % cm
print "He's %d pounds heavy" % weight
print "Which is %r kilos heavy" % kg
print "He's actually not too heavy"
print "he's got %s eyes and %s hair." % (eyes, hair)
print "his teeth are usually %s depending on the coffee." % teeth

print " If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
