extends CharacterBody2D

@export var speed = 100
@export var rotation_speed = 1.7

signal Ball_count_updated(Bullet_Name, Bullet_Count ) ## singal for the label UI update

var rotation_direction = 0


## Stock de munitions
var Red_bullet = 2
var Green_bullet = 0
var Blue_bullet = 0





# pré-Charger le scénario de la balle
var balle_scene = preload("res://scenes_game/Bullet.tscn")

func _ready():
	#initialisation de l'ui
	emit_signal("Ball_count_updated", "Red_bullet", Red_bullet)
	emit_signal("Ball_count_updated", "Green_bullet", Green_bullet)
	emit_signal("Ball_count_updated", "Blue_bullet", Blue_bullet)

func get_input():
	rotation_direction = Input.get_axis("Turn_Left", "Turn_Right")
	velocity = transform.x * Input.get_axis("Move_down", "Move_up") * speed
	
func _input(event):
	if event.is_action_pressed("Shoot_Red"):
		#print("shoot red")
		self.Tirer(1, Red_bullet)
	elif event.is_action_pressed("Shoot_Green"):
		#print("shoot green")
		self.Tirer(2, Green_bullet)
	elif event.is_action_pressed("Shoot_Blue"):
		#print("shoot Blue")
		self.Tirer(3, Blue_bullet)



func _physics_process(delta):#delta is constant here
	get_input()
	rotation += rotation_direction * rotation_speed * delta
	move_and_slide()


func Tirer(color_type:int, Ammo_count : int ):
	if(Ammo_count>= 1):
		var balle = balle_scene.instantiate()
		var direction_shoot = Vector2(cos(rotation), sin(rotation))
		
		get_parent().add_child(balle)
		
		balle.global_position = $Canon_Node/Barrel.global_position #node sur le bout du canon
		#print("position Tank : ", global_position)
		#print("position Canon : ", $Canon_Node/Barrel.global_position)
		#print("position canon node : ", $Canon_Node.global_position)
		balle.direction = direction_shoot #direction du tank
		
		
		match color_type:## could be optimised with 1 func arg only, no time tho
			1:
				Decrease_Bullet("Red_Ammo")
				balle.shoot(Color(1,0,0), "Red")

			2: 
				Decrease_Bullet("Green_Ammo")
				balle.shoot(Color(0,1,0), "Green")

			3:
				Decrease_Bullet("Blue_Ammo")
				balle.shoot(Color(0,0,1), "Blue")

			_:
				printerr("March color Error; see code int tank.gd")
		
		$TankSounds.try_play() ##une version en ajoutant un script, pas utilisé ailleurs, je mets direct la condition.
		
	else :
		print("No more ammo of this color ")
	
## fonction pour increase les balles count
func Add_bullet(Name : String):
	match Name:
		"Red_Ammo":
			#print("Red ammo Added")
			Red_bullet+=1
		"Green_Ammo":
			#print("Green ammo Added")
			Green_bullet+=1
		"Blue_Ammo":
			#print("Blue ammo Added")
			Blue_bullet+=1
		_:
			printerr("Error, no ammo type known, tank.gd")
			
## fonction pour decrase les balles count
func Decrease_Bullet(Name : String):
	match Name:
		"Red_Ammo":
			Red_bullet-=1
			emit_signal("Ball_count_updated", "Red_bullet", Red_bullet)
		"Green_Ammo":
			Green_bullet-=1
			emit_signal("Ball_count_updated", "Green_bullet", Green_bullet)
		"Blue_Ammo":
			Blue_bullet-=1
			emit_signal("Ball_count_updated", "Blue_bullet", Blue_bullet)
		_:
			printerr("Error, no ammo type known, tank.gd")
	
	

