import pygame
from point import *
from renderer import *
from boxcollider import *
from physics import *
from enemy import *

class PlayerBullet:
    def __init__(self):
        self.position = Point()
        self.renderer = loadSpriteRenderer("resources/player-bullet.png")
        self.box_collider = BoxCollider(self.position, 9, 20)
        self.active = True

    def run(self):
        self.position.add_up(0, -10)

        target = physics.check_contact(self.box_collider)
        if target is not None and type(target) is Enemy:
            target.active = False