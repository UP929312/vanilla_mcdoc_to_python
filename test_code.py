from generated_symbols.data import AdvancementIcon, FoodPredicate, MinMaxBounds

my_food_predicate = FoodPredicate(
    level=MinMaxBounds(min=1, max=10),
    saturation=5,
)
print(my_food_predicate)

advancement_icon = AdvancementIcon(item='minecraft:acacia_boat')
