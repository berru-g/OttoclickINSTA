#projet d automatisation de like sur insta pour projet pro
#    prochaine etape:
#1 - choisir le hastag à cibler
#2 - calculer le nombre de click ou scroll
import pyautogui as pt
import pyautogui
from time import sleep

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            #pt.Click()
            print("1")
            pyautogui.click()
         
        except:
            print("0")
            pyautogui.scroll(-1200)
#            pyautogui.press(RIGHT)
            sleep(0.4)
            return 0


if __name__ == '__main__':
    clicker = Clicker('likeinstaWHITE.png', speed=.001)
    sleep(1)
    #Pointsjoueur = Pointsjoueur + 1
    end = 0

    while True:
        if clicker.nav_to_image() == 0:
            end += 1

        # End the loop
        if end > 150:
            break
print("session terminee")
