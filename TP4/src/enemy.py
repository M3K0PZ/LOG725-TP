import pygame

from src.StateMachine.FinalStateMachine import StateMachine

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # l'état initiale
        
        self.is_hit = False
        self.current_sprite = pygame.image.load('./assets/enemy.png')
        self.rect = self.current_sprite.get_rect()
        # la position initiale est au centre de l'écran
        self.starting_position = (400, 100)
        self.rect.center = self.starting_position
        self.speed = 2
        self.backoff_time = 1000
        self.FinalStateMachine = StateMachine()
        self.state = self.FinalStateMachine.get_state()

    # Tip : pour calculer la distance (x, y) entre l'ennemi et les projectiles, calculez la différence entre les coordonnées. Par exemple : (position x du sprite 1) - (position x du sprite 2)
    def compute_distance(self, bullet):
        #return la distance entre l'ennemi et le projectile
        return abs(self.rect.y - bullet.rect.y)

    # Utilisez les règles dans la machine à états de réference comme base pour construire la structure de if/else nécessaire
    def update(self, bullets):
        self.FinalStateMachine.update(self, bullets)
        
        self.state = self.FinalStateMachine.get_state()#juste pour avoir une update de l'état visuelle, pas nécéssaire
        
