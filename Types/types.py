class Time(int):
    def __init__(self, time) -> int:
        super().__init__()
        self.time = time
    
    async def return_time(self, time):
        if not isinstance(time, int):
            raise Exception("Time must be an int")
        if time > 1 or time < 48:
            raise Exception("Max time is 48h & min time is 1h")
        return time


class Prize(str):
    def __init__(self, prize) -> str:
        super().__init__()
        self.prize = prize
    
    async def return_prize(self, prize):
        if not isinstance(prize, str):
            raise Exception("Prize must be a str")
        if len(prize) > 1 or len(prize) < 100:
            raise Exception("Max prize len is 100 & min length is 1")
        return prize


class Winners(int):
    def __init__(self, winners) -> int:
        super().__init__()
        self.time = winners
    
    async def return_winners(self, winners):
        if not isinstance(winners, int):
            raise Exception("Winners must be an int")
        if winners > 1 or winners < 15:
            raise Exception("Max winners is 48h & min time is 1h")
        return winners
