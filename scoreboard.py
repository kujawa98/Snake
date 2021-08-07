import pygame


class Scoreboard:
    def __init__(self):
        self.best = self.read_score()
        self.current = 0
        self.font = pygame.font.SysFont(None, 23)

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

    def draw(self, window):
        txt = self.font.render("Current score - " + str(self.current), False, (0, 0, 0))
        txt2 = self.font.render("Best score - " + str(self.best), False, (0, 0, 0))
        window.blit(txt, (100, 697))
        window.blit(txt2, (400, 697))
