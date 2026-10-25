class Checker:
    def __init__(self):
        self.over_limit_count = 1

    def check(self, value, limit):
        """Update the running count if value is over limit."""
        if value > limit:
            self.over_limit_count += 1

c = Checker()
c.check(120, 100)
c.check(87, 100)
print(c.over_limit_count)   # 1 - it actually changed, no return needed