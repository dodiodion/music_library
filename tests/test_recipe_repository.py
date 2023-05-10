from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1,'pizza', 45, 4),
        Recipe(2,'coxinha', 60, 4),
        Recipe(3,'poutine', 15, 3),
        Recipe(4,'feijoada', 120, 5)]
    
def test_find_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(2)
    assert recipe == Recipe(2,'coxinha', 60, 4)