import random
from ecs import System
from components import Position, Velocity
import pygame
from components import Position, Velocity, Drawable, Score, PaddleTag, BallTag, Controlable, Controlable_IA


class MovementSystem(System):
    def update(self, entities):
        for entity in entities:
            if all(k in entity.components for k in [Position, Velocity]):
                ## toutes les entités sauf les raquette sinon elles tombent
                if ( not PaddleTag in entity.components ):
                    pos = entity.get_component(Position)
                    vel = entity.get_component(Velocity)
                    pos.x += vel.vx
                    pos.y += vel.vy
            

class CollisionSystem(System):
    def update(self, entities):
        screen_height = pygame.display.get_surface().get_height()
        for entity in entities:
            if BallTag in entity.components:
                pos_balle = entity.get_component(Position)
                vel_balle = entity.get_component(Velocity)
                # Inverser la vitesse verticale si la balle touche le haut ou le bas
                if pos_balle.y <= 0 or pos_balle.y >= screen_height - 10:  # 10 est la hauteur de la balle
                    vel_balle.vy = -vel_balle.vy
                #Si on touche une raquette
                for entity2 in entities:
                    if PaddleTag in entity2.components:
                        pos_raquette = entity2.get_component(Position)
                        vel2 = entity2.get_component(Velocity)
                        if (pos_balle.x <= pos_raquette.x + 10
                            and pos_balle.x >= pos_raquette.x
                            and pos_balle.y >= pos_raquette.y
                            and pos_balle.y <= pos_raquette.y + 70): #60 est la hauteur de la raquette, 70 pour laisser un peu de marge
                            
                            #chaque retour on accélère la balle jusqu'à une certaine vitesse
                            if abs(vel_balle.vx) < 8:
                                vel_balle.vx = -1 * (vel_balle.vx*1.05)  
                            else:
                                vel_balle.vx = -1 * vel_balle.vx                          
                            
                            # Deflect slightly up or down depending on where ball hit bat
                            vel_balle.vy += vel2.vy / 128
                            # max the y qnd x velocity
                            if vel_balle.vy > 5:
                                vel_balle.vy = 5
                            
                     
        
class PaddleControlSystem(System):
    def update(self, entities):
        screen_height = pygame.display.get_surface().get_height()
        for entity in entities:
            if PaddleTag in entity.components:
                pos = entity.get_component(Position)
                vel = entity.get_component(Velocity)
                keys = pygame.key.get_pressed()

                # Pour la première raquette
                if entity == entities[1]:  #  entities[1] est paddle1 //il faudrait chercher les raquettes par leur tag
                    if keys[pygame.K_w] and pos.y > 0:
                        pos.y -= vel.vy
                    if keys[pygame.K_s] and pos.y < screen_height - 60:  # 60 est la hauteur de la raquette
                        pos.y += vel.vy

                # Pour la deuxième raquette si elle a le composant Controlable_IA ou non ça change
                if entity == entities[2]:  # entities[2] est paddle2
                    """ if ( Controlable_IA in entity.components ): #mon code de l'ia l'autre plus complexe n'est pas totalement a moi 
                        #code de l'ia du jeu 
                        ball = entities[0]
                        ball_pos = ball.get_component(Position)
                        ball_vel = ball.get_component(Velocity)
                        # bouge en fonction de la position de la balle et de sa vitesse
                        if ball_vel.vx > 0 and ball_pos.y > pos.y and pos.y < screen_height - 60:
                            pos.y += vel.vy
                        elif ball_vel.vx > 0 and ball_pos.y < pos.y and pos.y > 0:
                            pos.y -= vel.vy """ 
                    if Controlable_IA in entity.components:
                        pos = entity.get_component(Position)
                        vel = entity.get_component(Velocity)
                        
                        ball = entities[0]  # Supposons que la balle est toujours entities[0]
                        ball_pos = ball.get_component(Position)
                        ball_vel = ball.get_component(Velocity)
                        
                        paddle_height = 60  # 60 est la hauteur de la raquette
                        half_paddle_height = 30  # 60 est la hauteur de la raquette
                        
                        # Calculer la position cible en tenant compte du milieu de la raquette
                        target_y = ball_pos.y + (ball_vel.vy * 5) - half_paddle_height
                        
                        #rajouter un peu d'aléatoire pour que l'ia ne soit pas trop forte
                        target_y += random.randint(-30, 30)
                        
                        # Réactivité variable basée sur la distance à la balle
                        distance_to_ball = abs(target_y + half_paddle_height - pos.y)
                        speed_modifier = 1 + (distance_to_ball / 100)
                        
                        #caper la vitesse pour que l'ia perde au bout d'un moment
                        if speed_modifier > 2:
                            speed_modifier = 2
                            
                        
                        
                        
                        # Mise à jour de la position de l'IA selon une tolérance et la vélocité de la raquette
                        tolerance = 10
                        if (ball_vel.vx > 0): 
                            if target_y > pos.y + tolerance:
                                pos.y += vel.vy * speed_modifier
                            elif target_y < pos.y - tolerance:
                                pos.y -= vel.vy * speed_modifier
                            
                                
   
                    elif( Controlable in entity.components ):
                        if keys[pygame.K_UP] and pos.y > 0:
                            pos.y -= vel.vy
                        if keys[pygame.K_DOWN] and pos.y < screen_height - 60:
                            pos.y += vel.vy

