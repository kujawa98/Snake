from snake import Snake
from setup import *
from drawer import draw_snake
from collision_checker import check_collision
from food_generator import generate_food


def fspots(snk):
    free_spots = [[i, j, True] for i in range(BOARD_WIDTH) for j in range(BOARD_HEIGHT)]
    for part in snk.parts:
        free_spots[BOARD_WIDTH * part.x - 1 + part.y - 1][2] = False
    return free_spots


def resolve_spots(snk, free_spots):
    free_spots[BOARD_WIDTH * snk.head.x - 1 + snk.head.y - 1][2] = False
    free_spots[BOARD_WIDTH * snk.tail.x - 1 + snk.tail.y - 1][2] = True


def main():
    snk = Snake()
    run = True
    free_spots = fspots(snk)
    food = generate_food(free_spots)
    foods = True
    clock = pygame.time.Clock()
    while run and not check_collision(snk):
        clock.tick(15)
        if not foods:
            food = generate_food(free_spots)
            foods = False
        draw_snake(snk, food)
        snk.move()
        resolve_spots(snk, free_spots)
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
