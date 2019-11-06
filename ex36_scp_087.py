import re
import random

from sys import exit

def face():
    print "A face appears, with no visible pupils, nostrils, or mouth."
    print "You feel extreme fear, and can't clam down."
    
    return True

def sound():
    if bool(random.getrandbits(1)):
        print "Suddenly, a sad and painful voice sounds from a child comes from downstairs."
        print "It sounds like to be tens of meters from here."
        return True
    else:
        return False

def stairs():
    platform = 1
    next = "downstairs"
    is_sound = False
    is_face = False
    escape = 10
    
    while True:
        print "You go %s 13 steps, and now you are at the %d platform." % (next, platform)
        print "The stairs are descending, then reaching an another platform."

        if platform > 5:
            is_sound = sound()
        
        if is_sound and not is_face and (random.random() < 0.2):
        	is_face = face()

        if is_face:
            print "The face is watching and follows you."
            print "Run! You are trying to escape."
            escape -= 1
            if escape == 0:
            	print "The face catches you, you fainted and disappeared."
            	exit(0)

        print "Do you want to go downstairs or upstairs?"
        next = raw_input("> ")
        
        while True:
            if re.search('down', next):
                platform += 1
                break
            elif re.search('up', next):
                platform -= 1
                if platform == 0:
                    print "You walk out the staircase."
                    exit(0)
                break
            else:
                print "You walk around, and are still at the %d platform." % platform
                print "Do you want to go downstairs or upstairs?"
                next = raw_input("> ")
                continue
        
        continue

def staircase():
    print "There are no lighting fixtures or windows present."
    print "All is in dark."
    print "A flashlight lays on the floor."
    print "Do you want to pick it up?"
    light = raw_input("> ")

    if re.search('[yY][eE][sS]', light):
        print "Flashlight turns on."
        print "There are stairs descending then reaching a semicircular platform."
        print "Descent direction rotates 180 degree at the platform."
        print "Then there are starirs descending, and hidden in the darkness."
        print "You can't see more."
        print "Do you want to go downstairs?"
        next = raw_input("> ")

        if re.search('[yY][eE][sS]', next):
            stairs()
        elif re.search('[nN][oO]', next):
            print "You are a coward."
            exit(0)
        else:
            print "I don't understand what you say."
            exit(0)
    elif re.search('[nN][oO]', light):
        print "You can't see anything."
        exit(0)
    else:
        print "I don't understand what you say."
        exit(0)

def start():
    print "There is a door in front of you."
    print "Do you want to open the door?"
    next = raw_input("> ")

    if re.search('[yY][eE][sS]', next):
        staircase()
    elif re.search('[nN][oO]', next):
        print "You are a coward."
        exit(0)
    else:
        print "I don't understand what you say."
        exit(0)

start()