class WaitState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state
    
    def enter(self,ai):
        print("Entering Wait state")

    def check_conditions(self, ai, bullets):
        #print("Checking conditions for Wait state")
        
        if(self.transition_to_Hurt(ai,bullets)) : ## si la transisition valide le changment d'état
            print("on change d'état vers Hurt")
            self.next_state = "Hurt"
            return True
        elif (self.transition_to_Replace(ai,bullets)) :
            print("on change d'état vers Hurt")
            self.next_state = "Replace"
            return True
        else:
            return False
     
    def update(self, ai , bullets):
        #does nothing but wait until no more bullets are fired
        pass

    def transition_to_Hurt(self, ai, bullets): #état qui dit 'touché' puis attends les 1s de plus en rouge
        if( bullets.__len__() <= 0 and ai.is_hit ):
            return True
    
    def transition_to_Replace(self, ai, bullets): #état qui revient au centre de l'écran
        if( bullets.__len__() <= 0 and not ai.is_hit ):
            return True