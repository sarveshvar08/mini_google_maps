def create_map():
    nodes = {
        "School": (70, 80),
        "Park": (230, 140),
        "Hall": (480, 60),
        "Library": (720, 130),

        "Home": (120, 300),
        "Office": (350, 230),
        "Mall": (540, 310),
        "Shop": (760, 260),

        "College": (300, 470),
        "Hospital": (600, 430),

        "Market": (200, 210),
        "Factory": (650, 330),
        "Stadium": (800, 90),
    }

    graph = {
        "School": [("Park", 3), ("Home", 6)],
        "Park": [("School", 3), ("Hall", 5), ("Market", 3), ("Office", 4)],
        "Hall": [("Park", 5), ("Library", 4), ("Factory", 6), ("Mall", 7)],
        "Library": [("Hall", 4), ("Shop", 5), ("Stadium", 3)],

        "Home": [("School", 6), ("Market", 2), ("Office", 3)],
        "Office": [("Home", 3), ("Park", 4), ("Factory", 3), ("College", 5)],
        "Mall": [("Hall", 7), ("Stadium", 3), ("Hospital", 4)],
        "Shop": [("Library", 5), ("Factory", 2)],

        "College": [("Office", 5), ("Hospital", 4), ("Market", 6)],
        "Hospital": [("College", 4), ("Factory", 5), ("Mall", 4)],

        "Market": [("Home", 2), ("Park", 3), ("College", 6)],
        "Factory": [("Office", 3), ("Shop", 2), ("Hospital", 5), ("Hall", 6)],
        "Stadium": [("Mall", 3), ("Library", 3)],
    }

    return nodes, graph