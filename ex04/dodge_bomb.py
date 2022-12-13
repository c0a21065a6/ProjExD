import pygame as pg
import sys

def main():
    #練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    #練習2
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()