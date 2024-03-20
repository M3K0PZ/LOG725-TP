import pygame

class HurtState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state
    
    def enter(self,ai):
        print("Entering Hurt state")
        ai.current_sprite = pygame.image.load('./assets/enemy_hurt.png')
        self.Wait_Flag = False
        
        
        
        
        
    def check_conditions(self, ai, bullets):
        #print("Checking conditions for template state")
        if(self.transition_to_Replace(ai,bullets)) : ## si la transisition valide le changment d'état
            self.next_state = "Replace"
            return True
        else:
            return False
     
    def update(self, ai , bullets):
        if( not self.Wait_Flag ):
            pygame.time.wait(1000) #on attend une seconde 
            self.Wait_Flag = True
            
        #le flag est juste la si on décide de pas utiliser pygame.time.wait(1000) et de faire un timer nous même
        #je l'utilise dans la transition, pour la forme, pas parce que c'est nécéssaire

    def transition_to_Replace(self, ai, bullets):
        if( self.Wait_Flag ):
            #j'aurais pu mettre le changement de sprite dans le check, mais ici c'est plus clair
            ai.current_sprite = pygame.image.load('./assets/enemy.png')
            return True