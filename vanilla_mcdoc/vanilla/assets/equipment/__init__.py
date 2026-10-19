"""Vanilla's assets/equipment/ files"""
from vanilla_mcdoc.assets.equipment.Dyeable import Dyeable
from vanilla_mcdoc.assets.equipment.Equipment import Equipment
from vanilla_mcdoc.assets.equipment.Layer import Layer
from vanilla_mcdoc.assets.equipment.Layers import Layers
from vanilla_mcdoc.assets.equipment.TrimOverride import TrimOverride, WhenStruct
from vanilla_mcdoc.assets.equipment.WingsLayer import WingsLayer

ARMADILLO_SCUTE = Equipment(
    layers=Layers(
        wolf_body=[
            Layer(texture='minecraft:armadillo_scute'),
            Layer(texture='minecraft:armadillo_scute_overlay', dyeable=Dyeable()),
        ],
    ),
)

BLACK_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:black')]))

BLACK_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:black_harness')]))

BLUE_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:blue')]))

BLUE_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:blue_harness')]))

BROWN_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:brown')]))

BROWN_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:brown_harness')]))

CHAINMAIL = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:chainmail')],
        humanoid_leggings=[Layer(texture='minecraft:chainmail')],
        humanoid_baby=[Layer(texture='minecraft:chainmail')],
    ),
)

COPPER = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:copper')],
        humanoid_leggings=[Layer(texture='minecraft:copper')],
        humanoid_baby=[Layer(texture='minecraft:copper')],
        horse_body=[Layer(texture='minecraft:copper')],
        nautilus_body=[Layer(texture='minecraft:copper')],
    ),
    trim_overrides=[TrimOverride(when=WhenStruct(material='minecraft:copper'), palette='minecraft:trim/copper_darker')],
)

CYAN_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:cyan')]))

CYAN_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:cyan_harness')]))

DIAMOND = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:diamond')],
        humanoid_leggings=[Layer(texture='minecraft:diamond')],
        humanoid_baby=[Layer(texture='minecraft:diamond')],
        horse_body=[Layer(texture='minecraft:diamond')],
        nautilus_body=[Layer(texture='minecraft:diamond')],
    ),
    trim_overrides=[TrimOverride(when=WhenStruct(material='minecraft:diamond'), palette='minecraft:trim/diamond_darker')],
)

ELYTRA = Equipment(layers=Layers(wings=[WingsLayer(texture='minecraft:elytra', use_player_texture=True)]))

GOLD = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:gold')],
        humanoid_leggings=[Layer(texture='minecraft:gold')],
        humanoid_baby=[Layer(texture='minecraft:gold')],
        horse_body=[Layer(texture='minecraft:gold')],
        nautilus_body=[Layer(texture='minecraft:gold')],
    ),
    trim_overrides=[TrimOverride(when=WhenStruct(material='minecraft:gold'), palette='minecraft:trim/gold_darker')],
)

GRAY_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:gray')]))

GRAY_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:gray_harness')]))

GREEN_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:green')]))

GREEN_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:green_harness')]))

IRON = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:iron')],
        humanoid_leggings=[Layer(texture='minecraft:iron')],
        humanoid_baby=[Layer(texture='minecraft:iron')],
        horse_body=[Layer(texture='minecraft:iron')],
        nautilus_body=[Layer(texture='minecraft:iron')],
    ),
    trim_overrides=[TrimOverride(when=WhenStruct(material='minecraft:iron'), palette='minecraft:trim/iron_darker')],
)

LEATHER = Equipment(
    layers=Layers(
        humanoid=[
            Layer(texture='minecraft:leather', dyeable=Dyeable(color_when_undyed=-6265536)),
            Layer(texture='minecraft:leather_overlay'),
        ],
        humanoid_leggings=[
            Layer(texture='minecraft:leather', dyeable=Dyeable(color_when_undyed=-6265536)),
            Layer(texture='minecraft:leather_overlay'),
        ],
        humanoid_baby=[
            Layer(texture='minecraft:leather', dyeable=Dyeable(color_when_undyed=-6265536)),
            Layer(texture='minecraft:leather_overlay'),
        ],
        horse_body=[
            Layer(texture='minecraft:leather', dyeable=Dyeable(color_when_undyed=-6265536)),
            Layer(texture='minecraft:leather_overlay'),
        ],
    ),
)

LIGHT_BLUE_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:light_blue')]))

LIGHT_BLUE_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:light_blue_harness')]))

LIGHT_GRAY_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:light_gray')]))

LIGHT_GRAY_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:light_gray_harness')]))

LIME_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:lime')]))

LIME_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:lime_harness')]))

MAGENTA_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:magenta')]))

MAGENTA_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:magenta_harness')]))

NETHERITE = Equipment(
    layers=Layers(
        humanoid=[Layer(texture='minecraft:netherite')],
        humanoid_leggings=[Layer(texture='minecraft:netherite')],
        humanoid_baby=[Layer(texture='minecraft:netherite')],
        horse_body=[Layer(texture='minecraft:netherite')],
        nautilus_body=[Layer(texture='minecraft:netherite')],
    ),
    trim_overrides=[TrimOverride(when=WhenStruct(material='minecraft:netherite'), palette='minecraft:trim/netherite_darker')],
)

ORANGE_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:orange')]))

ORANGE_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:orange_harness')]))

PINK_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:pink')]))

PINK_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:pink_harness')]))

PURPLE_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:purple')]))

PURPLE_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:purple_harness')]))

RED_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:red')]))

RED_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:red_harness')]))

SADDLE = Equipment(
    layers=Layers(
        nautilus_saddle=[Layer(texture='minecraft:saddle')],
        pig_saddle=[Layer(texture='minecraft:saddle')],
        strider_saddle=[Layer(texture='minecraft:saddle')],
        camel_husk_saddle=[Layer(texture='minecraft:saddle')],
        camel_saddle=[Layer(texture='minecraft:saddle')],
        horse_saddle=[Layer(texture='minecraft:saddle')],
        donkey_saddle=[Layer(texture='minecraft:saddle')],
        mule_saddle=[Layer(texture='minecraft:saddle')],
        zombie_horse_saddle=[Layer(texture='minecraft:saddle')],
        skeleton_horse_saddle=[Layer(texture='minecraft:saddle')],
    ),
)

TRADER_LLAMA = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:trader_llama')]))

TRADER_LLAMA_BABY = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:trader_llama_baby')]))

TURTLE_SCUTE = Equipment(
    layers=Layers(humanoid=[Layer(texture='minecraft:turtle_scute')], humanoid_baby=[Layer(texture='minecraft:turtle_scute')]),
)

WHITE_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:white')]))

WHITE_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:white_harness')]))

YELLOW_CARPET = Equipment(layers=Layers(llama_body=[Layer(texture='minecraft:yellow')]))

YELLOW_HARNESS = Equipment(layers=Layers(happy_ghast_body=[Layer(texture='minecraft:yellow_harness')]))
