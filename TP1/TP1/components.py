from ecs import Component

class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity(Component):
    def __init__(self, vx=0, vy=0):
        self.vx = vx
        self.vy = vy

class Drawable(Component):
    def __init__(self, width=10, height=10, color=(255, 255, 255)):
        self.width = width
        self.height = height
        self.color = color

class Score(Component):
    def __init__(self, value=0):
        self.value = value

class PaddleTag(Component):
    """Un composant vide pour identifier les raquettes."""
    pass

class BallTag(Component):
    """Un composant vide pour identifier la balle."""
    pass

class Controlable(Component):
    """Un composant vide pour identifier les entités controlables dans le system des mouvements."""
    pass
class Controlable_IA(Component):
    """Un composant vide pour identifier les entités controlées par IA dans le system des mouvements."""
    pass