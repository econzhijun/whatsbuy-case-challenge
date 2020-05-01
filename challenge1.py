class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v: int) -> bool:
        if self.coins + v > self.capacity:
            return False
        else:
            return True

    def add(self, v: int) -> None:
        assert self.can_add(v), f"Cannot add {v} coins now"
        self.coins += v