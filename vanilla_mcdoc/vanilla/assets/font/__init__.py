"""Vanilla's assets/font/ files"""
from vanilla_mcdoc.assets.font.Font import Font
from vanilla_mcdoc.assets.font.FontOption import FontOption
from vanilla_mcdoc.assets.font.GlyphProvider import GlyphProviderBitmap, GlyphProviderReference

ALT = Font(
    providers=[
        GlyphProviderReference(id='minecraft:include/space', type='reference'),
        GlyphProviderBitmap(
            file='minecraft:font/ascii_sga.png',
            ascent=7,
            chars=[
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00ABCDEFGHIJKLMNO',
                'PQRSTUVWXYZ\x00\x00\x00\x00\x00',
                '\x00abcdefghijklmno',
                'pqrstuvwxyz\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            ],
            type='bitmap',
        ),
    ],
)

DEFAULT = Font(
    providers=[
        GlyphProviderReference(id='minecraft:include/space', type='reference'),
        GlyphProviderReference(id='minecraft:include/default', type='reference', filter={FontOption.UNIFORM: False}),
        GlyphProviderReference(id='minecraft:include/unifont', type='reference'),
    ],
)

ILLAGERALT = Font(
    providers=[
        GlyphProviderReference(id='minecraft:include/space', type='reference'),
        GlyphProviderBitmap(
            file='minecraft:font/asciillager.png',
            ascent=7,
            chars=[
                '!,-.0123456789?a',
                'bcdefghijklmnopq',
                'rstuvwxyzABCDEFG',
                'HIJKLMNOPQRSTUVW',
                'XYZ\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            ],
            type='bitmap',
        ),
    ],
)

UNIFORM = Font(
    providers=[
        GlyphProviderReference(id='minecraft:include/space', type='reference'),
        GlyphProviderReference(id='minecraft:include/unifont', type='reference'),
    ],
)
