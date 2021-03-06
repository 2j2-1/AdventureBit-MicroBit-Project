from microbit import *
import radio
from utilities import Communicator

class Enemy:
    def __init__(self):
        self.health = 10
        self.attack = 10
        # self.defence = 0.5
        # self.sp_defence = 0.5

    def take_damage(self, damage):
        self.health -= int(damage)
        return self.health

    def send_health(self):
        com.send_command("health", self.health)

    def displayHealth(self):
        lights = self.health * 10
        board = [["0" for x in range(5)] for y in range(5)]
        for i in range(5):
            if lights >= i * 20 + 20:
                board[i][0] = "9"
        return Image(':'.join([''.join(vals) for vals in board]))


def showPixels(mapping):
    grid = [["0"] * 5 for y in range(5)]
    for x, y in mapping:
        grid[x][y] = "9"
    return Image(':'.join([''.join(vals) for vals in grid]))

com = Communicator(42)
enemy = Enemy()
while 1:
    display.show(enemy.displayHealth())
    resp = com.wait_for_command()
    if resp["command"] == "attack":
        enemy.take_damage(resp["value"])
        enemy.send_health()
