"""Vanilla's data/tags/point_of_interest_type/ files"""
from vanilla_mcdoc.data.tag.Tag import Tag

ACQUIRABLE_JOB_SITE = Tag(
    values=[
        'minecraft:armorer',
        'minecraft:butcher',
        'minecraft:cartographer',
        'minecraft:cleric',
        'minecraft:farmer',
        'minecraft:fisherman',
        'minecraft:fletcher',
        'minecraft:leatherworker',
        'minecraft:librarian',
        'minecraft:mason',
        'minecraft:shepherd',
        'minecraft:toolsmith',
        'minecraft:weaponsmith',
    ],
)

BEE_HOME = Tag(values=['minecraft:beehive', 'minecraft:bee_nest'])

VILLAGE = Tag(values=['#minecraft:acquirable_job_site', 'minecraft:home', 'minecraft:meeting'])
