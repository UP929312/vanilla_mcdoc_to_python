"""Vanilla's data/test_instance/ files"""
from vanilla_mcdoc.data.gametest.TestInstance import TestInstanceFunction

ALWAYS_PASS = TestInstanceFunction(
    environment='minecraft:default',
    structure='minecraft:empty',
    max_ticks=1,
    setup_ticks=1,
    required=False,
    function='minecraft:always_pass',
    type='minecraft:function',
)
