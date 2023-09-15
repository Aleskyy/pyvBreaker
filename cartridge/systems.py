import time
from . import shared
from . import pimodules
import os

pyv = pimodules.pyved_engine
pyv.bootstrap_e()

__all__ = [
    'controls_sys',
    'physics_sys',
    'rendering_sys',
    'gamectrl_sys'
]

def controls_sys(entities, components):
    pg = pyv.pygame

    controllable_ent = pyv.find_by_components('controls')
    activekeys = pg.key.get_pressed()

    for ent in controllable_ent:
        ctrl = ent['controls']
        ctrl['left'] = activekeys[pg.K_LEFT]
        ctrl['right'] = activekeys[pg.K_RIGHT]
        if ctrl['right']:
            ent['speed'] = shared.PLAYER_SPEED

        if ctrl['left']:
            ent['speed'] = -shared.PLAYER_SPEED
            
            
def physics_sys(entities, components):
    true = True            

def rendering_sys(entities, components):
    """
    displays everything that can be rendered
    """
    scr = shared.screen

    scr.fill((0, 0, 0))
    pl_ent = pyv.find_by_archetype('player')[0]
    li_blocks = pyv.find_by_archetype('block')
    ball = pyv.find_by_archetype('ball')[0]

    pyv.draw_rect(scr, 'white', pl_ent['body'])
    pyv.draw_rect(scr, 'blue', ball['body'])
    for b in li_blocks:
        pyv.draw_rect(scr, 'purple', b['body'])
        
        
def gamectrl_sys(entities, components):
    pg = pyv.pygame
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
            pyv.vars.gameover = True