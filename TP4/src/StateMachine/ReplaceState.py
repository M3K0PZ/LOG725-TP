class ReplaceState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state
    
    def enter(self, ai):
        print("Entering Replace state")

    def check_conditions(self, ai, bullets):
        #print("Checking conditions for template state")
        
        if(self.transition_to_Idle(ai,bullets)) : ## si la transisition valide le changment d'état
            #print("on change d'état ")
            self.next_state = "Idle"
            return True
        else:
            return False
     
    def update(self, ai , bullets):
        #go to ai.starting_position if not already there (-16 to center the ai on the starting position)
        if( ai.rect.x != ai.starting_position[0]-16 ):
            #a gauche ou a droite
            if( ai.rect.x < ai.starting_position[0]-16 ):
                ai.rect.x += ai.speed
            elif( ai.rect.x > ai.starting_position[0]-16 ):
                ai.rect.x -= ai.speed
        #si on était en 3d on reseterait aussi y 
        

    def transition_to_Idle(self, ai, bullets):
        if( ai.rect.x == ai.starting_position[0]-16 ): #on est replacés! c'est reparti
            return True