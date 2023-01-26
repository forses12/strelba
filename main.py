import time

import pygame

import model
import view,control

while True:
    time.sleep(1/100)
    view.draw()
    control.pain()
    model.help_me()
