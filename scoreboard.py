class Scoreboard:
    def __init__(self):
        self.best = self.read_score()
        self.current = 0

    def update_score(self):
        self.current += 1
        if self.best < self.current:
            self.best = self.current

    def save_score(self):
        with open('score.txt', 'w') as f:
            f.write(str(self.best))

    def read_score(self):
        try:
            with open('score.txt') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0
