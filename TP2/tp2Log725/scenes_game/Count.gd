extends Label

@export var Ammo_type : String
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_tank_ball_count_updated(Bullet_Name, Bullet_Count):
	#print("EVENT FIRED "+ Bullet_Name)
	if Bullet_Name == Ammo_type : 
		#print("Updated :  "+ Bullet_Name)
		self.text= str(Bullet_Count)
