import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        

class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.price = False

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            
            if check_bound(self.rct, self.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]

        #self.blit(scr)


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.color = color
        self.rad = rad
        self.vxy = vxy
        self.sfc = pg.Surface((2 * rad, 2 * rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.sfc.blit(self.sfc, self.rct) 
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

class Item:
    def __init__(self, scr:Screen):
        self.sfc = pg.image.load("fig/present.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.width)
        scr.sfc.blit(self.sfc, self.rct)
    
    def check(self, scr:Screen, kkt:Bird, count):
        if count%2000 == 0: #無敵アイテムの位置を2000フレームごとに変更する
            self.rct.centerx = random.randint(0, scr.rct.width)
            self.rct.centery = random.randint(0, scr.rct.width)
            #print("a")

        if kkt.price == False: #無敵モードではない時の挙動
            scr.sfc.blit(kkt.sfc, kkt.rct)
            if count > 4000:
                scr.sfc.blit(self.sfc, self.rct)
                if kkt.rct.colliderect(self.rct):
                    timee = 0
                    kkt.price = True
                    kkt.nsfc = pg.image.load("fig/6.png")
                    kkt.nsfc = pg.transform.rotozoom(kkt.nsfc, 0, 2.0)
                    scr.sfc.blit(kkt.nsfc, kkt.rct)

        elif kkt.price: #無敵モードの時の挙動
            scr.sfc.blit(kkt.nsfc, kkt.rct)
            self.rct.centerx = random.randint(0, scr.rct.width)
            self.rct.centery = random.randint(0, scr.rct.width)

class finish:
    def __init__(self):
        self.val = False
    def check(self, kkt:Bird, bmd:Bomb, scr:Screen, count):
        if kkt.rct.colliderect(bmd.rct):
                if kkt.price: #爆弾に当たった時無敵モードだったら解除する
                    scr.sfc.blit(kkt.sfc, kkt.rct)
                    kkt.price = False
                    self.up = count
                    print(1)
                
                elif count - self.up < 100:
                    print(count - self.up)
                    pass
                
                else: #無敵じゃないときに爆弾に当たった場合
                    print("finish")
                    self.val = True

            
class Karashu:
    
        
        

        

        
def main():
    clock =pg.time.Clock()
    
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/3.png", 2.0, (900, 400))
    kkt.blit(scr)

    bkd_lst = []
    for i in range(5):
        bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
        bkd_lst.append(bkd)    
    bkd.update(scr)   
   
    
    check = 0
    item = Item(scr)
    fin = finish()
    while True:
        scr.blit() #pgbg_sfc, pgbg_rct

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        
        item.check(scr, kkt, check)
        
        check += 1
        

        for i in range(5):
            bkd_lst[i].update(scr)
            fin.check(kkt, bkd_lst[i], scr, check)
            if fin.val:
                return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()