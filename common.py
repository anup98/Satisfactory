import json
from item import Item
from recipe import Recipe
from main import REMOVELIST


def getItems():
    with open("scraper/data.json") as f:
        data = json.load(f)

    items = data['items']
    buildings = data['buildings']
    masterItems = {
        items[i]['name'].strip(): Item(items[i]['name'].strip()) for i in items
    }
    masterRecipes = {}

    for recipe in data['recipes'].values():
        if recipe['forBuilding'] or not recipe['inMachine']:
            continue

        r = Recipe(recipe['name'].replace("Alternate:", "").strip(), buildings[recipe['producedIn'][0]]['name'], recipe['alternate'])

        multiplier = 60 / recipe['time']

        for item in recipe['ingredients']:
            name = items[item['item']]['name']
            r.add_input(name, item['amount'] * multiplier)
            if r.name not in masterItems[name].usedInRecipes:
                masterItems[name].usedInRecipes.append(r.name)

        for item in recipe['products']:
            name = items[item['item']]['name']
            r.add_output(name, item['amount'] * multiplier)
            if r.name not in masterItems[name].recipes:
                masterItems[name].recipes.append(r.name)
        
        masterRecipes[r.name] = r
        
        for i in REMOVELIST:
            masterItems.pop(i)
    
    return masterItems, masterRecipes

def formulaData(r: Recipe):
    data = {
        "inputs": r.inputs,
        "outputs": r.outputs,
        "building": r.building,
    }
    return data



