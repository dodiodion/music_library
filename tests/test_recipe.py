from lib.recipe import Recipe
"""
Recipe constructs with an id, a recipe_name, cooking_time and a rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test recipe name", 65, 3)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test recipe name"
    assert recipe.cooking_time == 65
    assert recipe.rating == 3

def test_recipe_equal():
    recipe1 = Recipe(1, "Test recipe name", 65, 3)
    recipe2 = Recipe(1, "Test recipe name", 65, 3)
    assert recipe1 == recipe2

def test_recipe_format():
    recipe = Recipe(1, "Test recipe name", 65, 3)
    assert str(recipe) == "Test recipe name - 65 min - 3 stars"