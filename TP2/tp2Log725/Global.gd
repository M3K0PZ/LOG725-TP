extends Node

var Sound_mode = true
var current_music : AudioStreamPlayer #Sons en train d'être joués

# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func Sound_on():
	Sound_mode = true
	print(current_music)
	if (current_music != null):
		current_music.play()
	
	

func Sound_off():
	Sound_mode = false
	if (current_music != null):
		current_music.stop()
	

func get_sound_mode():
	return Sound_mode
	
func play(player: AudioStreamPlayer):
	
	if player and player is AudioStreamPlayer and Sound_mode:
		player.play()
	
	
		
func play_music(player: AudioStreamPlayer):
	print("sound_played")
	if (current_music != null): # si on joue déja une musique on va la stopper 
		current_music.stop()
		current_music = null
	
	current_music = player ## on rajoute le son si il doit être resume / stopé (les musiques pas les sfx)
		
	if player and player is AudioStreamPlayer and Sound_mode:
		player.play()
		
	
