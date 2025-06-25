import pygame
import sys

#ゲーム背景
class BG:
    def __init__(self, screen):
        self.screen = screen
        self.COLOR = (0,0,0)
    def draw(self):
        self.screen.fill(self.COLOR)

#メインオブジェクト
class App:
    #ウインドウ設定
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FRAMELATE = 60
    APP_CAPTION = "MyGame"
    
    def __init__(self):
        self.window_init()
        self.obj_init()

    #ウインドウ初期化
    def window_init(self):
        pygame.init()                                   #Pygame初期化
        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)     #ウインドウサイズ
        )
        pygame.display.set_caption(self.APP_CAPTION)    #ウインドウの説明
        self.clock = pygame.time.Clock()                #クロック処理オブジェクト
    #オブジェクトのインスタンス初期化
    def obj_init(self):
        self.bg = BG(self.screen)
    
    #ロジック処理
    def update(self):
        pass

    #描画処理
    def draw(self):
        self.bg.draw()
        pygame.display.update()
    #確実な終了処理
    def quit(self):
        pygame.quit()               # Pygameの終了(画面閉じられる)
        sys.exit()                  # スクリプト全体の終了
    #ウインドウの✗ボタン終了処理
    def checkExit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 閉じるボタンが押されたら終了
                self.quit()
    #メインループ処理
    def loop(self):
        while True:
            self.clock.tick(self.FRAMELATE)
            self.checkExit()
            self.update()
            self.draw()

if __name__ == "__main__":
    app = App()
    app.loop()