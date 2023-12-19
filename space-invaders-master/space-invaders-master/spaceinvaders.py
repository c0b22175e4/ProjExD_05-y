from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/fonts/'
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

# Colors (R, G, B)
WHITE = (255, 255, 255)

SCREEN = display.set_mode((800, 600))
IMG_NAMES = ['enemy1_1', 'enemy1_2', 'enemy2_1', 'enemy2_2', 'enemy3_1', 'enemy3_2'] #tekiNo.
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha() #teki png. 
          for name in IMG_NAMES}

ENEMY_DEFAULT_POSITION = 65  # Initial value for a new game
ENEMY_MOVE_DOWN = 35

class Enemy(sprite.Sprite): #tekiclass
    def __init__(self, row, column):
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    def toggle_image(self): #kurikaesi
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def load_images(self): #tekishuturyoku
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  }
        img1, img2 = (IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row])
        self.images.append(transform.scale(img1, (40, 35)))
        self.images.append(transform.scale(img2, (40, 35)))

class EnemiesGroup(sprite.Group): #tekigroup
    def __init__(self, columns, rows):
        sprite.Group.__init__(self)
        self.enemies = [[None] * columns for _ in range(rows)]
        self.columns = columns
        self.rows = rows
        self.moveTime = 600
        self.direction = 1
        self.rightMoves = 30
        self.leftMoves = 30
        self.moveNumber = 15
        self.timer = time.get_ticks()
        self.bottom = ENEMY_DEFAULT_POSITION + ((rows - 1) * 45) + 35

    def update(self, current_time): 
        if current_time - self.timer > self.moveTime:
            if self.direction == 1:
                max_move = self.rightMoves
            else:
                max_move = self.leftMoves

            if self.moveNumber >= max_move:
                self.direction *= -1
                self.moveNumber = 0
                self.bottom = 0
                for enemy in self:
                    enemy.rect.y += ENEMY_MOVE_DOWN
                    enemy.toggle_image()
                    if self.bottom < enemy.rect.y + 35:
                        self.bottom = enemy.rect.y + 35
            else:
                velocity = 10 if self.direction == 1 else -10
                for enemy in self:
                    enemy.rect.x += velocity
                    enemy.toggle_image()
                self.moveNumber += 1

            self.timer += self.moveTime

    def add_internal(self, *sprites):
        super(EnemiesGroup, self).add_internal(*sprites)
        for s in sprites:
            self.enemies[s.row][s.column] = s

    def remove_internal(self, *sprites):
        super(EnemiesGroup, self).remove_internal(*sprites)
        for s in sprites:
            self.kill(s)

    def kill(self, enemy):
        self.enemies[enemy.row][enemy.column] = None

def main():
    init()
    mixer.pre_init(44100, -16, 1, 4096)
    mixer.init()
    clock = time.Clock()

    game = SpaceInvaders()
    game.reset(0)

    while True:
        for e in event.get():
            if e.type == QUIT:
                sys.exit()

        current_time = time.get_ticks()
        game.screen.blit(game.background, (0, 0))
        game.enemies.update(current_time)
        game.allSprites.update(current_time)
        game.allSprites.draw(game.screen)

        display.update()
        clock.tick(60)

class SpaceInvaders(object): #tekimatome
    def __init__(self):
        self.screen = SCREEN
        self.background = image.load(IMAGE_PATH + 'background.jpg').convert() #haikei
        self.enemies = EnemiesGroup(10, 5)
        self.allSprites = sprite.Group()
        self.make_enemies()
        self.timer = time.get_ticks()

    def reset(self, score):
        self.enemies.empty()
        self.make_enemies()
        self.allSprites.empty()
        self.allSprites.add(self.enemies)
        self.score = score

    def make_enemies(self): 
        for row in range(5):
            for column in range(10):
                enemy = Enemy(row, column)
                enemy.rect.x = 157 + (column * 50)
                enemy.rect.y = ENEMY_DEFAULT_POSITION + (row * 45)
                self.enemies.add(enemy)

if __name__ == '__main__':
    main()
