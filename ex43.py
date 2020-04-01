from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured"
		exit(1)
		
class Engine(object):

    def __init__(self, scene_map):
      #  print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Plays first scene", current_scene

        while True:
           # print "\n--------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
           # print "map returns new scene", current_scene

class Death(Scene):
	
	quips = [
	"You're dead! Good job!",
	"You make a really nice main course!",
	"What did I expect??",
	"Enjoy the afterlife.",
	"The gothons dance on your shattered corpse."
	]
	def enter(self):
		print Death.quips[randint(0,4)]
		
class CentralCorridor(Scene):

	def enter(self):
		print "Your ship has been invaded by gothons"
		print "Everyone is dead."
		print "Except you."
		print "Time to make them pay."
		print "You have to get to the weapons room."
		print "You see a Gothon."
		print "He looks mad."
		print "What do you do?"
		
		action = raw_input("> ")
		
		if action == "shoot":
			print "You shoot at the Gothon."
			print "He seems to fizzle."
			print "He's got a personal shield!?"
			print "Your weapon is useless."
			print "He shoots you."
			print "You die."
			return 'death'
			
		
		elif action == "tell joke":
			print "You tell a joke."
			print "You can't tell what he thinks."
			print "He makes a loud grunting noise."
			print "He's laughing."
			print "He laughs so hard he falls over and hits his head."
			print "He dies."
			print "You can move on to the next room."
			return 'laserweaponarmory'
			
		elif action == "do nothing":
			print "He stares at you..."
			print "You stare back."
			print "He shoots you."
			print "You die."
			print "The end."
			return 'death'
			
		else:
			print "please enter a valid command"
			return 'central_corridor'
		
		
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You've gotten past the gothon."
		print "Stumbling and stammering in the dark, you reach the Armoury."
		print "At last."
		print "Now to get the bomb."
		print "Oh, wait."
		print "You've forgotten the pass code."
		print "You'll have to try to guess the code. You can remember that it's 4 digit code"
		print "There's a hint."
		print "A picture of apple pie?"
		
		guesses = 1
		code = "3142"
		guess = raw_input("> ")
		
		while guesses < 4 and guess != code:
			
			print "ERROR"
			guess = raw_input("> ")
			guesses = guesses + 1
		
		if guess == code:
			print "You guess the code!"
			print "You hurry inside."
			print "You find the bomb."
			print "Time to give these gothons a taste of their own medicine!"
			return 'thebridge'
	
			
			
		else:
			print "You fail to guess the code."
			print "You hear something behind you."
			print "You draw your weapon."
			return 'death'
		
	
		
		
class TheBridge(Scene):

	def enter(self):
		print "You've reached the bridge."
		print "It looks empty aside from one gothon."
		print "What do you do?"
		
		action = raw_input("> ")
		
		if action == "shoot":
			print "You shoot the gothon in the back."
			print "No one seems to notice."
			print "Good job."
			print "Now plant that bomb and get out of there."
			return "escapepod"
			
		elif action == "strangle":
			print "You sneak up behind him and try to strangle him."
			print "He's far stronger than you expect."
			print "He peels your arm off easily then turns and breaks your arms."
			print "You are now helpless."
			return 'death'
			
		elif action == "wait":
			print "You wait."
			print "More gothons enter the bridge."
			print "You're stuck."
			print "It's hopeless, you can't sneak out."
			return 'death'
			
		else:
			print "Please enter a valid command."
			return 'thebridge'
			
		
class EscapePod(Scene):

	def enter(self):
		print "You've almost made it"
		print "What do you do now?"
		
		action = raw_input("> ")
		
		if action == "detonate":
			print "The bomb goes off in the distance."
			print "You jump into the escape pod and jettison away."
			print "Success!"
			print "You watch as the ship burns, taking all the gothons with it."
			
		elif action == "jettison":
			print "You jump into the escape pod and jettison away."
			print "They've detected you."
			print "They lock on."
			print "You detonate the explosives."
			print "The ship explodes."
			print "You watch as the ship burns."
		
		else:
			print "You're indecision costs you."
			print "The gothons discover you."
			return 'death'
		
class Map(object):
	
	scenes = {
		'central_corridor' : CentralCorridor(),
		'thebridge' : TheBridge(),
		'death' : Death(),
		'laserweaponarmory' : LaserWeaponArmory(),
		'escapepod' : EscapePod()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		print "start_scene in next_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene returns", val
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
