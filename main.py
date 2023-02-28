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


class Mountain(pygame.sprite.Sprite):
    def __init__(self, all_sprites, image):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    def __init__(self, pos, all_sprites, mountain, image):
        super().__init__(all_sprites)
        self.mountain = mountain
        self.image = image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, self.mountain):
            self.rect = self.rect.move(0, 1)


def game(screen):
    all_sprites = pygame.sprite.Group()
    image_p = load_image("pt.png")
    image_m = load_image("mountains.png")
    mountain = Mountain(all_sprites, image_m)

    FPS = 60
    tick = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos, all_sprites, mountain, image_p)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    game(screen)
