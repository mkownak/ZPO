
class PizzaCheese(Builder):

    ingredients = []

    def add_ingredient(self, ingredient: str) -> str:

        if ingredients_dict[ingredient] == "cheese":
            self.ingredients.append(ingredient)
            return f"{ingredient} added"
        elif ingredients_dict[ingredient] != "cheese":
            return 


    def show_ingredients(self) -> list:
        return self.ingredients


class PizzaMeat(Builder):

    ingredients = []

    def add_ingredient(self, ingredient: str) -> str:
        self.ingredients.append(ingredient)
        return f"{ingredient} added"

    def show_ingredients(self) -> list:
        return self.ingredients


p1 = Pizza()
print(p1.add_ingredient("bruh"))
print(p1.show_ingredients())
