# SoundManager.gd
extends Node2D

func _ready():
	pass

func play_wall():
	$Collision_sound.play()
