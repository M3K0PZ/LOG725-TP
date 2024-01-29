import pygame
from ecs import Entity
from components import Position, Velocity, Drawable, Score, PaddleTag, BallTag, Controlable, Controlable_IA
from systems import MovementSystem, CollisionSystem, PaddleControlSystem, ScoreSystem, DrawSystem


pygame.init()
screen = pygame.display.set_mode((800, 600))


# Entités
ball = Entity()
ball.add_component(Position(400, 300))
ball.add_component(Velocity(5, 5))
ball.add_component(Drawable(10, 10, (255, 255, 255)))
ball.add_component(BallTag())

paddle1 = Entity()
paddle1.add_component(Position(30, 250))
paddle1.add_component(Velocity(0, 10))
paddle1.add_component(Drawable(10, 60, (255, 255, 255)))
paddle1.add_component(PaddleTag())
paddle1.add_component(Controlable())

paddle2 = Entity()
paddle2.add_component(Position(760, 250))
paddle2.add_component(Velocity(0, 10))
paddle2.add_component(Drawable(10, 60, (255, 255, 255)))
paddle2.add_component(PaddleTag())
paddle2.add_component(Controlable_IA())

score1 = Entity()
score1.add_component(Score(0))

score2 = Entity()
score2.add_component(Score(0))

entities = [ball, paddle1, paddle2, score1, score2]

# Systèmes
movement_system = MovementSystem()
collision_system = CollisionSystem()
paddle_control_system = PaddleControlSystem()
score_system = ScoreSystem() 
draw_system = DrawSystem(screen) ## all display is done here


# Boucle de jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    movement_system.update(entities)
    collision_system.update(entities)
    paddle_control_system.update(entities)
    score_system.update(entities)
    
    draw_system.update(entities)
    """ pas besoin de le finir pour le tp mais c'est ici qu'on mettrait le menu et le game over
    if (game_state == "PLAYING"):
        draw_system.update(entities)
    elif (game_state == "HOME"):
        draw_system.update_home(entities)
    elif (game_state == "GAME_OVER"):
        draw_system.update_game_over(entities)
     """
    

    clock.tick(60)

pygame.quit()
