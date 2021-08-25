from abc import abstractmethod


pl = [
    {
      "SKU": "10_CH.EVERGREEN_SILVER.BAY",
      "Available": 10
    },
    {
      "SKU": "10_SNAKE_LAURENTII",
      "Available": 22
    },
    {
      "SKU": "2_CACT_GRAFT_RED",
      "Available": 58
    },
    {
      "SKU": "2_SNAKE_STARFISH",
      "Available": 68
    },
    {
      "SKU": "4_ALOCASIA_BLACK.VELVET",
      "Available": 16
    },
    {
      "SKU": "4_ANTHURIUM_PINK",
      "Available": 28
    },
    {
      "SKU": "4_ANTHURIUM_PINK_BARE.ROOT",
      "Available": 28
    },
    {
      "SKU": "4_ANTHURIUM_PURPLE",
      "Available": 26
    },
    {
      "SKU": "4_ANTHURIUM_PURPLE_PP.WHT.TERRA",
      "Available": 17
    },
    {
      "SKU": "4_ANTHURIUM_RED",
      "Available": 16
    },
    {
      "SKU": "4_ANTHURIUM_RED_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_ANTHURIUM_WHITE",
      "Available": 49
    },
    {
      "SKU": "4_ARABICA_COFFEE",
      "Available": 125
    },
    {
      "SKU": "4_BROMELIAD_CHRISTIANE",
      "Available": 33
    },
    {
      "SKU": "4_BROMELIAD_CHRISTIANE_PP.HUEY",
      "Available": 33
    },
    {
      "SKU": "4_BROMELIAD_CYANEA",
      "Available": 26
    },
    {
      "SKU": "4_BROMELIAD_DONNA",
      "Available": 72
    },
    {
      "SKU": "4_BROMELIAD_FIREBALL",
      "Available": 14
    },
    {
      "SKU": "4_BROMELIAD_SPLENRIET",
      "Available": 62
    },
    {
      "SKU": "4_CALATHEA_BEAUTY.STAR",
      "Available": 103
    },
    {
      "SKU": "4_CALATHEA_DOTTIE",
      "Available": 14
    },
    {
      "SKU": "4_CALATHEA_FREDDIE",
      "Available": 82
    },
    {
      "SKU": "4_CALATHEA_FURRY.FEATHER",
      "Available": 39
    },
    {
      "SKU": "4_CALATHEA_GREY.STAR",
      "Available": 10
    },
    {
      "SKU": "4_CALATHEA_MAKOYANA",
      "Available": 140
    },
    {
      "SKU": "4_CALATHEA_MEDALLION",
      "Available": 80
    },
    {
      "SKU": "4_CALATHEA_MEDALLION_BARE.ROOT",
      "Available": 80
    },
    {
      "SKU": "4_CALATHEA_MEDALLION_PP.HUEY",
      "Available": 32
    },
    {
      "SKU": "4_CALATHEA_MEDALLION_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_CALATHEA_MEDALLION.II",
      "Available": 69
    },
    {
      "SKU": "4_CALATHEA_ORBIFOLIA",
      "Available": 10
    },
    {
      "SKU": "4_CALATHEA_ORNATA",
      "Available": 183
    },
    {
      "SKU": "4_CALATHEA_ORNATA_BARE.ROOT",
      "Available": 183
    },
    {
      "SKU": "4_CALATHEA_RATTLESNAKE",
      "Available": 63
    },
    {
      "SKU": "4_CALATHEA_RATTLESNAKE_BARE.ROOT",
      "Available": 63
    },
    {
      "SKU": "4_CALATHEA_VARIETY_2PK",
      "Available": 59
    },
    {
      "SKU": "4_CALATHEA_VITTATA",
      "Available": 30
    },
    {
      "SKU": "4_CALATHEA_WHITE.FUSION",
      "Available": 10
    },
    {
      "SKU": "4_CALATHEA_ZEBRINA",
      "Available": 32
    },
    {
      "SKU": "4_CH.EVERGREEN_LADY.VALENTINE",
      "Available": 18
    },
    {
      "SKU": "4_CH.EVERGREEN_SILVER.BAY",
      "Available": 28
    },
    {
      "SKU": "4_CROTON_GOLD.DUST",
      "Available": 169
    },
    {
      "SKU": "4_CROTON_MAMMY",
      "Available": 40
    },
    {
      "SKU": "4_CROTON_PETRA",
      "Available": 150
    },
    {
      "SKU": "4_CROTON_SUNNY.STAR",
      "Available": 86
    },
    {
      "SKU": "4_CROTON_VARIETY_2PK",
      "Available": 113
    },
    {
      "SKU": "4_CROTON_VARIETY_3PK",
      "Available": 75
    },
    {
      "SKU": "4_DIEFFENBACHIA_CAMILLE",
      "Available": 83
    },
    {
      "SKU": "4_DIEFFENBACHIA_CAMILLE_BARE.ROOT",
      "Available": 83
    },
    {
      "SKU": "4_DIEFFENBACHIA_CAMILLE_PP.HUEY",
      "Available": 74
    },
    {
      "SKU": "4_DIEFFENBACHIA_CAMILLE_PP.WHT.CYL",
      "Available": 74
    },
    {
      "SKU": "4_DRACAENA_COLORAMA",
      "Available": 37
    },
    {
      "SKU": "4_DRACAENA_JANET.CRAIG",
      "Available": 217
    },
    {
      "SKU": "4_DRACAENA_JANET.CRAIG_BARE.ROOT",
      "Available": 217
    },
    {
      "SKU": "4_DRACAENA_LEMON.LIME",
      "Available": 175
    },
    {
      "SKU": "4_DRACAENA_LUCKY.BAMBOO",
      "Available": 24
    },
    {
      "SKU": "4_DRACAENA_MAGENTA",
      "Available": 50
    },
    {
      "SKU": "4_DRACAENA_MARGINATA.CANE",
      "Available": 436
    },
    {
      "SKU": "4_DRACAENA_MARGINATA.CANE_PP.HUEY",
      "Available": 88
    },
    {
      "SKU": "4_DRACAENA_MARGINATA.CANE_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_DRACAENA_MARGINATA.CANE_PP.WHT.CYL",
      "Available": 167
    },
    {
      "SKU": "4_DRACAENA_MARGINATA.SUNRAY",
      "Available": 18
    },
    {
      "SKU": "4_DRACAENA_MASSANGEANA",
      "Available": 20
    },
    {
      "SKU": "4_DRACAENA_SONG.OF.INDIA",
      "Available": 198
    },
    {
      "SKU": "4_DRACAENA_SONG.OF.INDIA_PP.HUEY",
      "Available": 86
    },
    {
      "SKU": "4_DRACAENA_SONG.OF.INDIA_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_DRACAENA_SONG.OF.INDIA_PP.WHT.CYL",
      "Available": 86
    },
    {
      "SKU": "4_DRACAENA_STED.SOL.CANE",
      "Available": 26
    },
    {
      "SKU": "4_DRACAENA_STED.SOL.CANE_PP.HUEY",
      "Available": 26
    },
    {
      "SKU": "4_DRACAENA_STED.SOL.CANE_PP.WHT.CYL",
      "Available": 26
    },
    {
      "SKU": "4_DRACAENA_TORNADO",
      "Available": 26
    },
    {
      "SKU": "4_DRACAENA_VARIETY_3PK",
      "Available": 125
    },
    {
      "SKU": "4_DRACAENA_WHITE.JEWEL",
      "Available": 51
    },
    {
      "SKU": "4_EPIPHYLLUM_RIC.RAC.CACTUS",
      "Available": 25
    },
    {
      "SKU": "4_FERN_AUSTRAL.GEM",
      "Available": 259
    },
    {
      "SKU": "4_FERN_AUTUMN",
      "Available": 126
    },
    {
      "SKU": "4_FERN_BLUE.STAR",
      "Available": 89
    },
    {
      "SKU": "4_FERN_BLUE.STAR_PP.HUEY",
      "Available": 40
    },
    {
      "SKU": "4_FERN_BLUE.STAR_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_FERN_COTTON.CANDY",
      "Available": 96
    },
    {
      "SKU": "4_FERN_COTTON.CANDY_BARE.ROOT",
      "Available": 96
    },
    {
      "SKU": "4_FERN_EMINA",
      "Available": 57
    },
    {
      "SKU": "4_FERN_HEART",
      "Available": 94
    },
    {
      "SKU": "4_FERN_HEART",
      "Available": 68
    },
    {
      "SKU": "4_FERN_HEART",
      "Available": 24
    },
    {
      "SKU": "4_FERN_JESTER.CROWN",
      "Available": 85
    },
    {
      "SKU": "4_FERN_JESTER.CROWN_KOKEDAMA",
      "Available": 23
    },
    {
      "SKU": "4_FERN_JESTER.CROWN_KOKEDAMA.BEADS",
      "Available": 25
    },
    {
      "SKU": "4_FERN_JESTER.CROWN_PP.HUEY",
      "Available": 70
    },
    {
      "SKU": "4_FERN_JESTER.CROWN_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_FERN_JESTER.CROWN_PP.WHT.CYL",
      "Available": 70
    },
    {
      "SKU": "4_FERN_KANGAROO.PAW",
      "Available": 86
    },
    {
      "SKU": "4_FERN_LEMON.BUTTON",
      "Available": 163
    },
    {
      "SKU": "4_FERN_LEMON.BUTTON_BARE.ROOT",
      "Available": 79
    },
    {
      "SKU": "4_FERN_LEMON.BUTTON_PP.HUEY",
      "Available": 88
    },
    {
      "SKU": "4_FERN_LEMON.BUTTON_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_FERN_LEMON.BUTTON_PP.WHT.CYL",
      "Available": 139
    },
    {
      "SKU": "4_FERN_LESLIE",
      "Available": 78
    },
    {
      "SKU": "4_FERN_MAHOGANY",
      "Available": 49
    },
    {
      "SKU": "4_FERN_NIDUS",
      "Available": 182
    },
    {
      "SKU": "4_FERN_NIDUS_BARE.ROOT",
      "Available": 182
    },
    {
      "SKU": "4_FERN_RABBIT.FOOT",
      "Available": 147
    },
    {
      "SKU": "4_FERN_STAGHORN",
      "Available": 73
    },
    {
      "SKU": "4_FERN_STAGHORN_BARE.ROOT",
      "Available": 73
    },
    {
      "SKU": "4_FERN_VARIETY_2PK",
      "Available": 31
    },
    {
      "SKU": "4_FERN_VICTORIA",
      "Available": 71
    },
    {
      "SKU": "4_FICUS_AUDREY",
      "Available": 66
    },
    {
      "SKU": "4_FICUS_BURGUNDY",
      "Available": 129
    },
    {
      "SKU": "4_FICUS_GINSENG",
      "Available": 29
    },
    {
      "SKU": "4_FICUS_LYRATA",
      "Available": 136
    },
    {
      "SKU": "4_FICUS_LYRATA_BARE.ROOT",
      "Available": 136
    },
    {
      "SKU": "4_FICUS_RUBY.PINK",
      "Available": 46
    },
    {
      "SKU": "4_FICUS_TINEKE",
      "Available": 185
    },
    {
      "SKU": "4_FITTONIA_WHITE",
      "Available": 28
    },
    {
      "SKU": "4_GUZMANIA_ORANGE",
      "Available": 33
    },
    {
      "SKU": "4_GUZMANIA_ROSE",
      "Available": 14
    },
    {
      "SKU": "4_GUZMANIA_YELLOW",
      "Available": 15
    },
    {
      "SKU": "4_HOYA_GRASS.LEAFED",
      "Available": 53
    },
    {
      "SKU": "4_HOYA_HEART",
      "Available": 160
    },
    {
      "SKU": "4_HOYA_HEART.VARIEGATED",
      "Available": 66
    },
    {
      "SKU": "4_HOYA_HOPE",
      "Available": 18
    },
    {
      "SKU": "4_HOYA_STRING.BEAN",
      "Available": 30
    },
    {
      "SKU": "4_HOYA_TRICOLOR",
      "Available": 52
    },
    {
      "SKU": "4_HYPOESTES_RED",
      "Available": 12
    },
    {
      "SKU": "4_HYPOESTES_WHITE",
      "Available": 12
    },
    {
      "SKU": "4_IVY_GLACIER",
      "Available": 78
    },
    {
      "SKU": "4_IVY_GLACIER_PP.HUEY",
      "Available": 54
    },
    {
      "SKU": "4_IVY_GLACIER_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_IVY_GLACIER_PP.WHT.CYL",
      "Available": 54
    },
    {
      "SKU": "4_IVY_GOLD.CHILD",
      "Available": 115
    },
    {
      "SKU": "4_IVY_GOLD.CHILD_KOKEDAMA",
      "Available": 20
    },
    {
      "SKU": "4_IVY_GOLD.CHILD_KOKEDAMA.BEADS",
      "Available": 20
    },
    {
      "SKU": "4_IVY_GREEN",
      "Available": 141
    },
    {
      "SKU": "4_IVY_GREEN_PP.HUEY",
      "Available": 88
    },
    {
      "SKU": "4_IVY_GREEN_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_IVY_VARIETY_2PK",
      "Available": 110
    },
    {
      "SKU": "4_IVY_VARIETY_3PK",
      "Available": 78
    },
    {
      "SKU": "4_LIPSTICK_BLACK.PAGODA",
      "Available": 40
    },
    {
      "SKU": "4_LIPSTICK_CLASSIC",
      "Available": 84
    },
    {
      "SKU": "4_MARANTA_LEMON.LIME",
      "Available": 60
    },
    {
      "SKU": "4_MARANTA_LEUCONEURA",
      "Available": 174
    },
    {
      "SKU": "4_MARANTA_RED",
      "Available": 116
    },
    {
      "SKU": "4_MONSTERA_DELICIOSA",
      "Available": 467
    },
    {
      "SKU": "4_MONSTERA_DELICIOSA_BARE.ROOT",
      "Available": 467
    },
    {
      "SKU": "4_MONSTERA_DELICIOSA_PP.HUEY",
      "Available": 88
    },
    {
      "SKU": "4_MONSTERA_DELICIOSA_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_MONSTERA_DELICIOSA_PP.WHT.CYL",
      "Available": 85
    },
    {
      "SKU": "4_MONSTERA_MINIMA",
      "Available": 886
    },
    {
      "SKU": "4_MONSTERA_SWISS.CHEESE",
      "Available": 33
    },
    {
      "SKU": "4_MYSTERY",
      "Available": 117
    },
    {
      "SKU": "4_MYSTERY_B.GRADE",
      "Available": 117
    },
    {
      "SKU": "4_MYSTERY_PET.FRIENDLY_A.GRADE",
      "Available": 118
    },
    {
      "SKU": "4_MYSTERY_PET.FRIENDLY_B.GRADE",
      "Available": 119
    },
    {
      "SKU": "4_MYSTERY_SUCCULENT",
      "Available": 120
    },
    {
      "SKU": "4_MYSTERY_SUCCULENT_B.GRADE",
      "Available": 119
    },
    {
      "SKU": "4_NETTLE_BABY.TEAR",
      "Available": 10
    },
    {
      "SKU": "4_PACHIRA_BRAID",
      "Available": 78
    },
    {
      "SKU": "4_PALM_ARECA",
      "Available": 52
    },
    {
      "SKU": "4_PALM_PARLOR",
      "Available": 33
    },
    {
      "SKU": "4_PALM_PARLOR_BARE.ROOT",
      "Available": 33
    },
    {
      "SKU": "4_PALM_PARLOR_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_PALM_PONYTAIL",
      "Available": 24
    },
    {
      "SKU": "4_PEPEROMIA_CUPID",
      "Available": 19
    },
    {
      "SKU": "4_PEPEROMIA_GINNY",
      "Available": 43
    },
    {
      "SKU": "4_PEPEROMIA_GREEN.BEAN",
      "Available": 19
    },
    {
      "SKU": "4_PEPEROMIA_MARBLE",
      "Available": 120
    },
    {
      "SKU": "4_PEPEROMIA_PARALLEL",
      "Available": 21
    },
    {
      "SKU": "4_PEPEROMIA_RANA.VERDE",
      "Available": 65
    },
    {
      "SKU": "4_PEPEROMIA_RED.STEMMED",
      "Available": 55
    },
    {
      "SKU": "4_PEPEROMIA_RIPPLE.RED",
      "Available": 41
    },
    {
      "SKU": "4_PEPEROMIA_THAILAND",
      "Available": 241
    },
    {
      "SKU": "4_PEPEROMIA_WATERMELON",
      "Available": 132
    },
    {
      "SKU": "4_PHILODENDRON_BIRKIN",
      "Available": 628
    },
    {
      "SKU": "4_PHILODENDRON_BLACK.CARDINAL",
      "Available": 13
    },
    {
      "SKU": "4_PHILODENDRON_BRASIL",
      "Available": 182
    },
    {
      "SKU": "4_PHILODENDRON_BRASIL_KOKEDAMA",
      "Available": 20
    },
    {
      "SKU": "4_PHILODENDRON_BRASIL_KOKEDAMA.BEADS",
      "Available": 20
    },
    {
      "SKU": "4_PHILODENDRON_CONGO.GREEN",
      "Available": 86
    },
    {
      "SKU": "4_PHILODENDRON_CORDATUM",
      "Available": 152
    },
    {
      "SKU": "4_PHILODENDRON_CORDATUM_PP.HUEY",
      "Available": 34
    },
    {
      "SKU": "4_PHILODENDRON_CORDATUM_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_PHILODENDRON_CORDATUM_PP.WHT.CYL",
      "Available": 34
    },
    {
      "SKU": "4_PHILODENDRON_MOONLIGHT",
      "Available": 277
    },
    {
      "SKU": "4_PHILODENDRON_NEON",
      "Available": 14
    },
    {
      "SKU": "4_PHILODENDRON_PRINCE.ORANGE",
      "Available": 100
    },
    {
      "SKU": "4_PHILODENDRON_VARIETY_2PK",
      "Available": 152
    },
    {
      "SKU": "4_PHILODENDRON_VELVET",
      "Available": 65
    },
    {
      "SKU": "4_PILEA_CH.MONEY_PP.HUEY",
      "Available": 79
    },
    {
      "SKU": "4_PILEA_PEPEROMIODES",
      "Available": 79
    },
    {
      "SKU": "4_PILEA_PEPEROMIODES_KOKEDAMA",
      "Available": 19
    },
    {
      "SKU": "4_PILEA_PEPEROMIODES_KOKEDAMA.BEADS",
      "Available": 20
    },
    {
      "SKU": "4_PILEA_PEPEROMIOIDES.WOOD",
      "Available": 31
    },
    {
      "SKU": "4_POTHOS_GOLDEN",
      "Available": 83
    },
    {
      "SKU": "4_POTHOS_GOLDEN_KOKEDAMA",
      "Available": 18
    },
    {
      "SKU": "4_POTHOS_GOLDEN_KOKEDAMA.BEADS",
      "Available": 20
    },
    {
      "SKU": "4_POTHOS_GOLDEN_PP.HUEY",
      "Available": 28
    },
    {
      "SKU": "4_POTHOS_GOLDEN_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_POTHOS_GOLDEN_PP.WHT.CYL",
      "Available": 28
    },
    {
      "SKU": "4_POTHOS_GREEN",
      "Available": 78
    },
    {
      "SKU": "4_POTHOS_NEON",
      "Available": 161
    },
    {
      "SKU": "4_POTHOS_NJOY",
      "Available": 65
    },
    {
      "SKU": "4_POTHOS_NJOY_KOKEDAMA",
      "Available": 18
    },
    {
      "SKU": "4_POTHOS_NJOY_KOKEDAMA.BEADS",
      "Available": 19
    },
    {
      "SKU": "4_POTHOS_SILVER.SPLASH",
      "Available": 64
    },
    {
      "SKU": "4_POTHOS_VARIETY_2PK",
      "Available": 28
    },
    {
      "SKU": "4_PRE.TERRA_HOYA_HEART.VAR",
      "Available": 10
    },
    {
      "SKU": "4_SCHEFFLERA_ARBORICOLA",
      "Available": 163
    },
    {
      "SKU": "4_SCHEFFLERA_MOONDROP",
      "Available": 81
    },
    {
      "SKU": "4_SCHEFFLERA_VARIEGATED",
      "Available": 91
    },
    {
      "SKU": "4_SCHEFFLERA_VARIETY_2PK",
      "Available": 81
    },
    {
      "SKU": "4_SNAKE_BLACK.GOLD",
      "Available": 45
    },
    {
      "SKU": "4_SNAKE_BRAID",
      "Available": 47
    },
    {
      "SKU": "4_SNAKE_EMERALD.STAR",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_FOREST.STAR",
      "Available": 49
    },
    {
      "SKU": "4_SNAKE_JADE.STAR",
      "Available": 69
    },
    {
      "SKU": "4_SNAKE_LAURENTII",
      "Available": 134
    },
    {
      "SKU": "4_SNAKE_LAURENTII_BARE.ROOT",
      "Available": 134
    },
    {
      "SKU": "4_SNAKE_LAURENTII_PP.HUEY",
      "Available": 88
    },
    {
      "SKU": "4_SNAKE_LAURENTII_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_SNAKE_LAURENTII_PP.WHT.CYL",
      "Available": 101
    },
    {
      "SKU": "4_SNAKE_MISTY.STAR",
      "Available": 127
    },
    {
      "SKU": "4_SNAKE_OCEAN.STAR",
      "Available": 58
    },
    {
      "SKU": "4_SNAKE_OCEAN.STAR_PP.HUEY",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_OCEAN.STAR_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_SNAKE_SILVER.STREAK",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_STARFISH",
      "Available": 11
    },
    {
      "SKU": "4_SNAKE_STUCKII",
      "Available": 130
    },
    {
      "SKU": "4_SNAKE_TWIST",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_VARIETY_2PK",
      "Available": 49
    },
    {
      "SKU": "4_SNAKE_VARIETY_3PK",
      "Available": 32
    },
    {
      "SKU": "4_SNAKE_VARIETY_4PK",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_VARIETY_5PK",
      "Available": 16
    },
    {
      "SKU": "4_SNAKE_ZEYLANICA",
      "Available": 209
    },
    {
      "SKU": "4_SNAKE_ZEYLANICA_BARE.ROOT",
      "Available": 209
    },
    {
      "SKU": "4_SPATHIPHYLLUM_GREEN",
      "Available": 43
    },
    {
      "SKU": "4_SPIDER_BONNIE",
      "Available": 60
    },
    {
      "SKU": "4_SPIDER_HAWAIIAN",
      "Available": 51
    },
    {
      "SKU": "4_SPIDER_REVERSE",
      "Available": 105
    },
    {
      "SKU": "4_STROMANTHE_SANGUINEA",
      "Available": 13
    },
    {
      "SKU": "4_STROMANTHE_TRIOSTAR",
      "Available": 38
    },
    {
      "SKU": "4_SUCC_AEONIUM_SUNBURST",
      "Available": 50
    },
    {
      "SKU": "4_SUCC_AGAVE_QUADRICOLOR",
      "Available": 29
    },
    {
      "SKU": "4_SUCC_AGAVE_VILMORINIANA",
      "Available": 15
    },
    {
      "SKU": "4_SUCC_ALOE_VERA",
      "Available": 81
    },
    {
      "SKU": "4_SUCC_ALOE_VERA_PP.HUEY",
      "Available": 77
    },
    {
      "SKU": "4_SUCC_ALOE_VERA_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_SUCC_ALOE_VERA_PP.WHT.CYL",
      "Available": 56
    },
    {
      "SKU": "4_SUCC_CACTUS_LIFESAVER",
      "Available": 20
    },
    {
      "SKU": "4_SUCC_CRASSULA_FALCATA",
      "Available": 41
    },
    {
      "SKU": "4_SUCC_CRASSULA_JADE",
      "Available": 111
    },
    {
      "SKU": "4_SUCC_CRASSULA_JADE.GOLLUM",
      "Available": 99
    },
    {
      "SKU": "4_SUCC_CRASSULA_JADE.RIPPLE",
      "Available": 29
    },
    {
      "SKU": "4_SUCC_CRASSULA_SILVER.DOLLAR",
      "Available": 97
    },
    {
      "SKU": "4_SUCC_ECHEVERIA_LILICANA",
      "Available": 40
    },
    {
      "SKU": "4_SUCC_ECHEVERIA_PERLE.VON.NURNBERG",
      "Available": 40
    },
    {
      "SKU": "4_SUCC_FISHHOOKS_PP.HUEY",
      "Available": 24
    },
    {
      "SKU": "4_SUCC_GRAPTOSEDUM_VERA.HIGGINS",
      "Available": 118
    },
    {
      "SKU": "4_SUCC_KALANCHOE_CHOCO.SOLDIER",
      "Available": 33
    },
    {
      "SKU": "4_SUCC_KLEINIA_PICKLE.PLANT",
      "Available": 82
    },
    {
      "SKU": "4_SUCC_PORTULACARIA_RAINBOW.BUSH",
      "Available": 132
    },
    {
      "SKU": "4_SUCC_SENECIO_FISHHOOKS",
      "Available": 24
    },
    {
      "SKU": "4_SUCC_SENECIO_STRING.OF.BANANAS",
      "Available": 26
    },
    {
      "SKU": "4_SUCC_SENECIO_STRING.OF.DOLPHINS",
      "Available": 46
    },
    {
      "SKU": "4_SUCC_SENECIO_STRING.OF.HEARTS",
      "Available": 11
    },
    {
      "SKU": "4_SUCC_STRING.OF.DOLPHINS_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_SUCC_VARIETY_2PK",
      "Available": 56
    },
    {
      "SKU": "4_SYNGONIUM_GOLD",
      "Available": 66
    },
    {
      "SKU": "4_SYNGONIUM_STRAWBERRY",
      "Available": 83
    },
    {
      "SKU": "4_SYNGONIUM_VARIETY_2PK",
      "Available": 66
    },
    {
      "SKU": "4_SYNGONIUM_VARIETY_3PK",
      "Available": 33
    },
    {
      "SKU": "4_SYNGONIUM_WHITE.BUTTERFLY",
      "Available": 95
    },
    {
      "SKU": "4_SYNGONIUM_WHITE.BUTTERFLY_BARE.ROOT",
      "Available": 95
    },
    {
      "SKU": "4_TRADESCANTIA_MOSES.IN.THE.CRADLE",
      "Available": 39
    },
    {
      "SKU": "4_ZAMIOCULCAS_ZAMIIFOLIA",
      "Available": 98
    },
    {
      "SKU": "4_ZAMIOCULCAS_ZAMIIFOLIA_PP.HUEY",
      "Available": 66
    },
    {
      "SKU": "4_ZAMIOCULCAS_ZAMIIFOLIA_PP.NAVARRO",
      "Available": 15
    },
    {
      "SKU": "4_ZAMIOCULCAS_ZAMIIFOLIA_PP.WHT.CYL",
      "Available": 66
    },
    {
      "SKU": "4_ZZ_BARE.ROOT",
      "Available": 98
    },
    {
      "SKU": "6_ANTHURIUM_PINK",
      "Available": 42
    },
    {
      "SKU": "6_ANTHURIUM_RED",
      "Available": 39
    },
    {
      "SKU": "6_ANTHURIUM_RED_PP.BLK.CYL",
      "Available": 15
    },
    {
      "SKU": "6_ANTHURIUM_RED_PP.WHT.CYL",
      "Available": 30
    },
    {
      "SKU": "6_ANTHURIUM_WHITE",
      "Available": 50
    },
    {
      "SKU": "6_ARALIA_MING.STUMP",
      "Available": 60
    },
    {
      "SKU": "6_BROMELIAD_MEDUSA",
      "Available": 54
    },
    {
      "SKU": "6_CALATHEA_BEAUTY.STAR",
      "Available": 11
    },
    {
      "SKU": "6_CALATHEA_GREY.STAR",
      "Available": 10
    },
    {
      "SKU": "6_CALATHEA_MEDALLION",
      "Available": 51
    },
    {
      "SKU": "6_CALATHEA_MEDALLION.II",
      "Available": 28
    },
    {
      "SKU": "6_CALATHEA_RATTLESNAKE",
      "Available": 65
    },
    {
      "SKU": "6_CH.EVERGREEN_SILVER.BAY",
      "Available": 58
    },
    {
      "SKU": "6_CROTON_MAMMY",
      "Available": 36
    },
    {
      "SKU": "6_CROTON_PETRA",
      "Available": 21
    },
    {
      "SKU": "6_DIEFFENBACHIA_CAMILLE",
      "Available": 31
    },
    {
      "SKU": "6_DIEFFENBACHIA_TROPIC.SNOW",
      "Available": 10
    },
    {
      "SKU": "6_DRACAENA_COLORAMA",
      "Available": 10
    },
    {
      "SKU": "6_DRACAENA_JANET.CRAIG",
      "Available": 25
    },
    {
      "SKU": "6_DRACAENA_LEMON.LIME",
      "Available": 42
    },
    {
      "SKU": "6_DRACAENA_LIMELIGHT",
      "Available": 37
    },
    {
      "SKU": "6_DRACAENA_LUCKY.BAMBOO",
      "Available": 10
    },
    {
      "SKU": "6_DRACAENA_MAGENTA",
      "Available": 10
    },
    {
      "SKU": "6_DRACAENA_MARGINATA.CANE",
      "Available": 21
    },
    {
      "SKU": "6_DRACAENA_SONG.OF.INDIA",
      "Available": 12
    },
    {
      "SKU": "6_EPIPHYLLUM_RIC.RAC.CACTUS",
      "Available": 92
    },
    {
      "SKU": "6_FERN_ALBO",
      "Available": 210
    },
    {
      "SKU": "6_FERN_AUTUMN",
      "Available": 20
    },
    {
      "SKU": "6_FERN_BLUE.STAR",
      "Available": 22
    },
    {
      "SKU": "6_FERN_KANGAROO.PAW",
      "Available": 14
    },
    {
      "SKU": "6_FERN_LEMON.BUTTON",
      "Available": 10
    },
    {
      "SKU": "6_FERN_MAIDENHAIR",
      "Available": 22
    },
    {
      "SKU": "6_FERN_STAGHORN",
      "Available": 56
    },
    {
      "SKU": "6_FICUS_BURGUNDY",
      "Available": 56
    },
    {
      "SKU": "6_FICUS_GINSENG",
      "Available": 19
    },
    {
      "SKU": "6_FICUS_LYRATA",
      "Available": 41
    },
    {
      "SKU": "6_FICUS_RUBY.PINK",
      "Available": 28
    },
    {
      "SKU": "6_FICUS_TINEKE",
      "Available": 44
    },
    {
      "SKU": "6_GUZMANIA_ORANGE",
      "Available": 18
    },
    {
      "SKU": "6_GUZMANIA_RED",
      "Available": 10
    },
    {
      "SKU": "6_HOYA_CARNOSA",
      "Available": 74
    },
    {
      "SKU": "6_HOYA_TRICOLOR",
      "Available": 52
    },
    {
      "SKU": "6_IVY_GOLD.CHILD",
      "Available": 15
    },
    {
      "SKU": "6_LIPSTICK_BLACK.PAGODA",
      "Available": 20
    },
    {
      "SKU": "6_LIPSTICK_CLASSIC",
      "Available": 18
    },
    {
      "SKU": "6_MARANTA_RED",
      "Available": 10
    },
    {
      "SKU": "6_MONSTERA_DELICIOSA",
      "Available": 229
    },
    {
      "SKU": "6_MONSTERA_SWISS.CHEESE",
      "Available": 13
    },
    {
      "SKU": "6_MYSTERY",
      "Available": 69
    },
    {
      "SKU": "6_MYSTERY_B.GRADE",
      "Available": 69
    },
    {
      "SKU": "6_MYSTERY_PET.FRIENDLY_A.GRADE",
      "Available": 70
    },
    {
      "SKU": "6_MYSTERY_PET.FRIENDLY_B.GRADE",
      "Available": 70
    },
    {
      "SKU": "6_NEMATANTHUS_CANDY.CORN",
      "Available": 26
    },
    {
      "SKU": "6_PACHIRA_BRAID",
      "Available": 41
    },
    {
      "SKU": "6_PALM_ARECA",
      "Available": 11
    },
    {
      "SKU": "6_PALM_PONYTAIL",
      "Available": 33
    },
    {
      "SKU": "6_PALM_SAGO",
      "Available": 15
    },
    {
      "SKU": "6_PEPEROMIA_GINNY",
      "Available": 20
    },
    {
      "SKU": "6_PEPEROMIA_MARBLE",
      "Available": 15
    },
    {
      "SKU": "6_PEPEROMIA_RANA.VERDE",
      "Available": 15
    },
    {
      "SKU": "6_PEPEROMIA_ROSSO",
      "Available": 16
    },
    {
      "SKU": "6_PEPEROMIA_WATERMELON",
      "Available": 27
    },
    {
      "SKU": "6_PHILODENDRON_BIRKIN",
      "Available": 30
    },
    {
      "SKU": "6_PHILODENDRON_BRASIL",
      "Available": 125
    },
    {
      "SKU": "6_PHILODENDRON_CONGO.ROJO",
      "Available": 20
    },
    {
      "SKU": "6_PHILODENDRON_CORDATUM",
      "Available": 177
    },
    {
      "SKU": "6_PILEA_BRONZE",
      "Available": 20
    },
    {
      "SKU": "6_POTHOS_GOLDEN",
      "Available": 110
    },
    {
      "SKU": "6_POTHOS_NEON",
      "Available": 17
    },
    {
      "SKU": "6_POTHOS_NJOY",
      "Available": 20
    },
    {
      "SKU": "6_POTHOS_SILVER.SPLASH",
      "Available": 10
    },
    {
      "SKU": "6_POTHOS_SNOW.QUEEN",
      "Available": 11
    },
    {
      "SKU": "6_SCHEFFLERA_ARBORICOLA",
      "Available": 21
    },
    {
      "SKU": "6_SCHEFFLERA_MOONDROP",
      "Available": 54
    },
    {
      "SKU": "6_SCHEFFLERA_VARIEGATED",
      "Available": 33
    },
    {
      "SKU": "6_SNAKE_BLACK.GOLD",
      "Available": 10
    },
    {
      "SKU": "6_SNAKE_JADE.STAR",
      "Available": 15
    },
    {
      "SKU": "6_SNAKE_LAURENTII",
      "Available": 215
    },
    {
      "SKU": "6_SNAKE_VARIETY_2PK",
      "Available": 177
    },
    {
      "SKU": "6_SNAKE_ZEYLANICA",
      "Available": 209
    },
    {
      "SKU": "6_SPATHIPHYLLUM_GREEN",
      "Available": 135
    },
    {
      "SKU": "6_SPIDER_GREEN",
      "Available": 10
    },
    {
      "SKU": "6_SPIDER_REVERSE",
      "Available": 24
    },
    {
      "SKU": "6_STROMANTHE_TRIOSTAR",
      "Available": 82
    },
    {
      "SKU": "6_SUCC_ALOE_VERA",
      "Available": 20
    },
    {
      "SKU": "6_SUCC_SENECIO_FISHHOOKS",
      "Available": 30
    },
    {
      "SKU": "6_SUCC_SENECIO_STRING.OF.BANANAS",
      "Available": 28
    },
    {
      "SKU": "6_SUCC_SENECIO_STRING.OF.HEARTS",
      "Available": 10
    },
    {
      "SKU": "6_ZAMIOCULCAS_ZAMIIFOLIA",
      "Available": 196
    },
    {
      "SKU": "8_SCHEFFLERA_VARIEGATED",
      "Available": 10
    },
    {
      "SKU": "8_SNAKE_LAURENTII",
      "Available": 10
    },
    {
      "SKU": "ACC_300ML.HUMIDIFIER",
      "Available": 18
    },
    {
      "SKU": "ACC_AUTO.WATERER",
      "Available": 99
    },
    {
      "SKU": "ACC_BUTTON_5PK",
      "Available": 10
    },
    {
      "SKU": "ACC_CLOTHES_APRON",
      "Available": 24
    },
    {
      "SKU": "ACC_COLD.PROTECT_L",
      "Available": 199
    },
    {
      "SKU": "ACC_COLD.PROTECT_M",
      "Available": 200
    },
    {
      "SKU": "ACC_EYE.DROPPER_5PK",
      "Available": 47
    },
    {
      "SKU": "ACC_GLOVE_GARDEN_L",
      "Available": 15
    },
    {
      "SKU": "ACC_GLOVE_GARDEN_M",
      "Available": 14
    },
    {
      "SKU": "ACC_GLOVE_GARDEN_S",
      "Available": 15
    },
    {
      "SKU": "ACC_GROW.WALL_BLACK",
      "Available": 21
    },
    {
      "SKU": "ACC_GROW.WALL_GREEN",
      "Available": 20
    },
    {
      "SKU": "ACC_HAND_CERAMIC",
      "Available": 13
    },
    {
      "SKU": "ACC_HEAT.PACK_72",
      "Available": 4782
    },
    {
      "SKU": "ACC_HPS.STICKER_PLANT.LADY",
      "Available": 36
    },
    {
      "SKU": "ACC_HPS.STICKER_TOO.MANY.PLANTS",
      "Available": 36
    },
    {
      "SKU": "ACC_HPS.STICKER_YOU.GROW.GIRL",
      "Available": 24
    },
    {
      "SKU": "ACC_JOYFUL.DIRT_ALL.PURPOSE",
      "Available": 54
    },
    {
      "SKU": "ACC_JOYFUL.DIRT_HOUSEPLANT",
      "Available": 31
    },
    {
      "SKU": "ACC_JOYFUL.DIRT_SUCCULENT",
      "Available": 36
    },
    {
      "SKU": "ACC_LAVA.ROCK_HPS_MIX",
      "Available": 1980
    },
    {
      "SKU": "ACC_LED_FLEX",
      "Available": 524
    },
    {
      "SKU": "ACC_MACRAME",
      "Available": 13
    },
    {
      "SKU": "ACC_MAGNET_CACTUS",
      "Available": 50
    },
    {
      "SKU": "ACC_METAL.ANIMAL_FROG",
      "Available": 35
    },
    {
      "SKU": "ACC_METAL.ANIMAL_MONKEY",
      "Available": 34
    },
    {
      "SKU": "ACC_METAL.PLANT.FLAG",
      "Available": 20
    },
    {
      "SKU": "ACC_METER_MOISTER",
      "Available": 495
    },
    {
      "SKU": "ACC_METER_PH",
      "Available": 34
    },
    {
      "SKU": "ACC_MODSPROUT_MASON.JAR_PARSLEY",
      "Available": 17
    },
    {
      "SKU": "ACC_MOSS_BLUE",
      "Available": 132
    },
    {
      "SKU": "ACC_MOSS_CHARTREUSE",
      "Available": 131
    },
    {
      "SKU": "ACC_MOSS_DARK.GREEN",
      "Available": 132
    },
    {
      "SKU": "ACC_MOSS_FUCHSIA",
      "Available": 131
    },
    {
      "SKU": "ACC_MOSS.POLE",
      "Available": 128
    },
    {
      "SKU": "ACC_NEEM.OIL.CONCENTRATE",
      "Available": 27
    },
    {
      "SKU": "ACC_PIN_CACTUS",
      "Available": 19
    },
    {
      "SKU": "ACC_PIN_CACTUS.HEART",
      "Available": 29
    },
    {
      "SKU": "ACC_PLANT.STICK_EYE_17IN",
      "Available": 50
    },
    {
      "SKU": "ACC_PLANT.STICK_LEAF_17IN",
      "Available": 39
    },
    {
      "SKU": "ACC_PLANT.STICK_PARADISE_17IN",
      "Available": 32
    },
    {
      "SKU": "ACC_PLASTIC.SAUCER_10IN",
      "Available": 28
    },
    {
      "SKU": "ACC_PLASTIC.SAUCER_4IN",
      "Available": 28
    },
    {
      "SKU": "ACC_PLASTIC.SAUCER_6IN",
      "Available": 30
    },
    {
      "SKU": "ACC_POSTER_ALBO",
      "Available": 22
    },
    {
      "SKU": "ACC_POSTER_FERN",
      "Available": 22
    },
    {
      "SKU": "ACC_POSTER_FIDDLE.LEAF",
      "Available": 23
    },
    {
      "SKU": "ACC_POSTER_PLANT.SPECIES",
      "Available": 18
    },
    {
      "SKU": "ACC_PROPAGATION_WIRE.L",
      "Available": 18
    },
    {
      "SKU": "ACC_PROPAGATION_WIRE.M",
      "Available": 17
    },
    {
      "SKU": "ACC_SCISSOR_HERB",
      "Available": 14
    },
    {
      "SKU": "ACC_SHEAR_MINI.SNIPPER",
      "Available": 41
    },
    {
      "SKU": "ACC_SHEAR_STAINLESS.STEEL",
      "Available": 10
    },
    {
      "SKU": "ACC_SOAP_TRUE.GRIT",
      "Available": 19
    },
    {
      "SKU": "ACC_SOCK_LONG_BLUE",
      "Available": 19
    },
    {
      "SKU": "ACC_SOCK_SHORT_PURPLE",
      "Available": 20
    },
    {
      "SKU": "ACC_SOIL_BIOCHAR",
      "Available": 102
    },
    {
      "SKU": "ACC_SOIL_FIDDLE.LEAF",
      "Available": 39
    },
    {
      "SKU": "ACC_SOIL_INDOOR_HPS",
      "Available": 1987
    },
    {
      "SKU": "ACC_SOIL_NOOT.MIX",
      "Available": 46
    },
    {
      "SKU": "ACC_SOIL_SUCCULENT_HPS",
      "Available": 1995
    },
    {
      "SKU": "ACC_SPRAY.WHITE_300ML",
      "Available": 167
    },
    {
      "SKU": "ACC_THERMOMETER",
      "Available": 19
    },
    {
      "SKU": "ACC_TOTE_DO.SOMETHING",
      "Available": 24
    },
    {
      "SKU": "ACC_TOTE_MORE.PLANTS",
      "Available": 20
    },
    {
      "SKU": "ACC_WATERING.CAN_BLACK_SHORT",
      "Available": 46
    },
    {
      "SKU": "ACC_WATERING.CAN_BLACK_TALL",
      "Available": 16
    },
    {
      "SKU": "ACC_WATERING.CAN_SQUEEZE",
      "Available": 83
    },
    {
      "SKU": "AIR_ADREANA",
      "Available": 43
    },
    {
      "SKU": "AIR_ADREANA_FERT",
      "Available": 37
    },
    {
      "SKU": "AIR_ARAUJEI",
      "Available": 15
    },
    {
      "SKU": "AIR_BAILEYI",
      "Available": 15
    },
    {
      "SKU": "AIR_BANDENSIS",
      "Available": 25
    },
    {
      "SKU": "AIR_BERGERI",
      "Available": 73
    },
    {
      "SKU": "AIR_BERGERI_5PK",
      "Available": 13
    },
    {
      "SKU": "AIR_BERGERI_FERT",
      "Available": 49
    },
    {
      "SKU": "AIR_BRACHYCAULOS",
      "Available": 54
    },
    {
      "SKU": "AIR_BRACHYCAULOS_2PK",
      "Available": 27
    },
    {
      "SKU": "AIR_BRACHYCAULOS_3PK",
      "Available": 18
    },
    {
      "SKU": "AIR_BRACHYCAULOS_5PK",
      "Available": 10
    },
    {
      "SKU": "AIR_BULBOSA",
      "Available": 79
    },
    {
      "SKU": "AIR_BULBOSA_3PK",
      "Available": 26
    },
    {
      "SKU": "AIR_BULBOSA_5PK",
      "Available": 15
    },
    {
      "SKU": "AIR_BULBOSA_5PK",
      "Available": 13
    },
    {
      "SKU": "AIR_BULBOSA_FERT",
      "Available": 33
    },
    {
      "SKU": "AIR_BUTZII",
      "Available": 94
    },
    {
      "SKU": "AIR_BUTZII_5PK",
      "Available": 18
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA",
      "Available": 20
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_FERT",
      "Available": 20
    },
    {
      "SKU": "AIR_EHLERSIANA",
      "Available": 15
    },
    {
      "SKU": "AIR_FLORIBUNDA",
      "Available": 16
    },
    {
      "SKU": "AIR_FUCHSII",
      "Available": 397
    },
    {
      "SKU": "AIR_FUCHSII_10PK",
      "Available": 39
    },
    {
      "SKU": "AIR_FUCHSII_25PK",
      "Available": 15
    },
    {
      "SKU": "AIR_FUCHSII_5PK",
      "Available": 79
    },
    {
      "SKU": "AIR_FUCHSII_5PK",
      "Available": 68
    },
    {
      "SKU": "AIR_FUCHSII_5PK",
      "Available": 24
    },
    {
      "SKU": "AIR_FUCHSII_5PK",
      "Available": 13
    },
    {
      "SKU": "AIR_FUCHSII_FERT",
      "Available": 122
    },
    {
      "SKU": "AIR_HARRISII",
      "Available": 57
    },
    {
      "SKU": "AIR_HARRISII_5PK",
      "Available": 10
    },
    {
      "SKU": "AIR_HARRISII_FERT",
      "Available": 28
    },
    {
      "SKU": "AIR_HOUSTON.RED.PRINCESS",
      "Available": 13
    },
    {
      "SKU": "AIR_IONANTHA",
      "Available": 428
    },
    {
      "SKU": "AIR_IONANTHA_100PK",
      "Available": 40
    },
    {
      "SKU": "AIR_IONANTHA_100PK",
      "Available": 36
    },
    {
      "SKU": "AIR_IONANTHA_10PK",
      "Available": 75
    },
    {
      "SKU": "AIR_IONANTHA_10PK",
      "Available": 42
    },
    {
      "SKU": "AIR_IONANTHA_10PK",
      "Available": 33
    },
    {
      "SKU": "AIR_IONANTHA_25PK",
      "Available": 95
    },
    {
      "SKU": "AIR_IONANTHA_25PK",
      "Available": 78
    },
    {
      "SKU": "AIR_IONANTHA_25PK",
      "Available": 17
    },
    {
      "SKU": "AIR_IONANTHA_3PK",
      "Available": 142
    },
    {
      "SKU": "AIR_IONANTHA_50PK",
      "Available": 37
    },
    {
      "SKU": "AIR_IONANTHA_50PK",
      "Available": 29
    },
    {
      "SKU": "AIR_IONANTHA_5PK",
      "Available": 111
    },
    {
      "SKU": "AIR_IONANTHA_5PK",
      "Available": 85
    },
    {
      "SKU": "AIR_IONANTHA_5PK",
      "Available": 26
    },
    {
      "SKU": "AIR_IONANTHA_POT_3PK",
      "Available": 142
    },
    {
      "SKU": "AIR_IONANTHA.MEXICO",
      "Available": 25
    },
    {
      "SKU": "AIR_JUNCEA",
      "Available": 17
    },
    {
      "SKU": "AIR_KOLBY",
      "Available": 228
    },
    {
      "SKU": "AIR_KOLBY_10PK",
      "Available": 22
    },
    {
      "SKU": "AIR_KOLBY_10PK",
      "Available": 15
    },
    {
      "SKU": "AIR_KOLBY_10PK",
      "Available": 13
    },
    {
      "SKU": "AIR_KOLBY_25PK",
      "Available": 37
    },
    {
      "SKU": "AIR_KOLBY_25PK",
      "Available": 35
    },
    {
      "SKU": "AIR_KOLBY_3PK",
      "Available": 75
    },
    {
      "SKU": "AIR_KOLBY_5PK",
      "Available": 45
    },
    {
      "SKU": "AIR_KOLBY_5PK",
      "Available": 31
    },
    {
      "SKU": "AIR_KOLBY_5PK",
      "Available": 25
    },
    {
      "SKU": "AIR_KOLBY_5PK",
      "Available": 11
    },
    {
      "SKU": "AIR_MONTANA",
      "Available": 32
    },
    {
      "SKU": "AIR_MOONLIGHT_FERT",
      "Available": 20
    },
    {
      "SKU": "AIR_MYSTERY_AIR.PLANT",
      "Available": 118
    },
    {
      "SKU": "AIR_PALEACEAX.TECTORUM",
      "Available": 26
    },
    {
      "SKU": "AIR_PSEUDOBAILEYI",
      "Available": 67
    },
    {
      "SKU": "AIR_PSEUDOBAILEYI_5PK",
      "Available": 13
    },
    {
      "SKU": "AIR_SCHIEDEANA_FERT",
      "Available": 30
    },
    {
      "SKU": "AIR_SEASHELL_3PK",
      "Available": 18
    },
    {
      "SKU": "AIR_SEASHELL_4PK",
      "Available": 18
    },
    {
      "SKU": "AIR_SPANISH.MOSS",
      "Available": 54
    },
    {
      "SKU": "AIR_SPANISH.MOSS_2PK",
      "Available": 27
    },
    {
      "SKU": "AIR_SPANISH.MOSS_3PK",
      "Available": 17
    },
    {
      "SKU": "AIR_SPANISH.MOSS_5PK",
      "Available": 10
    },
    {
      "SKU": "AIR_STELLIFERA",
      "Available": 40
    },
    {
      "SKU": "AIR_STRICTA",
      "Available": 66
    },
    {
      "SKU": "AIR_STRICTA_5PK",
      "Available": 12
    },
    {
      "SKU": "AIR_TENUIFOLIA",
      "Available": 55
    },
    {
      "SKU": "AIR_TENUIFOLIA_5PK",
      "Available": 11
    },
    {
      "SKU": "AIR_TRICOLOR",
      "Available": 44
    },
    {
      "SKU": "AIR_VARIETY_3PK",
      "Available": 71
    },
    {
      "SKU": "AIR_VARIETY_3PK_TALL",
      "Available": 17
    },
    {
      "SKU": "AIR_VARIETY_SPRAY_2PK",
      "Available": 275
    },
    {
      "SKU": "AIR_VARIETY_SPRAY_3PK",
      "Available": 71
    },
    {
      "SKU": "AIR_VELUTINA",
      "Available": 90
    },
    {
      "SKU": "AIR_VELUTINA_5PK",
      "Available": 18
    },
    {
      "SKU": "AIR_VELUTINA_FERT",
      "Available": 40
    },
    {
      "SKU": "AIR_XEROGRAPHICA",
      "Available": 25
    },
    {
      "SKU": "AIR_XEROGRAPHICA_2PK",
      "Available": 12
    },
    {
      "SKU": "AQUA_JAVA.MOSS_LOOSE",
      "Available": 98
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_DARK.GREEN_CROTONS",
      "Available": 80
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_DARK.GREEN_DRACAENAS",
      "Available": 80
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_DARK.GREEN_FERNS",
      "Available": 80
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_DARK.GREEN_MONSTERAS",
      "Available": 80
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_GLOSS.BLACK_CROTONS",
      "Available": 79
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_GLOSS.BLACK_DRACAENAS",
      "Available": 79
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_GLOSS.BLACK_FERNS",
      "Available": 72
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_GLOSS.BLACK_MONSTERAS",
      "Available": 79
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_LIGHT.BLUE_CROTONS",
      "Available": 64
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_LIGHT.BLUE_DRACAENAS",
      "Available": 64
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_LIGHT.BLUE_FERNS",
      "Available": 64
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_LIGHT.BLUE_MONSTERAS",
      "Available": 64
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.BLACK_CROTONS",
      "Available": 89
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.BLACK_DRACAENAS",
      "Available": 89
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.BLACK_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.BLACK_MONSTERAS",
      "Available": 89
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.MINT_CROTONS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.MINT_DRACAENAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.MINT_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.MINT_MONSTERAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.PINK_CROTONS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.PINK_DRACAENAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.PINK_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.PINK_MONSTERAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.RED_CROTONS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.RED_DRACAENAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.RED_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_MATTE.RED_MONSTERAS",
      "Available": 90
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_NAVY.MARBLE_CROTONS",
      "Available": 51
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_NAVY.MARBLE_DRACAENAS",
      "Available": 51
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_NAVY.MARBLE_FERNS",
      "Available": 51
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_NAVY.MARBLE_MONSTERAS",
      "Available": 51
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_RED_CROTONS",
      "Available": 68
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_RED_DRACAENAS",
      "Available": 68
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_RED_FERNS",
      "Available": 68
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_RED_MONSTERAS",
      "Available": 68
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_WHITE_CROTONS",
      "Available": 95
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_WHITE_DRACAENAS",
      "Available": 112
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_WHITE_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_CYLINDER_WHITE_MONSTERAS",
      "Available": 85
    },
    {
      "SKU": "ARRANGEMENT_PEPE_PINK_CROTONS",
      "Available": 14
    },
    {
      "SKU": "ARRANGEMENT_PEPE_PINK_DRACAENAS",
      "Available": 29
    },
    {
      "SKU": "ARRANGEMENT_PEPE_PINK_FERNS",
      "Available": 16
    },
    {
      "SKU": "ARRANGEMENT_TERRA.COTTA_CROTONS",
      "Available": 94
    },
    {
      "SKU": "ARRANGEMENT_TERRA.COTTA_DRACAENAS",
      "Available": 94
    },
    {
      "SKU": "ARRANGEMENT_TERRA.COTTA_FERNS",
      "Available": 70
    },
    {
      "SKU": "ARRANGEMENT_TERRA.COTTA_MONSTERAS",
      "Available": 94
    },
    {
      "SKU": "BONSAI_BLACK.PINE",
      "Available": 24
    },
    {
      "SKU": "BONSAI_MAPLE",
      "Available": 11
    },
    {
      "SKU": "BOOK_CRAZY.PLANT.LADY",
      "Available": 10
    },
    {
      "SKU": "BOOK_LEAF.SUPPLY",
      "Available": 11
    },
    {
      "SKU": "BOOK_MAKE.PLANT.LOVE.YOU",
      "Available": 15
    },
    {
      "SKU": "BOOK_PLANTS.DREAM",
      "Available": 10
    },
    {
      "SKU": "BOOK_SUCCULENTS.SIMPLIFIED",
      "Available": 10
    },
    {
      "SKU": "BOOK_TERRAIN",
      "Available": 10
    },
    {
      "SKU": "BOOK_TRAIN.YOUR.CACTUS",
      "Available": 10
    },
    {
      "SKU": "BUNDLE_AIR.PURIFYING_4IN",
      "Available": 28
    },
    {
      "SKU": "BUNDLE_BEST.SELLERS_4IN",
      "Available": 105
    },
    {
      "SKU": "BUNDLE_BEST.SELLERS_6IN",
      "Available": 20
    },
    {
      "SKU": "BUNDLE_EASY.CARE_4IN",
      "Available": 61
    },
    {
      "SKU": "BUNDLE_EASY.CARE_6IN",
      "Available": 99
    },
    {
      "SKU": "BUNDLE_GIFT.POT_GLOSS.BLACK.CYLINDER",
      "Available": 18
    },
    {
      "SKU": "BUNDLE_GIFT.POT_HUEY",
      "Available": 18
    },
    {
      "SKU": "BUNDLE_GIFT.POT_WHITE.CYLINDER",
      "Available": 18
    },
    {
      "SKU": "BUNDLE_LOW.LIGHT_4IN",
      "Available": 43
    },
    {
      "SKU": "BUNDLE_MOM.DAY_AIR.PLANT",
      "Available": 21
    },
    {
      "SKU": "BUNDLE_NEW.PLANT.PARENT",
      "Available": 41
    },
    {
      "SKU": "BUNDLE_SPRING_4IN",
      "Available": 15
    },
    {
      "SKU": "CUT_POTHOS_GOLDEN_5PK",
      "Available": 101
    },
    {
      "SKU": "FERT_AIR.PLANT_30ML",
      "Available": 37273
    },
    {
      "SKU": "FERT_HOUSEPLANT_500ML",
      "Available": 122
    },
    {
      "SKU": "FERT_LEAF.ARMOR",
      "Available": 17
    },
    {
      "SKU": "FERT_NOOT.FOOD",
      "Available": 48
    },
    {
      "SKU": "FERT_PELLET_HPS",
      "Available": 64
    },
    {
      "SKU": "Final_Product_NetSuite_Testing_1",
      "Available": 38
    },
    {
      "SKU": "Integration_Test_Product",
      "Available": 1155
    },
    {
      "SKU": "Inventory_Quantity_Test_Item",
      "Available": 38
    },
    {
      "SKU": "MZ_MASK_BLACK",
      "Available": 40
    },
    {
      "SKU": "MZ_MASK_BLUE",
      "Available": 40
    },
    {
      "SKU": "MZ_MASK_GREY",
      "Available": 40
    },
    {
      "SKU": "MZ_MASK_PINK",
      "Available": 40
    },
    {
      "SKU": "NetSuite_Integration_Test_Item",
      "Available": 610
    },
    {
      "SKU": "NetSuite_Integration_Test_Item 5",
      "Available": 39
    },
    {
      "SKU": "NetSuite_Integration_Test_Item2",
      "Available": 116
    },
    {
      "SKU": "NetSuite_Kit_Package_Item_Test_2",
      "Available": 34
    },
    {
      "SKU": "Netsuite_Product_Integration_Test",
      "Available": 56
    },
    {
      "SKU": "NetSuite_Test_Item",
      "Available": 39
    },
    {
      "SKU": "NetSuite_Test_Item_New",
      "Available": 77
    },
    {
      "SKU": "Order_Split_Testing_Item",
      "Available": 18
    },
    {
      "SKU": "Order_Split_Testing_Item_10",
      "Available": 10
    },
    {
      "SKU": "Order_Split_Testing_Item_2",
      "Available": 18
    },
    {
      "SKU": "Order_Split_Testing_Item_3",
      "Available": 24
    },
    {
      "SKU": "PLANTASIA_SHIRT_LS.L",
      "Available": 10
    },
    {
      "SKU": "PLANTASIA_SHIRT_LS.M",
      "Available": 10
    },
    {
      "SKU": "PLANTASIA_SHIRT_LS.S",
      "Available": 10
    },
    {
      "SKU": "PLANTASIA_VINYL",
      "Available": 18
    },
    {
      "SKU": "PLUMERIA_JEANIE.MORAGNE_DOUBLE",
      "Available": 10
    },
    {
      "SKU": "PLUMERIA_SIAM.RUBY_TRIPLE",
      "Available": 10
    },
    {
      "SKU": "PLUMERIA_SLAUGHTER.PINK_DOUBLE",
      "Available": 13
    },
    {
      "SKU": "PLUMERIA_SLAUGHTER.PINK_TRIPLE",
      "Available": 10
    },
    {
      "SKU": "PLUMERIA_TILLIES.HUGHES_SINGLE",
      "Available": 11
    },
    {
      "SKU": "PLUMERIA_TILLIES.HUGHES_TRIPLE",
      "Available": 10
    },
    {
      "SKU": "POT_ANIMAL_CHICKEN",
      "Available": 10
    },
    {
      "SKU": "POT_ANIMAL_FISH",
      "Available": 55
    },
    {
      "SKU": "POT_ANIMAL_GIRAFFE",
      "Available": 10
    },
    {
      "SKU": "POT_ANIMAL_HIPPO",
      "Available": 19
    },
    {
      "SKU": "POT_ANIMAL_PANDA",
      "Available": 10
    },
    {
      "SKU": "POT_ANIMAL_POLAR.BEAR",
      "Available": 10
    },
    {
      "SKU": "POT_ANIMAL_TURTLE",
      "Available": 26
    },
    {
      "SKU": "POT_ANIMAL_ZEBRA",
      "Available": 26
    },
    {
      "SKU": "POT_AVON_WHITE_6.5IN",
      "Available": 35
    },
    {
      "SKU": "POT_BASKET_EBBA_8IN",
      "Available": 22
    },
    {
      "SKU": "POT_BASKET_WOVEN",
      "Available": 19
    },
    {
      "SKU": "POT_BOHEMIAN_4PK",
      "Available": 17
    },
    {
      "SKU": "POT_CABA_PLANTER_5IN",
      "Available": 20
    },
    {
      "SKU": "POT_CHROMO_3IN",
      "Available": 45
    },
    {
      "SKU": "POT_CROIX_PLANTER_BLACK_SMALL_4.5IN",
      "Available": 24
    },
    {
      "SKU": "POT_CYLINDER_BLACK_6IN",
      "Available": 15
    },
    {
      "SKU": "POT_CYLINDER_DARK.GREEN_6IN",
      "Available": 80
    },
    {
      "SKU": "POT_CYLINDER_GLOSSBLACK_6IN",
      "Available": 79
    },
    {
      "SKU": "POT_CYLINDER_LIGHT.BLUE_6IN",
      "Available": 64
    },
    {
      "SKU": "POT_CYLINDER_MATTE.BLACK_5.5IN",
      "Available": 89
    },
    {
      "SKU": "POT_CYLINDER_MATTE.MINT_5.5IN",
      "Available": 90
    },
    {
      "SKU": "POT_CYLINDER_MATTE.PINK_5.5IN",
      "Available": 90
    },
    {
      "SKU": "POT_CYLINDER_MATTE.RED_5.5IN",
      "Available": 90
    },
    {
      "SKU": "POT_CYLINDER_MATTE.WHITE_5.5IN",
      "Available": 89
    },
    {
      "SKU": "POT_CYLINDER_MATTEBLACK_6IN",
      "Available": 78
    },
    {
      "SKU": "POT_CYLINDER_NAVY.MARBLE_6IN",
      "Available": 51
    },
    {
      "SKU": "POT_CYLINDER_RED_6IN",
      "Available": 68
    },
    {
      "SKU": "POT_CYLINDER_WHITE_6IN",
      "Available": 167
    },
    {
      "SKU": "POT_DESERT_4IN",
      "Available": 47
    },
    {
      "SKU": "POT_DESERT_COMPOTE_5IN",
      "Available": 25
    },
    {
      "SKU": "POT_EXPRESSIONS_POT_6IN",
      "Available": 39
    },
    {
      "SKU": "POT_FLEUR.DE.LIS_WHITE_5IN",
      "Available": 12
    },
    {
      "SKU": "POT_GIA.GIRAFFE_8.5IN",
      "Available": 11
    },
    {
      "SKU": "POT_GOLD.STARS_5IN",
      "Available": 10
    },
    {
      "SKU": "POT_GREY.LEAVES_5IN",
      "Available": 12
    },
    {
      "SKU": "POT_GROW.BAG_1G",
      "Available": 18
    },
    {
      "SKU": "POT_HANGER_WOOD.FLAT_12IN",
      "Available": 17
    },
    {
      "SKU": "POT_HUEY_5IN",
      "Available": 88
    },
    {
      "SKU": "POT_HYDROPONIC.VINTAGE",
      "Available": 188
    },
    {
      "SKU": "POT_KIWI_5IN",
      "Available": 12
    },
    {
      "SKU": "POT_LIBERTY_BLACK_8IN",
      "Available": 10
    },
    {
      "SKU": "POT_NAVARRO_7IN",
      "Available": 15
    },
    {
      "SKU": "POT_OWL_2IN",
      "Available": 42
    },
    {
      "SKU": "POT_PEPE_GREEN_7IN",
      "Available": 63
    },
    {
      "SKU": "POT_PEPE_PINK_7IN",
      "Available": 29
    },
    {
      "SKU": "POT_RAHNZA_HANGING_11IN",
      "Available": 20
    },
    {
      "SKU": "POT_RIDGED_TERRA_4IN",
      "Available": 15
    },
    {
      "SKU": "POT_SONORA_6IN",
      "Available": 20
    },
    {
      "SKU": "POT_STD_TERRA.COTA_6IN",
      "Available": 94
    },
    {
      "SKU": "POT_STD_TERRA.COTA_6IN",
      "Available": 94
    },
    {
      "SKU": "POT_TOMI_HANGING_4.5IN",
      "Available": 34
    },
    {
      "SKU": "POT_WHITE.FLOWERS_5IN",
      "Available": 12
    },
    {
      "SKU": "SEED_BEETS.DETROIT",
      "Available": 19
    },
    {
      "SKU": "SEED_BROCCOLI.WALTHAM",
      "Available": 19
    },
    {
      "SKU": "SEED_CAULIFLOWER.IGLOO",
      "Available": 19
    },
    {
      "SKU": "SEED_CUCUMBER.MUNCHER",
      "Available": 19
    },
    {
      "SKU": "SEED_EGGPLANT.LONG PURPLE",
      "Available": 20
    },
    {
      "SKU": "SEED_GREEN.BEANS.BLUE.LAKE",
      "Available": 19
    },
    {
      "SKU": "SEED_GREEN.PEPPERS.CA.WONDER",
      "Available": 18
    },
    {
      "SKU": "SEED_LETTUCE.MIX.GREENS",
      "Available": 19
    },
    {
      "SKU": "SEED_MUSTARD.SOUTHERN",
      "Available": 19
    },
    {
      "SKU": "SEED_MYSTERY",
      "Available": 997
    },
    {
      "SKU": "SEED_OKRA",
      "Available": 19
    },
    {
      "SKU": "SEED_ONION.TOKYO.LONG.WHITE",
      "Available": 19
    },
    {
      "SKU": "SEED_RUTABAGA.AMERICAN",
      "Available": 19
    },
    {
      "SKU": "SEED_TOMATO.SAN.MARZANO",
      "Available": 18
    },
    {
      "SKU": "SOIL_NOOT.RESCUE",
      "Available": 43
    },
    {
      "SKU": "TEST SEED COUNT",
      "Available": 162
    },
    {
      "SKU": "10_FICUS_BURGUNDY",
      "Available": 1
    },
    {
      "SKU": "10_FICUS_LYRATA",
      "Available": 4
    },
    {
      "SKU": "10_SNAKE_ZEYLANICA",
      "Available": 1
    },
    {
      "SKU": "10_STRELITZIA_BIRD.OF.PARADISE",
      "Available": 1
    },
    {
      "SKU": "10_ZAMIOCULCAS_ZAMIIFOLIA",
      "Available": 6
    },
    {
      "SKU": "2_IVY_GREEN",
      "Available": 2
    },
    {
      "SKU": "2_PALM_PONYTAIL",
      "Available": 8
    },
    {
      "SKU": "4_ALOCASIA_TINY.DANCER",
      "Available": 3
    },
    {
      "SKU": "4_ANTHURIUM_CRYSTALINUM",
      "Available": 1
    },
    {
      "SKU": "4_ANTHURIUM_RED_PP.HUEY",
      "Available": 1
    },
    {
      "SKU": "4_ANTHURIUM_RED_PP.WHT.CYL",
      "Available": 1
    },
    {
      "SKU": "4_ANTHURIUM_VARIETY_2PK",
      "Available": 8
    },
    {
      "SKU": "4_ANTHURIUM_VARIETY_3PK",
      "Available": 7
    },
    {
      "SKU": "4_BROMELIAD_ENERGY",
      "Available": 2
    },
    {
      "SKU": "4_CALATHEA_PEACOCK",
      "Available": 3
    },
    {
      "SKU": "4_CALATHEA_WHITE.STAR",
      "Available": 9
    },
    {
      "SKU": "4_DIEFFENBACHIA_CAMILLE_PP.NAVARRO",
      "Available": 9
    },
    {
      "SKU": "4_DRACAENA_ELEGANCE",
      "Available": 8
    },
    {
      "SKU": "4_FERN_ALBO",
      "Available": 1
    },
    {
      "SKU": "4_HOYA_ROPE",
      "Available": 7
    },
    {
      "SKU": "4_IVY_EVA",
      "Available": 5
    },
    {
      "SKU": "4_NEMATANTHUS_CANDY.CORN",
      "Available": 5
    },
    {
      "SKU": "4_NETTLE_SILVER.SPARKLE",
      "Available": 4
    },
    {
      "SKU": "4_PEPEROMIA_CAPERATA.RIPPLE",
      "Available": 2
    },
    {
      "SKU": "4_PEPEROMIA_NAPOLI.NIGHTS",
      "Available": 7
    },
    {
      "SKU": "4_PEPEROMIA_ROSSO",
      "Available": 2
    },
    {
      "SKU": "4_PEPEROMIA_VARIETY_2PK",
      "Available": 2
    },
    {
      "SKU": "4_PEPEROMIA_VARIETY_3PK",
      "Available": 2
    },
    {
      "SKU": "4_PRE.WHITE_ANTHURIUM_PINK",
      "Available": 5
    },
    {
      "SKU": "4_PRE.WHITE_PHILO_CORDATUM",
      "Available": 5
    },
    {
      "SKU": "4_SCINDAPSUS.TREUBII_MOONLIGHT",
      "Available": 1
    },
    {
      "SKU": "4_SNAKE_MOONSHINE",
      "Available": 7
    },
    {
      "SKU": "4_SUCC_ADENIUM_DESERT.ROSE",
      "Available": 5
    },
    {
      "SKU": "4_SUCC_AEONIUM_GREEN.SUNSET",
      "Available": 5
    },
    {
      "SKU": "4_SUCC_SENECIO_STRING.OF.PEARLS",
      "Available": 1
    },
    {
      "SKU": "4_SUCC_STRING.OF.DOLPHINS_PP.HUEY",
      "Available": 5
    },
    {
      "SKU": "4_SUCC.ECHEVERIA_VARIETY_4PK",
      "Available": 2
    },
    {
      "SKU": "4_ZAMIOCULCAS_ZAMIIFOLIA_PP.TERRA.LIBERTY",
      "Available": 1
    },
    {
      "SKU": "6_ARALIA_FABIAN.STUMP",
      "Available": 6
    },
    {
      "SKU": "6_BEGONIA_MACULATA",
      "Available": 9
    },
    {
      "SKU": "6_BROMELIAD_SILVER.VASE",
      "Available": 8
    },
    {
      "SKU": "6_CALATHEA_DOTTIE",
      "Available": 3
    },
    {
      "SKU": "6_CALATHEA_FREDDIE",
      "Available": 5
    },
    {
      "SKU": "6_CALATHEA_FURRY.FEATHER",
      "Available": 9
    },
    {
      "SKU": "6_CALATHEA_MAKOYANA",
      "Available": 4
    },
    {
      "SKU": "6_CALATHEA_ORNATA",
      "Available": 6
    },
    {
      "SKU": "6_CALATHEA_WARSCEWICZII",
      "Available": 2
    },
    {
      "SKU": "6_CH.EVERGREEN_FIRST.DIAMOND",
      "Available": 4
    },
    {
      "SKU": "6_CH.EVERGREEN_MARIA",
      "Available": 8
    },
    {
      "SKU": "6_CROTON_OAK.LEAF",
      "Available": 2
    },
    {
      "SKU": "6_FERN_JESTER.CROWN",
      "Available": 7
    },
    {
      "SKU": "6_FICUS_BENJAMINA",
      "Available": 2
    },
    {
      "SKU": "6_HOYA_ROPE",
      "Available": 5
    },
    {
      "SKU": "6_IVY_GREEN",
      "Available": 4
    },
    {
      "SKU": "6_IVY_VARIETY_2PK",
      "Available": 4
    },
    {
      "SKU": "6_MARANTA_LEMON.LIME",
      "Available": 7
    },
    {
      "SKU": "6_MARANTA_LEUCONEURA",
      "Available": 1
    },
    {
      "SKU": "6_ORCHID.CACTUS_CURLY.SUE",
      "Available": 1
    },
    {
      "SKU": "6_PALM_PARLOR",
      "Available": 5
    },
    {
      "SKU": "6_PEPEROMIA_FROST",
      "Available": 1
    },
    {
      "SKU": "6_PHILODENDRON_CONGO.GREEN",
      "Available": 2
    },
    {
      "SKU": "6_PHILODENDRON_NEON",
      "Available": 1
    },
    {
      "SKU": "6_SNAKE_GOLD.FLAME",
      "Available": 5
    },
    {
      "SKU": "6_SPIDER_HAWAIIAN",
      "Available": 8
    },
    {
      "SKU": "6_STROMANTHE_SANGUINEA",
      "Available": 3
    },
    {
      "SKU": "6_SUCC_CACTUS_LIFESAVER",
      "Available": 1
    },
    {
      "SKU": "6_SUCC_CACTUS_RAT.TAIL",
      "Available": 8
    },
    {
      "SKU": "6_SYNGONIUM_WHITE.BUTTERFLY",
      "Available": 9
    },
    {
      "SKU": "8_MONSTERA_DELICIOSA",
      "Available": 5
    },
    {
      "SKU": "8_MONSTERA_MINIMA",
      "Available": 8
    },
    {
      "SKU": "8_PACHIRA_BRAID",
      "Available": 9
    },
    {
      "SKU": "8_POTHOS_GOLDEN",
      "Available": 4
    },
    {
      "SKU": "8_SNAKE_ZEYLANICA",
      "Available": 9
    },
    {
      "SKU": "ACC_ACRYLIC.MARKERS",
      "Available": 5
    },
    {
      "SKU": "ACC_AIR_HANGER_BRASS",
      "Available": 4
    },
    {
      "SKU": "ACC_CARE.CARD.BINDER",
      "Available": 4
    },
    {
      "SKU": "ACC_CRAWL.INSECT.KILLER",
      "Available": 8
    },
    {
      "SKU": "ACC_GARDEN.TARP_6FT",
      "Available": 7
    },
    {
      "SKU": "ACC_GLOVE_GARDEN_XL",
      "Available": 5
    },
    {
      "SKU": "ACC_MODSPROUT_MASON.JAR_ROSEMARY",
      "Available": 5
    },
    {
      "SKU": "ACC_MOSS_WHITE",
      "Available": 7
    },
    {
      "SKU": "ACC_PLANT.STICK_SNAKE_18IN",
      "Available": 3
    },
    {
      "SKU": "ACC_PROPAGATION_WIRE.S",
      "Available": 4
    },
    {
      "SKU": "ACC_SHEAR_BLACK",
      "Available": 4
    },
    {
      "SKU": "ACC_TOTE_PASTEL.LEAVES",
      "Available": 1
    },
    {
      "SKU": "ACC_TROWEL_WOOD",
      "Available": 8
    },
    {
      "SKU": "ACC_WATERING.CAN_WHITE_WOOD",
      "Available": 1
    },
    {
      "SKU": "AIR_ARAUJEI_10PK",
      "Available": 1
    },
    {
      "SKU": "AIR_ARAUJEI_5PK",
      "Available": 3
    },
    {
      "SKU": "AIR_BANDENSIS_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_BANDENSIS_5PK",
      "Available": 5
    },
    {
      "SKU": "AIR_BERGERI_10PK",
      "Available": 6
    },
    {
      "SKU": "AIR_BERGERI_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_BRACHYCAULOS_10PK",
      "Available": 5
    },
    {
      "SKU": "AIR_BRACHYCAULOS_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_BULBOSA_10PK",
      "Available": 8
    },
    {
      "SKU": "AIR_BULBOSA_10PK",
      "Available": 7
    },
    {
      "SKU": "AIR_BULBOSA_10PK",
      "Available": 4
    },
    {
      "SKU": "AIR_BULBOSA_10PK",
      "Available": 3
    },
    {
      "SKU": "AIR_BULBOSA_25PK",
      "Available": 2
    },
    {
      "SKU": "AIR_BULBOSA_5PK",
      "Available": 6
    },
    {
      "SKU": "AIR_BULBOSA_5PK",
      "Available": 4
    },
    {
      "SKU": "AIR_BUTZII_10PK",
      "Available": 8
    },
    {
      "SKU": "AIR_BUTZII_10PK",
      "Available": 6
    },
    {
      "SKU": "AIR_BUTZII_10PK",
      "Available": 4
    },
    {
      "SKU": "AIR_BUTZII_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_BUTZII_25PK",
      "Available": 2
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_10PK",
      "Available": 3
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_10PK",
      "Available": 3
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_CAPUT.MEDUSA_5PK",
      "Available": 4
    },
    {
      "SKU": "AIR_EHLERSIANA_10PK",
      "Available": 1
    },
    {
      "SKU": "AIR_EHLERSIANA_5PK",
      "Available": 3
    },
    {
      "SKU": "AIR_FUCHSII_100PK",
      "Available": 3
    },
    {
      "SKU": "AIR_FUCHSII_50PK",
      "Available": 7
    },
    {
      "SKU": "AIR_HARRISII_10PK",
      "Available": 4
    },
    {
      "SKU": "AIR_HARRISII_25PK",
      "Available": 2
    },
    {
      "SKU": "AIR_HOUSTON.RED.PRINCESS_10PK",
      "Available": 1
    },
    {
      "SKU": "AIR_HOUSTON.RED.PRINCESS_5PK",
      "Available": 2
    },
    {
      "SKU": "AIR_IONANTHA_100PK",
      "Available": 4
    },
    {
      "SKU": "AIR_IONANTHA_50PK",
      "Available": 8
    },
    {
      "SKU": "AIR_IONANTHA.MEXICO_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_IONANTHA.MEXICO_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_IONANTHA.MEXICO_5PK",
      "Available": 5
    },
    {
      "SKU": "AIR_JUNCEA_10PK",
      "Available": 1
    },
    {
      "SKU": "AIR_JUNCEA_5PK",
      "Available": 7
    },
    {
      "SKU": "AIR_JUNCEA_5PK",
      "Available": 7
    },
    {
      "SKU": "AIR_JUNCEA_5PK",
      "Available": 3
    },
    {
      "SKU": "AIR_JUNCEA_5PK",
      "Available": 3
    },
    {
      "SKU": "AIR_KOLBY_100PK",
      "Available": 1
    },
    {
      "SKU": "AIR_KOLBY_10PK",
      "Available": 6
    },
    {
      "SKU": "AIR_KOLBY_25PK",
      "Available": 8
    },
    {
      "SKU": "AIR_KOLBY_25PK",
      "Available": 6
    },
    {
      "SKU": "AIR_KOLBY_50PK",
      "Available": 4
    },
    {
      "SKU": "AIR_MONTANA_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_MONTANA_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_MONTANA_5PK",
      "Available": 5
    },
    {
      "SKU": "AIR_PALEACEAX.TECTORUM_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_PALEACEAX.TECTORUM_5PK",
      "Available": 5
    },
    {
      "SKU": "AIR_PSEUDOBAILEYI_10PK",
      "Available": 6
    },
    {
      "SKU": "AIR_PSEUDOBAILEYI_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_SPANISH.MOSS_10PK",
      "Available": 5
    },
    {
      "SKU": "AIR_SPANISH.MOSS_25PK",
      "Available": 2
    },
    {
      "SKU": "AIR_STELLIFERA_10PK",
      "Available": 4
    },
    {
      "SKU": "AIR_STELLIFERA_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_STELLIFERA_5PK",
      "Available": 8
    },
    {
      "SKU": "AIR_STRICTA_10PK",
      "Available": 5
    },
    {
      "SKU": "AIR_STRICTA_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_TENUIFOLIA_10PK",
      "Available": 5
    },
    {
      "SKU": "AIR_TENUIFOLIA_25PK",
      "Available": 2
    },
    {
      "SKU": "AIR_TRICOLOR_10PK",
      "Available": 4
    },
    {
      "SKU": "AIR_TRICOLOR_25PK",
      "Available": 1
    },
    {
      "SKU": "AIR_TRICOLOR_5PK",
      "Available": 8
    },
    {
      "SKU": "AIR_VELUTINA_10PK",
      "Available": 3
    },
    {
      "SKU": "AIR_VELUTINA_10PK",
      "Available": 3
    },
    {
      "SKU": "AIR_VELUTINA_25PK",
      "Available": 3
    },
    {
      "SKU": "AIR_VICTORIANA",
      "Available": 5
    },
    {
      "SKU": "AIR_VICTORIANA_5PK",
      "Available": 1
    },
    {
      "SKU": "AIR_XEROGRAPHICA_10PK",
      "Available": 2
    },
    {
      "SKU": "AIR_XEROGRAPHICA_3PK",
      "Available": 8
    },
    {
      "SKU": "AIR_XEROGRAPHICA_3PK",
      "Available": 7
    },
    {
      "SKU": "AIR_XEROGRAPHICA_3PK",
      "Available": 1
    },
    {
      "SKU": "AIR_XEROGRAPHICA_5PK",
      "Available": 4
    },
    {
      "SKU": "AIR_XEROGRAPHICA_FERT",
      "Available": 4
    },
    {
      "SKU": "BOOK_AIR.PLANTS",
      "Available": 7
    },
    {
      "SKU": "BOOK_DECORATE.PLANTS",
      "Available": 7
    },
    {
      "SKU": "BOOK_GROW.HOUSEPLANTS",
      "Available": 8
    },
    {
      "SKU": "BOOK_HOME.SWEET.HOUSEPLANT",
      "Available": 8
    },
    {
      "SKU": "BOOK_INDESTRUCTIBLE.HP",
      "Available": 1
    },
    {
      "SKU": "BOOK_INSPIRED.HP",
      "Available": 8
    },
    {
      "SKU": "BOOK_PLANT.CHANGED.MY.LIFE",
      "Available": 9
    },
    {
      "SKU": "BOOK_PLANT.PARENTING",
      "Available": 6
    },
    {
      "SKU": "BOOK_PROPAGATING.PLANTS",
      "Available": 9
    },
    {
      "SKU": "BOOK_WHATS.WRONG",
      "Available": 8
    },
    {
      "SKU": "BUNDLE_AIR.PURIFYING_6IN",
      "Available": 6
    },
    {
      "SKU": "BUNDLE_VALENTINES.DAY",
      "Available": 1
    },
    {
      "SKU": "CUT_PHILODENDRON_BRASIL_5PK",
      "Available": 3
    },
    {
      "SKU": "CUT_POTHOS_NEON_5PK",
      "Available": 1
    },
    {
      "SKU": "FERT_FIDDLE.LEAF",
      "Available": 4
    },
    {
      "SKU": "FERT_INSECT.SPRAY",
      "Available": 8
    },
    {
      "SKU": "FERT_MONSTERA.FOOD",
      "Available": 3
    },
    {
      "SKU": "Integration_Testing_Product_SZ",
      "Available": 2
    },
    {
      "SKU": "NetSuite_Kit_Package_Item_Test",
      "Available": 6
    },
    {
      "SKU": "PLANTASIA_SHIRT_MAN.PLANT.L",
      "Available": 8
    },
    {
      "SKU": "PLANTASIA_SHIRT_MAN.PLANT.M",
      "Available": 5
    },
    {
      "SKU": "PLANTASIA_SHIRT_MAN.PLANT.S",
      "Available": 9
    },
    {
      "SKU": "PLANTASIA_TOTE",
      "Available": 9
    },
    {
      "SKU": "PLUMERIA_DWARF.WATERMELON_DOUBLE",
      "Available": 9
    },
    {
      "SKU": "PLUMERIA_DWARF.WATERMELON_TRIPLE",
      "Available": 3
    },
    {
      "SKU": "PLUMERIA_JEANIE.MORAGNE_SINGLE",
      "Available": 2
    },
    {
      "SKU": "PLUMERIA_JEANIE.MORAGNE_TRIPLE",
      "Available": 7
    },
    {
      "SKU": "PLUMERIA_MARDI.GRAS_TRIPLE",
      "Available": 6
    },
    {
      "SKU": "PLUMERIA_SAN.MIGUEL_DOUBLE",
      "Available": 3
    },
    {
      "SKU": "PLUMERIA_SAN.MIGUEL_SINGLE",
      "Available": 7
    },
    {
      "SKU": "PLUMERIA_SAN.MIGUEL_TRIPLE",
      "Available": 3
    },
    {
      "SKU": "PLUMERIA_SIAM.RUBY_DOUBLE",
      "Available": 9
    },
    {
      "SKU": "PLUMERIA_SIAM.RUBY_SINGLE",
      "Available": 8
    },
    {
      "SKU": "PLUMERIA_SLAUGHTER.PINK_SINGLE",
      "Available": 8
    },
    {
      "SKU": "PLUMERIA_TILLIES.HUGHES_DOUBLE",
      "Available": 4
    },
    {
      "SKU": "POT_AVON_GREY_6.5IN",
      "Available": 6
    },
    {
      "SKU": "POT_AZTECA_4IN",
      "Available": 1
    },
    {
      "SKU": "POT_CABA_PLANTER_9IN",
      "Available": 8
    },
    {
      "SKU": "POT_CYLINDER_GREEN_6IN",
      "Available": 5
    },
    {
      "SKU": "POT_CYLINDER_GREY_6IN",
      "Available": 1
    },
    {
      "SKU": "POT_CYLINDER_NAVY_6IN",
      "Available": 5
    },
    {
      "SKU": "POT_CYLINDER_ROUGH_6IN",
      "Available": 1
    },
    {
      "SKU": "POT_CYLINDER_RUST_6IN",
      "Available": 4
    },
    {
      "SKU": "POT_DELPHI_WHITE_6IN",
      "Available": 7
    },
    {
      "SKU": "POT_DELRAY_FOOTED_6IN",
      "Available": 7
    },
    {
      "SKU": "POT_EXPRESSIONS_FOOTED_6IN",
      "Available": 7
    },
    {
      "SKU": "POT_FEM.ROSA_6.5IN",
      "Available": 6
    },
    {
      "SKU": "POT_FREJA_5IN",
      "Available": 2
    },
    {
      "SKU": "POT_HANGING_WOOD.BRICK_12.5IN",
      "Available": 8
    },
    {
      "SKU": "POT_LIBERTY_BLACK_6IN",
      "Available": 9
    },
    {
      "SKU": "POT_LIBERTY_ORANGE_6IN",
      "Available": 4
    },
    {
      "SKU": "POT_LIBERTY_YELLOW_6IN",
      "Available": 7
    },
    {
      "SKU": "POT_LUNAREECE_TERRACOTTA",
      "Available": 1
    },
    {
      "SKU": "POT_MULTI.HOLE_TERRA_10IN",
      "Available": 7
    },
    {
      "SKU": "POT_PONCE_HANGING_7IN",
      "Available": 6
    },
    {
      "SKU": "POT_QUEEN.OPHELIA_WHITE_6IN",
      "Available": 1
    },
    {
      "SKU": "POT_ROSSI_13.5IN",
      "Available": 4
    },
    {
      "SKU": "POT_ROSSI_9IN",
      "Available": 4
    },
    {
      "SKU": "POT_SAO_NAVY_7IN",
      "Available": 9
    },
    {
      "SKU": "POT_STAND_TRIPLE_BLACK_34IN",
      "Available": 4
    },
    {
      "SKU": "POT_STD_TERRA.COTA_4IN",
      "Available": 7
    },
    {
      "SKU": "POT_STD_TERRA.COTA_6IN",
      "Available": 1
    },
    {
      "SKU": "POT_STD_TERRA.COTA_6IN",
      "Available": 1
    },
    {
      "SKU": "POT_STEPS_PINK_4IN",
      "Available": 5
    },
    {
      "SKU": "POT_STEPS_PINK_6IN",
      "Available": 2
    },
    {
      "SKU": "POT_STEPS_TERRA.COTTA_4IN",
      "Available": 4
    },
    {
      "SKU": "POT_STEPS_TERRA.COTTA_6IN",
      "Available": 2
    },
    {
      "SKU": "POT_STEPS_WHITE_4IN",
      "Available": 1
    },
    {
      "SKU": "POT_STEPS_WHITE_6IN",
      "Available": 2
    },
    {
      "SKU": "POT_TERRA.COTTA_SQUARE_4IN",
      "Available": 5
    }
   ]

new = []

for p in pl:
    n = ""
    sku = p["SKU"]
    s = sku.split("_")
    if(s[0].isnumeric()):
        s[0]+= '"'
        s[len(s)-1] = " ".join(s[len(s)-1].split("."))
        fin = " ".join(s).title()

        img = "1-"+s[1]+"-"+s[2]+"-"+s[0]+" MAIN.jpg"

        obj = {
            sku: {
                "name": fin,
                "image": img
            }
        }
        new.append(obj)
        print(obj)
 
    elif(isinstance(s[0], str)):
        break
    # print(new)

    f = open("newNames.js", "w")
    f.write(str(new))
    f.close()
