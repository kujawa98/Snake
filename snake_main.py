from snake import Snake
from setup import *
from drawer import draw_snake


def main():
    snk = Snake()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(25)
        snk.move()
        draw_snake(snk)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snk.head.direction != DIRECTIONS["down"]:
                        snk.change_direction(DIRECTIONS["up"])
                if event.key == pygame.K_DOWN:
                    if snk.head.direction != DIRECTIONS["up"]:
                        snk.change_direction(DIRECTIONS["down"])
                if event.key == pygame.K_LEFT:
                    if snk.head.direction != DIRECTIONS["right"]:
                        snk.change_direction(DIRECTIONS["left"])
                if event.key == pygame.K_RIGHT:
                    if snk.head.direction != DIRECTIONS["left"]:
                        snk.change_direction(DIRECTIONS["right"])
        pygame.display.update()


if __name__ == '__main__':
    main()
