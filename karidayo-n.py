import sys
import pygame as pg
import random


WIDTH, HEIGHT = 800, 600

def main():
    # ウィンドウの初期化
    pg.display.set_caption("Kokaton Invader")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex05/images/background.png")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            # 画面の描画
            screen.blit(bg_img, [0, 0])

            pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()