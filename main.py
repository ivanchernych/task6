import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Character(pygame.sprite.Sprite):
    def __init__(self, image, coord, speed,  *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def walk(self, event):

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.rect.y -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.rect.y += self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed

    def update(self, *args):
        if args:
            self.walk(args[0])


def game(screen):
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    image = load_image("creature.png", -1)
    Character(image, (0, 0), 10, player_group, all_sprites)

    FPS = 60
    tick = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            all_sprites.update(event)
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    game(screen)
