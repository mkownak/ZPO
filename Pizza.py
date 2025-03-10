from abc import ABC, abstractmethod


ingredients_dict = {"salami": "meat",
                    "gouda": "cheese",
                    "cebula": "vege",
                    "pomidor": "vege",
                    "kurczak": "meat",
                    "mozzarella": "cheese",}

class PizzaBuilder(ABC):
    ingredients: list

    @abstractmethod
    def add_ingredient(self, ingredient: str) -> None:
        pass

    @abstractmethod
    def show_ingredients(self) -> list:
        pass


class PizzaVege(PizzaBuilder):

    ingredients = []

    def add_ingredient(self, ingredient: str) -> None:
        if ingredients_dict[ingredient] == "vege":
            self.ingredients.append(ingredient)
        else:
            raise ValueError("Składnik nie jest vege")

    def show_ingredients(self) -> list:
        return self.ingredients


class PizzaMeat(PizzaBuilder):

    ingredients = []

    def add_ingredient(self, ingredient: str) -> None:
        if ingredients_dict[ingredient] == "meat":
            self.ingredients.append(ingredient)
        else:
            raise ValueError("Składnik nie jest miesem")

    def show_ingredients(self) -> list:
        return self.ingredients


class PizzaCheese(PizzaBuilder):

    ingredients = []

    def add_ingredient(self, ingredient: str) -> None:
        if ingredients_dict[ingredient] == "cheese":
            self.ingredients.append(ingredient)
        else:
            raise ValueError("Składnik nie jest serem")

    def show_ingredients(self) -> list:
        return self.ingredients


class PizzaDirector:
    _builder = None
    ingredients: list

    def _set_pizza(self, ingredient: str) -> None:
        category = ingredients_dict.get(ingredient)
        if category == "vege":
            self._builder = PizzaVege()
        elif category == "meat":
            self._builder = PizzaMeat()
        elif category == "cheese":
            self._builder = PizzaCheese()
        else:
            raise ValueError("nieznany składnik")

        self._builder.add_ingredient(ingredient) # dodanie decydujacego skladnika

    def add_ingredient(self, ingredient: str) -> None:
        if self._builder is None:
            self._set_pizza(ingredient)
        else:
            self._builder.add_ingredient(ingredient)

    def show_ingredients(self) -> list:
        return self._builder.show_ingredients()


p1 = PizzaDirector()
p1.add_ingredient("salami")
p1.add_ingredient("kurczak")
print(p1.show_ingredients())

