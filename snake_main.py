from snake import Snake
from setup import *
from drawer import draw_snake


def main():
    snk = Snake()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(10)
        draw_snake(snk)
        snk.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snk.change_direction(DIRECTIONS["up"])
                if event.key == pygame.K_DOWN:
                    snk.change_direction(DIRECTIONS["down"])
                if event.key == pygame.K_LEFT:
                    snk.change_direction(DIRECTIONS["left"])
                if event.key == pygame.K_RIGHT:
                    snk.change_direction(DIRECTIONS["right"])
        pygame.display.update()


if __name__ == '__main__':
    main()
