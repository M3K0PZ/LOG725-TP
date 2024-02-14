extends Area2D


@export var speed : float

var color : Color
var direction = Vector2() #vecteur normalisé de ou on tire
var Color_name : String

signal Wall_breaking()


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	position += speed * delta * direction.normalized()

	#Code pour optimiser les performanes : on ibère les balles si elles sortent de l'écran
	var screen_size = get_viewport_rect().size
	if position.x < 0 or position.x > screen_size.x or position.y < 0 or position.y > screen_size.y:
		queue_free()
	

func shoot(Color_Choice : Color, Name: String):
	color = Color_Choice
	Color_name = Name
	# Appliquer la couleur au Sprite de la balle
	var sprite = get_node("Sprite2D")  # Assurez-vous que le chemin vers le Sprite est correct
	sprite.modulate = color

func get_shoot_direction() -> Vector2:
	return Vector2(cos(rotation), sin(rotation))


func _on_body_shape_entered(_body_rid, body, _body_shape_index, _local_shape_index):
	if(body.has_meta("Color")):
		var block_color = body.get_meta("Color")
		#print(block_color)
		if(block_color == Color_name):
			if(Global.get_sound_mode()):
				var AudioListener = get_node("../AudioListener")
				#print(AudioListener)
				if(AudioListener != null):
					AudioListener.play_wall()
			
			body.queue_free()
			#singale la destruction du mur pour l'audio listener 
			emit_signal("Wall_breaking")
			
	#if body.is_in_group("Destructible"): Une autre méthode pour les murs, mais j'ai pas fait comme ça
		#body.queue_free()
	queue_free()
