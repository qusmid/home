class Tomato:

    states = {1: "Незрелое", 2: "Зрелое"}

    def __init__(self):
        _index = 0
        _state = Tomato.states[0]

    def grow(self):
        pass

    def is_ripe(self):
        pass


class TomatoBush:

    def __init__(self):
        tomatoes = []
