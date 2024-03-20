
# classe qui sert de base pour tout les autres états, 
# créée pour que mon prof aie pas a toutes les relire une par une et pour qu'elles soient toutes uniformes

class TemplateState:
    def __init__(self):
        self.next_state = None
    
    def get_next_state(self):
        return self.next_state
    
    def enter(self):
        print("Entering template state")

    def check_conditions(self, ai, bullets):
        print("Checking conditions for template state")
        
        if(self.transition_to_State(ai,bullets)) : ## si la transisition valide le changment d'état
            print("on change d'état ")
            self.next_state = "State"
            return True
        else:
            return False
     
    def update(self, ai , bullets):
        pass

    def transition_to_State(self, ai, bullets):
        if( True ):
            return True