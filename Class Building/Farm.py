import Building


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, type_crop):
        self.type_crop = type_crop
        super.__init__()
