from sys import exit
from ex45_combat import *
from ex45_scenes import *

class Engine(object):
    def __init__(self, map_scenes):
        self.map_scenes = map_scenes
        print "Map of scenes: ", self.map_scenes
    
    def play(self):
        current_scene = self.map_scenes.opening_scene()
        print "First scene: ", current_scene
        
        while True:
            print "\n--------"
            print "current_scene: ", current_scene
            next_scene_name = current_scene.enter()
            print "next scene name: ", next_scene_name
            current_scene = self.map_scenes.next_scene(next_scene_name)
            
                  
class Map(object):
    scenes = {
	'outside_tower' : OutsideTower(),
	'entrance_hall' : EntranceHall(),
	'staircase_1' : Staircase1(),
	'second_floor' : SecondFloor(),
	'staircase_2' : Staircase2(),
	'third_floor' : ThirdFloor(),
	'hall' : Hall(),
	'treasure_room' : TreasureRoom(),
    'combat1' : GenericGoblinCombat('staircase_1'),
    'combat2' : GenericGoblinCombat('staircase_2'),
    'combat3' : GenericGoblinCombat('treasure_room'),
    'final_boss' : FinalBossCombat()
    }
	
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "first scene in Map __init__ :", self.start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print "next scene:", val
        return val
        
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

chosen_scene = raw_input("> ")
a_map = Map(chosen_scene)
game_engine = Engine(a_map)
game_engine.play()        
