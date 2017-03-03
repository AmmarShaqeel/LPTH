from random import randint


def goblin_attack(number_of_goblins,hero_hp, goblin_melee):
    if number_of_goblins > 0:
        print "The goblins attack!"
        print "You cower in fear."
        number_of_goblins += 1
        for count in range(1, number_of_goblins):
            if hero_hp <= 0:
                print "/n ------------------"
                print "You die slowly."
                exit(0)
            print "Goblin number #%r attacks" % count
            hero_hp = hero_hp - goblin_melee
            print "He does %r damage" % goblin_melee
            print "You have %r health left." % hero_hp
            count += 1
    else:
        print "All the goblins are dead!"
        print "Good job!"
        

def mage_attack(hero_hp, mage_melee, mage_ranged):
    chance = randint(1,3)
    
    if chance == 1:
        type_attack = "melee"
    else:
        type_attack = "ranged"
    
    print "He strikes back with a %s attack" % type_attack
    
    if type_attack == "melee":
        hero_hp -= mage_melee
        print "He does %r damage" %  mage_melee
    else:
        hero_hp -= mage_ranged
        print "He does %r damage" %  mage_ranged
    
    print "You have %r hp left." % hero_hp
    
    if hero_hp <= 0:
        print "You die."
        print "The last thing you see before you die is gold."
        print "Lots of it."
        print "Forever out of your grasp."
        exit(0)
   
    return hero_hp 
    
           
class Character(object):
    def __init__(self, char_hp, char_melee, char_ranged):
        self.char_hp = char_hp
        self.char_melee = char_melee
        self.char_ranged = char_ranged
        

class GenericGoblinCombat(object):
    def __init__ (self, next_scene):
        self.next_scene = next_scene
    
    def enter(self):
        print "Hero hp: %r" % hero.char_hp
        num_goblins = randint(1,5)
        
        print "There are %d goblins" % num_goblins
        
        while num_goblins > 0 and hero.char_hp > 0:
            goblin = Character(30, 10, 0)
            print "What do you want to do?"
            print "1. Melee."
            print "2. Ranged."
            
            action = raw_input("> ")
            
            if action == "1":
                print "You hit a goblin with your sword!"
                print "It does 50 dmg."
                goblin.char_hp = goblin.char_hp - hero.char_ranged
            elif action == "2":
                print "You shoot the goblin!"
                print "It does 50 dmg."
                goblin.char_hp = goblin.char_hp - hero.char_melee
            
            if goblin.char_hp <= 0:
                print "A goblin dies!"
                print "Congrats"
                num_goblins -= 1
                print "Number of goblins left: %r" % num_goblins
                
            goblin_attack(num_goblins, hero.char_hp, goblin.char_melee)
        
        return self.next_scene  

        
class FinalBossCombat(object):
    
    def enter(self):
        print "It's time"
        print "You prepare for combat"
        print "He's waiting for you to move."
        print "What do you do?"
        
        while mage.char_hp > 0 and hero.char_hp > 0:
            print "1. Melee"
            print "2. Ranged"
            
            action = raw_input("> ")
            
            if action == "1":
                print "You hit a mage with your sword!"
                print "It does 50 dmg."
                mage.char_hp = mage.char_hp - hero.char_ranged
            elif action == "2":
                print "You shoot the mage!"
                print "It does 50 dmg."
                mage.char_hp = mage.char_hp - hero.char_melee
            
            if mage.char_hp <= 0:
                print "He's dead!"
                print "The treasure is yours!"
                exit(0)
            else:
                hero.char_hp = mage_attack(hero.char_hp, mage.char_hp, mage.char_ranged)
                            
    
mage = Character(150, 30, 60)
hero = Character(150, 50, 50)