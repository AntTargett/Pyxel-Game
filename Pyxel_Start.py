import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 160, caption='Hello Pyxel')

        self.pyxel_y=0

        pyxel.image(0).load(0, 0, 'assets/Ant.jpeg')
        pyxel.sound(0).set(
            'e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr'
            'c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr', 'p', '6',
            'vffn fnff vffs vfnn', 25)

        pyxel.sound(1).set(
            'r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2'
            'f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ', 's', '6',
            'nnff vfff vvvv vfff svff vfff vvvv svnn', 25)

        pyxel.sound(2).set(
            'c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1'
            'a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1', 't', '7', 'n', 25)

        pyxel.sound(3).set(
            'f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1'
            'f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1', 't', '7', 'n', 25)

        pyxel.sound(4).set('f0ra4r f0ra4r f0ra4r f0f0a4r', 'n',
                           '6622 6622 6622 6422', 'f', 25)
        self.text="ImAnAnt Cool new game!"
        self.is_playing = [True] * 3

        self.play_music(True, True, True)

        pyxel.run(self.update, self.draw)


    def play_music(self, ch0, ch1, ch2):
        self.is_playing = (ch0, ch1, ch2)

        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)

        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.text = "Test Texg"
        if pyxel.btn(pyxel.KEY_LEFT):
            self.text = "ImAnAnt Cool new game!"
        if pyxel.btn(pyxel.KEY_UP):
            self.pyxel_y+=1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.pyxel_y-=1
        

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40, 41,  self.text, pyxel.frame_count % 16)
        pyxel.blt(61, self.pyxel_y, 0, 0, 0, 70, 70)


App()
