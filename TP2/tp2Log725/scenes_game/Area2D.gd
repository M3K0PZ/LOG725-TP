extends Area2D
class_name Bullet
## A node used for [Gun]
##
## This node is used for [Gun], acts like a bullet with configurable speed and angle( for gun )

@export_category("Bullet")

## The time in seconds where this bullet is deleted
@export var delete_after : int = 30 

# Variables pour les paramètres de la balle (tank info)
var direction = Vector2()

## speed of the bullet in pixels per second
@export var speed : float


func _ready():
	print("ready")


func on_screen_exited():
	queue_free()

func tirer(couleur : int):
	print("Shooting with color %d", couleur)
	match couleur : 
		1 :
			print ("shot : color")
		2:
			print("Shot : color")
		3: 
			print("shot : color")

func _on_Bullet_body_entered(body): #si on touche n'importe quoi on despawn la balle, si on touche un mur coloré il despawn aussi
	if body.is_in_group("Color_Walls"):
		body.queue_free()
	queue_free()
