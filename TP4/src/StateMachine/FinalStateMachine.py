from src.StateMachine.FleeState import FleeState
from src.StateMachine.IdleState import IdleState
from src.StateMachine.WaitState import WaitState
from src.StateMachine.HurtState import HurtState
from src.StateMachine.ReplaceState import ReplaceState


class  StateMachine:

    def __init__(self):
              
        self.States = { 
            "Flee" : FleeState(),
            "Idle" : IdleState(),
            "Wait" : WaitState(),
            "Hurt" : HurtState(),
            "Replace" : ReplaceState()
        }
        self.current_state = self.States["Idle"]
        self.current_state_name = "Idle"

    def set_state(self, state):
        self.current_state = self.States[state]
        self.current_state_name = state
    
    def get_state(self):
        return self.current_state_name

    def update(self, ai, bullets):
        if self.current_state is not None:
            #updtate des états 
            self.current_state.update(ai,bullets)
            
            # si on a les conditions de transition
            if (self.current_state.check_conditions(ai, bullets)):
                #on assigne le prochain état
                self.set_state(self.current_state.get_next_state())
                #on call son équivalent d'init a chaque fois qu'on rentre dedans ie. on réinitialise l'état
                self.current_state.enter(ai)
                
                
                
            
          