import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    #第1引数：こうかとんrectまたは爆弾rect
    #第2引数：スクリーンrect

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1

    return yoko, tate


def main():
    bomb = 3
    count = 0
    price = False
    clock = pg.time.Clock()

    #練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()

    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    
    #練習３
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    #アイテムの仕様
    item_sfc = pg.image.load("fig/present.png")
    item_sfc = pg.transform.rotozoom(item_sfc, 0, 0.1)
    item_rct = item_sfc.get_rect()
    item_rct.centerx = random.randint(0, scrn_rct.width)
    item_rct.centery = random.randint(0, scrn_rct.width)
    scrn_sfc.blit(item_sfc, item_rct)


    #練習５
    bomb_rct_lst = []
    vx = []
    vy = []
    for i in range(bomb):
        bomb_sfc = pg.Surface((20, 20))
        bomb_sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
        bomb_rct_lst.append(bomb_sfc.get_rect())
        bomb_rct_lst[i].centerx = random.randint(0, scrn_rct.width)
        bomb_rct_lst[i].centery = random.randint(0, scrn_rct.height)
        scrn_sfc.blit(bomb_sfc, bomb_rct_lst[i])
        vx.append(random.randint(-1, 1)) 
        vy.append(random.randint(-1, 1))

    #練習2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #れんしゅう４
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1

        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1

        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1

            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        
        if count%2000 == 0:
            item_rct.centerx = random.randint(0, scrn_rct.width)
            item_rct.centery = random.randint(0, scrn_rct.width)

        if price == False:
            scrn_sfc.blit(tori_sfc, tori_rct)
            if count > 4000:
                scrn_sfc.blit(item_sfc, item_rct)
                if tori_rct.colliderect(item_rct):
                    timee = 0
                    price = True
                    tori_nsfc = pg.image.load("fig/6.png")
                    tori_nsfc = pg.transform.rotozoom(tori_nsfc, 0, 2.0)
                    #tori_rct = tori_sfc.get_rect()
                    #tori_rct.center = tori_rct.centerx, tori_rct.centery
                    scrn_sfc.blit(tori_nsfc, tori_rct)
        elif price:
            scrn_sfc.blit(tori_nsfc, tori_rct)
            item_rct.centerx = random.randint(0, scrn_rct.width)
            item_rct.centery = random.randint(0, scrn_rct.width)
        
        

        count += 1
        #練習６
        for i in range(bomb):
            if count%10000 == 0:
                if vx[i] < 0:
                    vx[i] -= 1
                
                else:
                    vx[i] += 1
                
                if vy[i] < 0:
                    vy[i] -= 1
                
                else:
                    vy[i] += 1

            bomb_rct_lst[i].move_ip(vx[i], vy[i])
            scrn_sfc.blit(bomb_sfc, bomb_rct_lst[i])
            yoko, tate =  check_bound(bomb_rct_lst[i], scrn_rct)
            vx[i] *= yoko
            vy[i] *= tate
        
        #練習８

        for bomb_rct in bomb_rct_lst:
            if tori_rct.colliderect(bomb_rct):
                if price:
                    scrn_sfc.blit(tori_sfc, tori_rct)
                    price = False
                    up = count
                
                elif count - up < 300:
                    pass
                
                else:
                    return
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()