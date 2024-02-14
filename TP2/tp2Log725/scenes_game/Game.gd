extends Node2D

#var tank_packed = preload("res://scenes_game/tank.gd")

# Called when the node enters the scene tree for the first time.
func _ready():
	#TODO if i wish to add more levels, i'd put this code into a scene named 'game' where i load each level, each level 
	# would have a metadata on it's base node, stating the usual needed stuff, like if i make a generative level a dictionnary of the positions,
	# maybe an index to the tilemap, the position of the tank, nuber of bullets, 
	#since it's not needed and i got only 24hrs (because pc is self destrcuting resulting in more & more bsod) i'm not doing it
	
	pass

	
	

func _input(event):
	if(event.is_action_pressed("Reload_map")):
		get_tree().reload_current_scene()
		
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# TODO : Win Logic (maybe des events depuis les zones de Win ?)
	pass

