extends TextureButton


# Called when the node enters the scene tree for the first time.
func _ready():
	var sound_mode = Global.get_sound_mode()
	if (!sound_mode): ## on inverse les textures si le son est off lors du spawn
		var temp = texture_normal
		self.texture_normal = texture_pressed
		self.texture_pressed = temp
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _pressed():
	if(Global.get_sound_mode()):
		Global.Sound_off()
	else:
		Global.Sound_on()
