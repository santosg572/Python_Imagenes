#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pygame-2-ventana-e-imagenes/

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys
import numpy as np

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------

line_color = (255, 0, 0)

def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("fondo.png").convert()
    print(dir(fondo))
    print(type(fondo))
    dd = pygame.surfarray.array3d(fondo)
    print(type(dd))
    print(dd.shape)
    Z = 255*np.ones((640, 480,3))
    fondo = pygame.surfarray.make_surface(Z)
    tux = pygame.image.load("tux3.png").convert_alpha()

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    a = 250.
    b = 180.
    x0 = 300.
    y0 = 220.

    xx = []
    yy = []

    np1=38
    teta = np.linspace(0, 2*np.pi, np1)    # 38
    for te in teta:
      x = x0 + a*np.cos(te)
      y = y0 + b*np.sin(te)
      print(np.around((x,y),2))
      x2 = x
      if x2 < 320:
        x2 = x2+40
      y2 = y
      if y2 < 240:
        y2 = y2 + 32
      xx.append(x2)
      yy.append(y2)
      screen.blit(tux, (x, y))

    screen.blit(tux, (320-20, 240-16))
    np1 = np1-1
    print(np1)


   
    for i in np.arange(np1):
      x0 = xx[i]
      y0 = yy[i]
      for j in np.arange(i+1,np1):
        print((i,j))
        x2 = xx[j]
        pygame.draw.line(screen,line_color, (x0, y0), (x2, yy[j]))
    screen.blit(tux, (320-20, 240-16))
    pygame.display.flip()

    pygame.image.save(screen, 'clusterio.png') 
    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
if __name__ == "__main__":
    main()

