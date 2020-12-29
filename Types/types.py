class Time(int):
    def __init__(self, time) -> int:
        super().__init__()
        self.time = time


class Prize(str):
    def __init__(self, prize) -> str:
        super().__init__()
        self.prize = prize


class Winners(int):
    def __init__(self, winners) -> int:
        super().__init__()
        self.time = winners
