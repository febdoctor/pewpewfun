""" Talk timer "timingo" PewPew application

Finish your talks on time with timingo for PewPew device.
"""

import pew

pew.init()
screen = pew.Pix()
background = pew.Pix.from_iter((
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
))

sesstime = 45
screen.blit(background)
while pew.keys():
    pass
while True:
    keys = pew.keys()
    if keys & pew.K_UP:
        sesstime+=5
    if keys & pew.K_DOWN and sesstime > 5:
        sesstime-=5
    if keys & pew.K_LEFT:
        sesstime+=1
    if keys & pew.K_RIGHT and sesstime > 2:
        sesstime-=1    
    if keys & pew.K_O:
        break
    txt = pew.Pix.from_text('%02d' % sesstime)
    screen.blit(txt, 0, 0)
    pew.show(screen)
    pew.tick(1/5)

while pew.keys():
    pass
print('NEXT')
secs = 0
rem = sesstime
screen.box(0)
clk = 8
steps = 8
ticks = 0
fg = 3
limits=[10, 5, 2, 1]
pressed = 0
while rem > 0:
    keys = pew.keys()
    if keys != pressed:
        if keys & pew.K_UP:
            rem+=1
        if keys & pew.K_DOWN and rem > 1:
            rem-=1
    pressed = keys
    m = 0
    for i in range(8):
        clr = min(max(0, secs - m), 7) // 2
        screen.pixel(i, 7, color = clr)
        m += steps
    ticks+=1
    if ticks == 4:
        secs += 1
        ticks = 0
    if secs >= 60:
        secs = 0
        rem -= 1
    for i, lim in enumerate(limits):
        if rem <= lim:
           fg = 3 - ticks % (i+1)
    txt = pew.Pix.from_text('%02d' % rem, color=fg)
    screen.blit(txt, 0, 0)
    pew.show(screen)
    pew.tick(1 / 4)

txt = pew.Pix.from_text('STOP')
while True:
    keys = pew.keys()
    for i in range(txt.width):
        screen.blit(txt, -i, 1)
        pew.show(screen)
        pew.tick(1 / 12)
