# vanilla-mcdoc

Pydantic models for every file in Minecraft: Java Edition's data packs and resource packs: recipes, advancements, loot
tables, worldgen, item models, and the rest. They're generated from [vanilla-mcdoc](https://github.com/SpyglassMC/vanilla-mcdoc),
the schemas that [Spyglass](https://github.com/SpyglassMC/Spyglass) uses to validate packs, so they follow every
Minecraft release and snapshot.

```python
from vanilla_mcdoc.data import Smelting

recipe = Smelting.model_validate({
    "type": "minecraft:smelting",
    "ingredient": "minecraft:iron_ore",
    "result": {"id": "minecraft:iron_ingot"},
    "experience": 0.7,
    "cookingtime": 200,
})
recipe.experience  # 0.7
recipe.model_dump(mode="json", exclude_none=True)  # Back to the JSON that goes in the pack
```

## Installing

Requires Python 3.14 or later.

```text
pip install vanilla-mcdoc
```

Each Minecraft version is its own package version, so you can install the one your pack targets:

| You want                                      | Install                                    |
|-----------------------------------------------|--------------------------------------------|
| The newest release of Minecraft               | `pip install vanilla-mcdoc`                |
| The newest snapshot, pre-release or RC        | `pip install --pre vanilla-mcdoc`          |
| A particular version, e.g. 26.1.2             | `pip install "vanilla-mcdoc==26.1.2.*"`    |

The package's version is the Minecraft version, padded to three numbers: 26.3 is `26.3.0`, and the snapshot
`26.4-snapshot-3` is `26.4.0a3` (pre-releases are `b`, release candidates `rc`). When the schemas are fixed or the
generator improves, that Minecraft version gets a new build: `26.3.0.post1`, `26.3.0.post2`, and so on. `==26.3.0.*`
always gets the newest build of 26.3. To check which one you have:

```python
import vanilla_mcdoc

vanilla_mcdoc.__minecraft_version__  # "26.3"
vanilla_mcdoc.__mcdoc_commit__       # The vanilla-mcdoc commit it was generated from
```

## Using it

Every schema is importable from a module that mirrors where vanilla-mcdoc defines it, e.g.
`vanilla_mcdoc.data.recipe.Smelting`, `vanilla_mcdoc.assets.item_definition.ItemModel`, or
`vanilla_mcdoc.world.item.ItemStackTemplate`. Names that only one module uses can also be imported straight from
`vanilla_mcdoc.data` or `vanilla_mcdoc.assets`, as in the example above.

**Models** (classes) validate with `Model.model_validate(data)`, or `Model(...)` with keyword arguments, like any
pydantic model. Invalid data raises pydantic's `ValidationError`, saying where and why:

```text
1 validation error for Smelting
cookingtime
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='slow', input_type=str]
```

**Unions** are type aliases rather than classes, e.g. a loot function can be any one of dozens of kinds, so they're
validated with a `TypeAdapter`, which gives you back the right model:

```python
from pydantic import TypeAdapter
from vanilla_mcdoc.data.loot.function.LootFunction import LootFunction

function = TypeAdapter(LootFunction).validate_python({"type": "minecraft:set_count", "count": 3})
type(function).__name__  # "LootFunctionSetCount"
```

Root resources, the ones that are files of their own in a pack, know which folder they go in, e.g.
`Smelting.__resource_dir__ == "recipe"`. `vanilla_mcdoc.root_resource_registry` lists all of them, in
`ROOT_DATAPACK_CLASSES` and `ROOT_RESOURCE_PACK_CLASSES`.

A few more things worth knowing:

- **Unknown keys are kept, not dropped**, so data the schemas don't cover yet survives a round trip.
- **Fields renamed to be valid Python** (e.g. `from` becomes `from_`) still read and write the real JSON key.
- **Resource locations** accept both forms: `"minecraft:stone"` and `"stone"`. Where vanilla-mcdoc lists a registry's
  entries, they're in its type too (e.g. `KnownItemId`), so your editor can autocomplete them.
- **The first time you use a model type in a program, it takes a second or two**, while pydantic builds that type's
  validator. After that, validating is fast.

## Where it comes from

The generator, and how the package gets published, live at
[UP929312/vanilla_mcdoc_to_python](https://github.com/UP929312/vanilla_mcdoc_to_python). It reads vanilla-mcdoc's
`symbols.json` (with the list of Minecraft versions from [misode/mcmeta](https://github.com/misode/mcmeta)), and checks
for updates every hour, so a new snapshot is usually on PyPI shortly after Spyglass has updated its schemas.

If something doesn't match what Minecraft accepts, it's either a gap in vanilla-mcdoc or a bug in the generator. Issues are welcome at the generator's repository.

This project isn't affiliated with Mojang, Microsoft or the Spyglass team.
