from dataclasses import dataclass
import random


@dataclass
class Target: 
    x = random.randrange(1, 9)
    y = random.randrange(1, 9)

    def generate_new_location(self):
        self.x = random.randrange(1, 9)
        self.y = random.randrange(1, 9)


def check_if_hit(tank, target, shot_distance):
    x_diff = abs(tank.x - target.x)
    y_diff = abs(tank.y - target.y)
    if x_diff + y_diff <= shot_distance:
        if tank.x == target.x and tank.y > target.y and tank.direction == 'DOWN':
            tank.points += 50
            return True
        elif tank.x == target.x and tank.y < target.y and tank.direction == 'UP':
            tank.points += 50
            return True
        elif tank.y == target.y and tank.x > target.x and tank.direction == 'RIGHT':
            tank.points += 50
            return True
        elif tank.y == target.y and tank.x < target.x and tank.direction == 'LEFT':
            tank.points += 50
            return True
    tank.points -= 50
    return False
