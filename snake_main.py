from snake import Snake
from setup import *
from drawer import draw_snake
from collision_checker import *
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
    clock = pygame.time.Clock()
    while run and not check_collision(snk):
        clock.tick(10)
        if food_collision(snk, food):
            snk.append_part()
            food = generate_food(free_spots)
        snk.move()
        resolve_spots(snk, free_spots)
        draw_snake(snk, food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snk.direction != DIRECTIONS["down"]:
                        snk.change_direction(DIRECTIONS["up"])
                if event.key == pygame.K_DOWN:
                    if snk.direction != DIRECTIONS["up"]:
                        snk.change_direction(DIRECTIONS["down"])
                if event.key == pygame.K_LEFT:
                    if snk.direction != DIRECTIONS["right"]:
                        snk.change_direction(DIRECTIONS["left"])
                if event.key == pygame.K_RIGHT:
                    if snk.direction != DIRECTIONS["left"]:
                        snk.change_direction(DIRECTIONS["right"])
        pygame.display.update()


if __name__ == '__main__':
    main()
