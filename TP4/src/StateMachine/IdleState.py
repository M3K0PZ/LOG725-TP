class IdleState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state
    
    def enter(self,ai):
        print("Entering idle state")

    def check_conditions(self, ai, bullets):
        #print("Checking conditions for idle state")
        
        if(self.transition_to_Flee(ai,bullets)) : ## si la transisition valide le changment d'état
            print("on change d'état de Idle à Flee")
            self.next_state = "Flee"
            return True
        else:
            return False
     
    def update(self, ai , bullets):
        #print("Updating idle state does nothing")
        pass

    def transition_to_Flee(self, ai, bullets):
        #si on a des balles, c'est qu'on a tiré ie fuir
        #print(bullets.__len__())
        if(bullets.__len__() > 0):
            return True
        
                
        
       
        
        