class ScoreSystem(System):    
    
    def update(self, entities):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()
        for entity in entities:
            if BallTag in entity.components:
                pos = entity.get_component(Position)
                v = entity.get_component(Velocity)  # pour réinitialiser la vitesse de la balle

                score_entities = [e for e in entities if Score in e.components]
                if pos.x <= 0:
                    # Joueur de droite marque
                    if len(score_entities) > 1:  # bug fix
                        score_entities[1].get_component(Score).value += 1  # Augmente le score du joueur de droite
                    pos.x, pos.y = screen_width // 2, screen_height // 2  # Réinitialiser la position de la balle
                    v.vx, v.vy = 5, random.choice([5, -5])  # Réinitialiser la vitesse de la balle avec une direction aléatoire
                elif pos.x >= screen_width:
                    # Joueur de gauche marque
                    if len(score_entities) > 0:
                        score_entities[0].get_component(Score).value += 1  # Augmente le score du joueur de gauche
                    pos.x, pos.y = screen_width // 2, screen_height // 2  # Réinitialiser la position de la balle
                    v.vx, v.vy = -5, random.choice([5, -5])  # Réinitialiser la vitesse de la balle avec une direction aléatoire

           
           
class DrawSystem :
    def __init__(self, screen):
        self.screen = screen
        # text init 
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render("0", 1, (255, 255, 255))
        self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 2)
        self.screen.blit(self.text, self.textpos)
        pygame.display.flip()
        
        self.bool = True
        
        
        
    def update(self, entities):
        self.screen.fill((0, 0, 0))
        scores = []
        if self.bool :
            for entity in entities:
                drawable = entity.get_component(Drawable)
                score = entity.get_component(Score)
                if drawable:
                    position = entity.get_component(Position)
                    pygame.draw.rect(self.screen, drawable.color, pygame.Rect(position.x, position.y, drawable.width, drawable.height))

                if score :
                    #stocker les scores 
                    scores.append(score.value)
            
            #afficher les scores
            self.text = self.font.render(str(scores[0]), 1, (255, 255, 255))
            self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 30 * 14)
            self.screen.blit(self.text, self.textpos)
            
            self.text = self.font.render("-", 1, (255, 255, 255))
            self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 30 * 15)
            self.screen.blit(self.text, self.textpos)
            
            self.text = self.font.render(str(scores[1]), 1, (255, 255, 255))
            self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 30 * 16)
            self.screen.blit(self.text, self.textpos)
            
            # si l'un des deux scores est a 10 fin du jeu 
            
            if ( scores[0] >= 7 ):
                self.text = self.font.render("Player Wins", 1, (255, 255, 255))
                self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 2, centery=self.screen.get_height() / 2)
                self.screen.blit(self.text, self.textpos)
                self.bool = False
                
                
                            
            elif(scores[1]>=7):
                self.text = self.font.render("player2 Wins", 1, (255, 255, 255))
                self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 2, centery=self.screen.get_height() / 2)
                self.screen.blit(self.text, self.textpos)
                self.bool = False

            
        
            
            pygame.display.flip()
        
        
    def update_home (self, entities):
        self.screen.fill((0, 0, 0))
        self.text = self.font.render("Press space to start", 1, (255, 255, 255))
        self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 2)
        self.screen.blit(self.text, self.textpos)
        pygame.display.flip()

    
    def update_game_over (self, entities):
        self.screen.fill((0, 0, 0))
        self.text = self.font.render("Press space to restart", 1, (255, 255, 255))
        self.textpos = self.text.get_rect(centerx=self.screen.get_width() / 2)
        self.screen.blit(self.text, self.textpos)
        pygame.display.flip()
    
""" class StateManagementSystem(System):
    def __init__(self):
        self.state = GameState.START
        self.systems = {}

    def add_system(self, state, system):
        if state not in self.systems:
            self.systems[state] = []
        self.systems[state].append(system)

    def set_state(self, new_state):
        self.state = new_state
        # Activer ou désactiver les systèmes en fonction du nouvel état
        for state, systems in self.systems.items():
            for system in systems:
                system.active = (state == new_state)

    def update(self, entities):
        # Ici, gérer logiques d'état
        pass
    
         """ # Idée de système pour gérer les états du jeu, sous une version ECS (ce que je n'ai pas fait mais pour l'idée)
