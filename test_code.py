from generated_symbols.data.advancement.predicate.FoodPredicate import FoodPredicate
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds

my_food_predicate = FoodPredicate(
    level=MinMaxBounds[int](min=1, max=10),
    saturation=5,
)
