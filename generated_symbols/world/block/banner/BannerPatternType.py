# Generated from symbols.json for ::java::world::block::banner::BannerPatternType
from enum import Enum


class BannerPatternType(Enum):
    BOTTOMSTRIPE = "bs"  # Bottom Stripe (Base)
    TOPSTRIPE = "ts"  # Top Stripe (Chief)
    LEFTSTRIPE = "ls"  # Left Stripe (Pale dexter)
    RIGHTSTRIPE = "rs"  # Right Stripe (Pale sinister)
    CENTERSTRIPEVERTICAL = "cs"  # Center Stripe (Vertical) (Pale)
    MIDDLESTRIPEHORIZONTAL = "ms"  # Middle Stripe (Horizontal) (Fess)
    DOWNRIGHTSTRIPE = "drs"  # Down Right Stripe (Bend)
    DOWNLEFTSTRIPE = "dls"  # Down Left Stripe (Bend sinister)
    SMALLVERTICALSTRIPES = "ss"  # Small (Vertical) Stripes (Paly)
    DIAGONALCROSS = "cr"  # Diagonal Cross (Saltire)
    SQUARECROSS = "sc"  # Square Cross (Cross)
    LEFTOFDIAGONAL = "ld"  # Left of Diagonal (Per bend sinister)
    RIGHTOFUPSIDEDOWNDIAGONAL = "rud"  # Right of upside-down Diagonal (Per bend)
    LEFTOFUPSIDEDOWNDIAGONAL = "lud"  # Left of upside-down Diagonal (Per bend inverted)
    RIGHTOFDIAGONAL = "rd"  # Right of Diagonal (Per bend sinister inverted)
    VERTICALHALFLEFT = "vh"  # Vertical Half (left) (Per pale)
    VERTICALHALFRIGHT = "vhr"  # Vertical Half (right) (Per pale inverted)
    HORIZONTALHALFTOP = "hh"  # Horizontal Half (top) (Per fess)
    HORIZONTALHALFBOTTOM = "hhb"  # Horizontal Half (bottom) (Per fess inverted)
    BOTTOMLEFTCORNER = "bl"  # Bottom Left Corner (Base dexter canton)
    BOTTOMRIGHTCORNER = "br"  # Bottom Right Corner (Base sinister canton)
    TOPLEFTCORNER = "tl"  # Top Left Corner (Chief dexter canton)
    TOPRIGHTCORNER = "tr"  # Top Right Corner (Chief sinister canton)
    BOTTOMTRIANGLE = "bt"  # Bottom Triangle (Chevron)
    TOPTRIANGLE = "tt"  # Top Triangle (Inverted chevron)
    BOTTOMTRIANGLESAWTOOTH = "bts"  # Bottom Triangle Sawtooth (Base indented)
    TOPTRIANGLESAWTOOTH = "tts"  # Top Triangle Sawtooth (Chief indented)
    MIDDLECIRCLE = "mc"  # Middle Circle (Roundel)
    MIDDLERHOMBUS = "mr"  # Middle Rhombus (Lozenge)
    BORDER = "bo"  # Border (Bordure)
    CURLYBORDER = "cbo"  # Curly Border (Bordure indented)
    BRICK = "bri"  # Brick (Field masoned)
    GRADIENT = "gra"  # Gradient (Gradient)
    GRADIENTUPSIDEDOWN = "gru"  # Gradient upside-down (Base gradient)
    CREEPER = "cre"  # Creeper (Creeper charge)
    SKULL = "sku"  # Skull (Skull charge)
    FLOWER = "flo"  # Flower (Flower charge)
    MOJANG = "moj"  # Mojang (Thing)
    GLOBE = "glb"  # Globe (Globe)
    PIGLIN = "pig"  # Piglin (Piglin)


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::banner::BannerPatternType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Bottom Stripe (Base)",
                "identifier": "BottomStripe",
                "value": "bs"
            },
            {
                "desc": "Top Stripe (Chief)",
                "identifier": "TopStripe",
                "value": "ts"
            },
            {
                "desc": "Left Stripe (Pale dexter)",
                "identifier": "LeftStripe",
                "value": "ls"
            },
            {
                "desc": "Right Stripe (Pale sinister)",
                "identifier": "RightStripe",
                "value": "rs"
            },
            {
                "desc": "Center Stripe (Vertical) (Pale)",
                "identifier": "CenterStripeVertical",
                "value": "cs"
            },
            {
                "desc": "Middle Stripe (Horizontal) (Fess)",
                "identifier": "MiddleStripeHorizontal",
                "value": "ms"
            },
            {
                "desc": "Down Right Stripe (Bend)",
                "identifier": "DownRightStripe",
                "value": "drs"
            },
            {
                "desc": "Down Left Stripe (Bend sinister)",
                "identifier": "DownLeftStripe",
                "value": "dls"
            },
            {
                "desc": "Small (Vertical) Stripes (Paly)",
                "identifier": "SmallVerticalStripes",
                "value": "ss"
            },
            {
                "desc": "Diagonal Cross (Saltire)",
                "identifier": "DiagonalCross",
                "value": "cr"
            },
            {
                "desc": "Square Cross (Cross)",
                "identifier": "SquareCross",
                "value": "sc"
            },
            {
                "desc": "Left of Diagonal (Per bend sinister)",
                "identifier": "LeftOfDiagonal",
                "value": "ld"
            },
            {
                "desc": "Right of upside-down Diagonal (Per bend)",
                "identifier": "RightOfUpsideDownDiagonal",
                "value": "rud"
            },
            {
                "desc": "Left of upside-down Diagonal (Per bend inverted)",
                "identifier": "LeftOfUpsideDownDiagonal",
                "value": "lud"
            },
            {
                "desc": "Right of Diagonal (Per bend sinister inverted)",
                "identifier": "RightOfDiagonal",
                "value": "rd"
            },
            {
                "desc": "Vertical Half (left) (Per pale)",
                "identifier": "VerticalHalfLeft",
                "value": "vh"
            },
            {
                "desc": "Vertical Half (right) (Per pale inverted)",
                "identifier": "VerticalHalfRight",
                "value": "vhr"
            },
            {
                "desc": "Horizontal Half (top) (Per fess)",
                "identifier": "HorizontalHalfTop",
                "value": "hh"
            },
            {
                "desc": "Horizontal Half (bottom) (Per fess inverted)",
                "identifier": "HorizontalHalfBottom",
                "value": "hhb"
            },
            {
                "desc": "Bottom Left Corner (Base dexter canton)",
                "identifier": "BottomLeftCorner",
                "value": "bl"
            },
            {
                "desc": "Bottom Right Corner (Base sinister canton)",
                "identifier": "BottomRightCorner",
                "value": "br"
            },
            {
                "desc": "Top Left Corner (Chief dexter canton)",
                "identifier": "TopLeftCorner",
                "value": "tl"
            },
            {
                "desc": "Top Right Corner (Chief sinister canton)",
                "identifier": "TopRightCorner",
                "value": "tr"
            },
            {
                "desc": "Bottom Triangle (Chevron)",
                "identifier": "BottomTriangle",
                "value": "bt"
            },
            {
                "desc": "Top Triangle (Inverted chevron)",
                "identifier": "TopTriangle",
                "value": "tt"
            },
            {
                "desc": "Bottom Triangle Sawtooth (Base indented)",
                "identifier": "BottomTriangleSawtooth",
                "value": "bts"
            },
            {
                "desc": "Top Triangle Sawtooth (Chief indented)",
                "identifier": "TopTriangleSawtooth",
                "value": "tts"
            },
            {
                "desc": "Middle Circle (Roundel)",
                "identifier": "MiddleCircle",
                "value": "mc"
            },
            {
                "desc": "Middle Rhombus (Lozenge)",
                "identifier": "MiddleRhombus",
                "value": "mr"
            },
            {
                "desc": "Border (Bordure)",
                "identifier": "Border",
                "value": "bo"
            },
            {
                "desc": "Curly Border (Bordure indented)",
                "identifier": "CurlyBorder",
                "value": "cbo"
            },
            {
                "desc": "Brick (Field masoned)",
                "identifier": "Brick",
                "value": "bri"
            },
            {
                "desc": "Gradient (Gradient)",
                "identifier": "Gradient",
                "value": "gra"
            },
            {
                "desc": "Gradient upside-down (Base gradient)",
                "identifier": "GradientUpsideDown",
                "value": "gru"
            },
            {
                "desc": "Creeper (Creeper charge)",
                "identifier": "Creeper",
                "value": "cre"
            },
            {
                "desc": "Skull (Skull charge)",
                "identifier": "Skull",
                "value": "sku"
            },
            {
                "desc": "Flower (Flower charge)",
                "identifier": "Flower",
                "value": "flo"
            },
            {
                "desc": "Mojang (Thing)",
                "identifier": "Mojang",
                "value": "moj"
            },
            {
                "desc": "Globe (Globe)",
                "identifier": "Globe",
                "value": "glb"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Piglin (Piglin)",
                "identifier": "Piglin",
                "value": "pig"
            }
        ]
    }
}

