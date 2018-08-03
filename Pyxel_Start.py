import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 160, caption='Hello Pyxel')
        pyxel.image(0).load(0, 0, 'assets/Ant.jpeg')
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40, 41, 'ImAnAnt Cool new game!', pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 70, 70)


App()
