import Building


class Reservoir(Building):
    isSupplied = None

    def __init__(self):
        self.isSupplied = False
        super.__init__()
