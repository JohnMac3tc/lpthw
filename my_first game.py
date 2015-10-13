from sys import exit
from sys import argv
import random
import time
prompt = 'so what do you choose? :  '



# so I'm going to try and create my own adventure game using all of the skills
# I've picked up so far.
# The story is about Jamey pup getting lost and having to find his own way home.
# He will need to be cunning and smart and survive long enough to get found
def displayIntro():
    print "The sun is just peeking through the curtain. You stretch and begin to look around..."
    time.sleep(3)
    print "Your mommy is downstairs and your daddy is still sleeping..."
    time.sleep(3)
    print "You decide to go downstairs......"
    time.sleep(4)
    print "The front door looks a little open. You nudge the door with your nose and see your mommy's car drive off!"
    print "You rush out as fast as you can, trying to catch up with the car but as you turn...."
    time.sleep(5)
    print "You're hit by a car!"
    time.sleep(1)
    print  "You panic as the world turns over and over!!! You finally stop spinning but realize there is a big truck coming right for you!"
    time.sleep(1)
    print "You need to get out of the way, right now! Do you run left or right?"


def chooseDirection():
    direction = ''
    while direction != 'left' and direction != 'right':
        print('Which way will you go? (left or right)')
        direction = raw_input(prompt)

    return direction


def carDodge(chosenDirection):
    if chosenDirection == "left":
        print "You bolt left, running as fast as you can. In fact you run until you're out of breath. But as you stop you realize something...."
        time.sleep(3)
        print "You have no idea how to get home!"
        time.sleep(2)
        print "All of a sudden you realize where you are. You're at the park!"

    if chosenDirection == "right":
        print "You bolt right, running as fast as you can. In fact you run until you're out of breath. But as you stop you realize something...."
        time.sleep(3)
        print "You have no idea how to get home!"
        time.sleep(2)
        print "You look in front of you and see a scary graveyard"


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    chosenDirection = chooseDirection()

    carDodge(chosenDirection)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
