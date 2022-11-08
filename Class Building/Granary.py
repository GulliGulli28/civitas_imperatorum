import Building


class Granary(Building):
    stockMax = 2600
    stock = None

    def __init__(self):
        self.stockMax = 2600
        self.stock = 0
        super.__init__()
