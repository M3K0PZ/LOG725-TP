class FleeState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state

    def enter(self,ai):
        print("Entering Flee state")

    def check_conditions(self, ai, bullets):
        #print("Checking conditions for idle state")
        if(self.transition_to_Wait(ai,bullets)) :
            print("on change d'état de Flee à Wait")
            self.next_state = "Wait"
            return True
        else:
            return False 
        # if (conditions) => next state = Qqch (ici plus de balles)

    def update(self, ai, bullets):
        #print("Updating Flee state")
        condition_de_changement = None
            
        ## prendre la balle la plus proche seulement :
        bullet_to_dodge = None
        if(bullets.__len__() > 0):
            for bullet in bullets :
                nouvelle_dist = self.compute_distance(ai,bullet)
                if (condition_de_changement == None or condition_de_changement > nouvelle_dist ) :
                    condition_de_changement = nouvelle_dist
                    bullet_to_dodge = bullet
                
            ## gauche ou droite 
            if condition_de_changement > 0 :
                side = self.get_bullet_side(ai,bullet_to_dodge)
                if (side > 0) :
                    #print("fuite a gauche ")
                    # checker si on est pas en dehors de l'écran
                    if (ai.rect.x - ai.speed < 0):
                        print("OOB ERROR, on sort de l'écran si on continue")
                    else :
                       #déplacer l'ia vers la gauche
                        ai.rect.x -= ai.speed
                                        
                elif (side < 0):
                    if( ai.rect.x + ai.speed > 790):
                        print("OOB ERROR, on sort de l'écran si on continue")
                    else:
                    #   print("fuite a droite ")
                        #déplacer l'ia vers la droite
                        ai.rect.x += ai.speed
                    



    def transition_to_Wait(self, ai, bullets):
        #si on est derrière un mur de 96px, on valide qu'on est cachés et on attend
        # attention prendre en compte la taille du sprite de l'ia (32 px )
        if( (ai.rect.x > 550 and ai.rect.x < 550+96 -32)  or ai.rect.x > 100 and ai.rect.x < 100+96 - 32):
            return True
    
    def compute_distance(self,ai, bullet):
        #return la distance entre l'ennemi et le projectile sur y 
        return abs(ai.rect.y - bullet.rect.y)
    
    def get_bullet_side(self,ai, bullet):
        #return la position du projectile par rapport à l'ennemi
        return bullet.rect.x - ai.rect.x









