from sys import exit
#Exit from Python. This is implemented by raising the SystemExit exception, 
#so cleanup actions specified by finally clauses of try statements are honored, 
#and it is possible to intercept the exit attempt at an outer level.
    
#this is a function for the gold room
def gold_room():
    print "This room is full of gold. How much do you take?"
        
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number>")
            
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard! Time to die")
            
            
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door"
    print "How are you going to move the bear?"
    print" You can taunt bear or take honey"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear moved from the door. You can go through it. Type in 'open door' to check out the other room"
            
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane"
    print " Do you flee for your life or eat your head?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        dead("you are a dead man, fool!")
        

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left"
    print "Which do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")
        
start()
            
    
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    