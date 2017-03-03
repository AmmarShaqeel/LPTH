class Map(object):
	
	scenes = {
	'central_corridor' : CentralCorridor,
	'thebridge' : TheBridge,
	'death' : Death,
	'laserweaponarmory' : LaserWeaponArmory,
	'escapepod' : EscapePod
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		