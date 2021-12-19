from recipe import Recipe

class Item:
    def __init__(self, name: str):
        self.name = name
        self.usedInRecipes = []
        self.recipes = []

    def getRecipes(self):
        return self.recipes
    
    def getUsedToCraft(self):
        return self.usedInRecipes

    def __str__(self):
        return self.name
    