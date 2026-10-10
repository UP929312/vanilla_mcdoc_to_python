"""
Generated from symbols.json for ::java::assets::model::Predicates
Local link to file: vanilla_mcdoc/assets/model/Predicates.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class Predicates(StrEnum):
    ANGLE = "angle"  # Used on compasses to determine the current angle, expressed in a decimal value of less than one.
    BLOCKING = "blocking"  # Used on shields to determine if currently blocking. If `1`, the player is blocking.
    BROKEN = "broken"  # Used on Elytra to determine if broken. If `1`, the Elytra is broken.
    CAST = "cast"  # Used on fishing rods to determine if the fishing rod has been cast. If `1`, the fishing rod has been cast.
    CHARGED = "charged"  # Used on crossbows to determine if they are charged with any projectile. If `1`, the crossbow is charged.
    COOLDOWN = "cooldown"  # Used on ender pearls and chorus fruit to determine the remaining cooldown, expressed in a decimal value between `0` and `1`.
    CUSTOMMODELDATA = "custom_model_data"  # Used on any item and is compared to the CustomModelData NBT, expressed in an integer value.  The number is still internally converted to float, causing a precision loss for some numbers above 16 million.  If the value read from the item data is greater than or equal to the value used for the predicate, the predicate is positive.
    DAMAGE = "damage"  # Used on items with durability to determine the amount of damage, expressed in a decimal value between `0` and `1`.
    DAMAGED = "damaged"  # Used on items with durability to determine if it is damaged. If 1, the item is damaged.  Note that if an item has the unbreakable tag, this may be `0` while the item has a non-zero `'damage'` tag.
    FIREWORK = "firework"  # Used on crossbows. If `1`, the crossbow is charged with a firework rocket.
    HONEYLEVEL = "honey_level"  # Used for honey level on bee nests and beehives.
    LEFTHANDED = "lefthanded"  # Determines the model used by left handed players. It affects the item they see in inventories, along with the item players see them holding or wearing.
    LEVEL = "level"  # Used for the `level` block state on light items.
    PULL = "pull"  # Determines the amount a bow or crossbow has been pulled, expressed in a decimal value of less than one.
    PULLING = "pulling"  # Used on bows and crossbows to determine if the bow is being pulled. If `1`, the bow is currently being pulled.
    THROWING = "throwing"  # Used on the trident to determine if the trident is ready to be thrown by the player. If `1`, the trident is ready for fire.
    TIME = "time"  # Used on clocks to determine the current time, expressed in a decimal value of less than one.
    TOOTING = "tooting"  # Whether the goat horn is being used.
    TRIMTYPE = "trim_type"
