import unittest
from snake import Snake
from setup import *


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snk = Snake()

    def test_initial_points(self):
        self.assertEqual([self.snk.head.x, self.snk.head.y], [8, 8])
        self.assertEqual([self.snk.tail.x, self.snk.tail.y], [8, 11])

    def test_snake_movement_same_direction(self):
        self.snk.move()
        self.snk.move()
        self.assertEqual([self.snk.head.x, self.snk.head.y], [8, 7])
        self.assertEqual([self.snk.tail.x, self.snk.tail.y], [8, 10])

    def test_snake_move_other_direction(self):
        self.snk.change_direction(DIRECTIONS['right'])
        self.snk.move()
        self.assertEqual(len(self.snk.parts), 3)
        self.assertEqual([self.snk.head.x, self.snk.head.y], [8.5, 8])
        self.assertEqual([self.snk.parts[1].x, self.snk.parts[1].y], [8, 8])
        self.assertEqual([self.snk.tail.x, self.snk.tail.y], [8, 10.5])

    def test_snake_move_tail_collision(self):
        self.snk.change_direction(DIRECTIONS['right'])
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.assertEqual(len(self.snk.parts), 2)
        self.assertEqual([self.snk.head.x, self.snk.head.y], [11, 8])
        self.assertEqual([self.snk.tail.x, self.snk.tail.y], [8, 8])

    def test_snake_move_change_dir_twice(self):
        self.snk.change_direction(DIRECTIONS['right'])
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.move()
        self.snk.change_direction(DIRECTIONS['down'])
        self.snk.move()
        self.assertEqual(len(self.snk.parts), 3)
        self.assertEqual([self.snk.head.x, self.snk.head.y], [11, 8.5])
        self.assertEqual([self.snk.tail.x, self.snk.tail.y], [8.5, 8])

    def test_anchor_point_appending(self):
        self.snk.append_anchor_point()
        self.assertEqual(len(self.snk.parts), 3)


if __name__ == "__main__":
    unittest.main()
