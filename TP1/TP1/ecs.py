class Component:
    pass

class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[component.__class__] = component

    def get_component(self, component_type):
        return self.components.get(component_type, None)

class System:
    def update(self, entities):
        pass
