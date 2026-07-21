# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::ReputationPart
from enum import Enum


class ReputationPart(Enum):
    MAJORNEGATIVE = "major_negative"  # Caused by the villager being directly killed, increasing by 25 each time.  Increases others' `major_negative` by 15 when shared through gossip.  Decays by 10 every 20 minutes.
    MINORNEGATIVE = "minor_negative"  # Caused by the villager being directly hurt, increasing by 25 each time  Increases others' `major_negative` by 5 when shared through gossip.  Decays by 20 every 20 minutes.
    MAJORPOSITIVE = "major_positive"  # Caused by the villager being cured, is always set to 20.  Does not increase others' `major_positive` through gossip.  Does not decay.
    MINORPOSITIVE = "minor_positive"  # Caused by the villager being cured, is increased by 25 each time.  Increases others' `minor_positive` by 20 when shared through gossip.  Decays by 1 every 20 minutes.
    TRADING = "trading"  # Caused by trading with the villager, increasing by 2 each time.  Does not increase others' `trading` through gossip.  Decays by 2 every 20 minutes.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::ReputationPart": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Caused by the villager being directly killed, increasing by 25 each time.\n\nIncreases others' `major_negative` by 15 when shared through gossip.\n\nDecays by 10 every 20 minutes.",
                "identifier": "MajorNegative",
                "value": "major_negative"
            },
            {
                "desc": "Caused by the villager being directly hurt, increasing by 25 each time\n\nIncreases others' `major_negative` by 5 when shared through gossip.\n\nDecays by 20 every 20 minutes.",
                "identifier": "MinorNegative",
                "value": "minor_negative"
            },
            {
                "desc": "Caused by the villager being cured, is always set to 20.\n\nDoes not increase others' `major_positive` through gossip.\n\nDoes not decay.",
                "identifier": "MajorPositive",
                "value": "major_positive"
            },
            {
                "desc": "Caused by the villager being cured, is increased by 25 each time.\n\nIncreases others' `minor_positive` by 20 when shared through gossip.\n\nDecays by 1 every 20 minutes.",
                "identifier": "MinorPositive",
                "value": "minor_positive"
            },
            {
                "desc": "Caused by trading with the villager, increasing by 2 each time.\n\nDoes not increase others' `trading` through gossip.\n\nDecays by 2 every 20 minutes.",
                "identifier": "Trading",
                "value": "trading"
            }
        ]
    }
}

