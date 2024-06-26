extends Node2D

# réseau
var peer = ENetMultiplayerPeer.new()
var hostname = "localhost"
var port = 11234

# état du jeu
var host_text = ""
var host_morse = ""
var client_answer = []
var game_over = false

# ===== GAME LOOP =====
func _physics_process(_delta):
	
	if (Input.is_action_just_pressed("ui_dot")): # fléche UP, point
		# jouer un son à J1
		rpc("_play_dot_on_server")
		
	elif (Input.is_action_just_pressed("ui_dash")): # fléche DOWN, trait d'union
		# jouer un son à J1
		rpc("_play_dash_on_server")
	# Note: Vous pouvez jouer le même son avec différentes durées pour le point (plus courte) et pour le trait d'union (plus longue), ou jouer des sons distincts.

# ===== EVÉNEMENTS INTERFACE =====
func _on_host_pressed():
	peer.create_server(port)
	multiplayer.multiplayer_peer = peer
	# montrer l'interface host
	$SendText.show()
	$MainMenu.hide()
	
func _on_join_pressed():
	peer.create_client(hostname, port)
	multiplayer.multiplayer_peer = peer
	# montrer l'interface client
	$ReceiveText.show()
	$MainMenu.hide()
	
func _on_btn_send_pressed():
	# à chaque fois que J1 envoye une message, le jeu est redémarré
	client_answer = []
	game_over = false
	host_text = $SendText/TextEdit.get_text()
	
	# chiffrer la message comme réference
	host_morse = get_morse_from_string(host_text)
	$SendText/AnswerPreview.set_text(host_morse)
	
	
	# envoyer la message à J2
	rpc("_show_text_on_client", host_text)


# ===== LOGIQUE DU JEU =====
func get_morse_from_string(text: String) -> String:
	var morse_code = {
		'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
		'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
		'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
		'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
	}
	
	var morse_text = []
	
	for aChar in text.to_upper():
		if aChar in morse_code:
			morse_text.append(morse_code[aChar])
	
	return "".join(morse_text)
	
func check_victory():
	#  Joueur 1 vérifie si la séquence reçue jusqu'à ce point correspond au message initial.
	var morse_rep = "".join(client_answer)
	print( "morse_rep = "+ morse_rep)
	print( "morse answer  = "+ host_morse)
	
	if( morse_rep == host_morse): # condition de victoire
		print("victoire :)")
		game_over = true
		
	elif (morse_rep.length() >= host_morse.length()): #condition de perte
		print("Perdu :(")
		game_over = true
		
	

# ===== MÉTHODES RPC (client)=====
@rpc("authority", "call_remote", "reliable")
func _show_text_on_client(text: String = ""):
		# Affiche le texte reçu sur l'interface du client
		$ReceiveText/TextDisplay.set_text(text)
		

@rpc("any_peer", "call_remote", "reliable")
func _play_dot_on_server():
	if !game_over:
		# Jouer le beep pour le point. Assurez-vous d'avoir un AudioStreamPlayer configuré
		$PointSound.play()
		# Ajouter le point à la réponse du client
		client_answer.append(".")
		check_victory()

@rpc("any_peer", "call_remote", "reliable")
func _play_dash_on_server():
	if !game_over:
		# Jouer le beep pour le trait. Assurez-vous d'avoir un AudioStreamPlayer configuré
		$DashSound.play()
		# Ajouter le trait à la réponse du client
		client_answer.append("-")
		check_victory()





