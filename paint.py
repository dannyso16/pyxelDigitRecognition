""" HOW TO PLAY
- you can draw a line with hold MOUSE_LEFT_BUTTON
- [delete]: clear the canvas and reset prediction
- [s]: save canvas and predict a digit which you draw

"""


# 3rd party
import numpy as np
from PIL import Image
import pyxel

# my library
import model

# constants
WINDOW_SIZE = 64


# ===== main =====
class App:

    # 0: white, -1: black
    windowData = [[0]*WINDOW_SIZE for _ in range(WINDOW_SIZE)]
    pred_digit = None

    def __init__(self):
        pyxel.init(WINDOW_SIZE, WINDOW_SIZE)
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btn(pyxel.KEY_DELETE):
            self.pred_digit = None
            # Change each pixel's color to white
            for y in range(pyxel.height):
                for x in range(pyxel.width):
                    self.windowData[y][x] = 0

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, hold=2, period=1):
            # Draw a line
            # This change pixel's colors like a star(*)
            # (the center is (mouse_x,mouse_y))
            x, y = pyxel.mouse_x, pyxel.mouse_y
            dx = [-3,-2,-1, 0, 0, 0,0,0,0,0,1,2,3,-1,-1,1,1,-2,-2,2,2]
            dy = [ 0, 0, 0,-3,-2,-1,0,1,2,3,0,0,0,-1,1,-1,1,2,-2,2,-2]
            for i in range(len(dx)):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < pyxel.width and 0 <= ny < pyxel.height:
                    self.windowData[ny][nx] = -1

        if pyxel.btn(pyxel.KEY_S):
            # save image and recognize the digit
            self._saveImage()
            self.pred_digit = model.load_predict()


    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        # show window
        for y in range(pyxel.height):
            for x in range(pyxel.width):
                if self.windowData[y][x]==-1:
                    pyxel.pix(x, y, pyxel.COLOR_BLACK)

        pyxel.text(0, 0, 'PREDICT: {}'.format(self.pred_digit), pyxel.COLOR_RED)


    def _saveImage(self):
        """ save 64x64 window's image into 8x8 picture
        The file name is 'screen_shot.png'
        """
        img = Image.new('RGB', (pyxel.width, pyxel.height))
        for y in range(pyxel.height):
            for x in range(pyxel.width):
                if self.windowData[y][x]==0:
                    img.putpixel((x,y), (255,255,255))
                else:
                    img.putpixel((x,y), (0,0,0))
        img = img.resize((8, 8), Image.BICUBIC)
        img.save("images/screen_shot.png")
        print("Image has saved correctly.")


App()
