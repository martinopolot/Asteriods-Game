import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        self.shoot_timer = 0 # cooltimer starts at 0

        # automatically add to groups
        # if hasattr(Player, 'containers'):
        #     for group in Player.containers:
        #         group.add(self)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    #  shoot 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: # move the player forward
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt) # rotate to the left
        if keys[pygame.K_d]:
            self.rotate(dt) # rotate to the right
        if keys[pygame.K_SPACE]:
            self.shoot() # updated method to handle spacebar
    # shooting
    # def shoot(self):
    #     if self.shoot_timer > 0:
    #         return
    #     self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    #     shot = Shot(self.position.x, self.position.y)
    #     direction = pygame.Vector2(0, 1).rotate(self.rotation)
    #     velocity = direction * PLAYER_SHOOT_SPEED
    #     Shot(self.position.x, self.position.y, velocity)

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt