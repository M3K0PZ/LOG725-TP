extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	pass


func _on_body_entered(_body):
	get_tree().call_deferred("change_scene_to_file", "res://Scene_end/End.tscn") 
	## defered call demandé par godot pour gérer les charactedbody2D sinon il est pas content
