class Recipe:
    """ Represents the inputs, outputs, etc for a single recipe """

    def __init__(self, name: str, building: str, alternate=False):
        self.name = name
        self.building = building
        self.inputs = {}
        self.outputs = {}
        self.alternate = alternate
 
    def add_input(self, name: str, quantity: float):
        self.inputs[name] = quantity

    def add_output(self, name: str, quantity: float):
        self.outputs[name] = quantity
   
    def __str__(self):
        return self.name