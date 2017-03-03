from random import randint

class Scene(object):
    def enter(self):
        print "Scene not yet complete."
        exit(1)

class Death(Scene):
    def enter(self):
        print "You have died"
        exit(0)
	
class OutsideTower(Scene):
    def enter(self):
        print "You've travelled far in search of this tower."
        print "Legend tells of a great treasure hidden inside."
        print "There's a massive door barring your way."
        print "You take a deep breath, and marshalling your strength,",
        print "let out a massive blast of energy."
        print "The door shatters leaving the way into the tower clear."
        return "entrance_hall"
	
class EntranceHall(Scene):
    def enter(self):
        print "You enter the tower"
        print "Goblins!"
        print "They move to attack."
        print "You prepare yourself for combat."
        return "combat1"
	
	
class Staircase1(Scene):
    def enter(self):
        print "You cautiously climb the staircase."
        print "It's very long."
        print "Very, very long."
        print "To you're surprise you encounter nothing."
        return "second_floor"
	
class SecondFloor(Scene):
    def enter(self):
        print "Puffing and panting you reach the second floor."
        print "Phew."
        print "More goblins."
        print "Time to deal with them."
        return "combat2"
	
class Staircase2(Scene):
    def enter(self):
        print "After defeating yet more goblins, you move on to the 2nd staircase."
        print "It's also very long."
        print "You hate stairs."
        return "third_floor"
	
class ThirdFloor(Scene):
    def enter(self):
        print "You reach the third floor."
        print "Nothing."
        print "The goblins must have pulled back to the hall."
        print "You get ready to go in."
        return "hall"
        
	
class Hall(Scene):
    def enter(self):
        print "Goblins"
        print "This is getting old."
        return "combat3"
       
	
class TreasureRoom(Scene):
    def enter(self):
        print "You've killed all the goblins."
        print "You reach the treasure room."
        print "There's an evil looking mage standing there."
        print "What do you do?"
        print "1. Attempt to persuade. (50% chance of success)."
        print "2. engage him in combat"
        
        action = raw_input("> ")
        
        if action == "1":
            result = randint(1,2)
            #print "Result: %r" % result
        elif action == "2":
            print "You engage him in combat."
            return "combat_boss"
        else:
            print "Please try again."
            return "treasure_room"
        
        if result == 1:
            print "Success! You persuade him to walk away and leave all the gold to you!"
            print "Game over!"
            print "You win!"
            exit(0)
        else:
            print "You fail to persuade him."
            print "You'll have to do this the hard way."
            return "final_boss"
            
        
        
	