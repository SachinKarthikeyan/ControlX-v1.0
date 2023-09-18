import pygame
from pynput.mouse import Controller, Button
import pyautogui

pygame.init()

if pygame.joystick.get_count() == 0:
    print("Nope")
    pygame.quit()
    exit()
else:
    print("Yippe")

mouse = Controller()

joystick = pygame.joystick.Joystick(0)
joystick.init()

xMovement = 0;
yMovement = 0;

def performClick(buttonState):
    if buttonState:
        mouse.press(Button.left)
    else:
        mouse.release(Button.left)

running = True;

while running:
    pygame.event.pump()

    joystickX = joystick.get_axis(0)
    joystickY = joystick.get_axis(1)

    if abs(joystickX) < 0.1:
        joystickX = 0
    if abs(joystickY) < 0.1:
        joystickY = 0

    xMovement =  joystickX * 5 # Change the Multiplier value to achieve smoother X axis movement
    yMovement = joystickY * 5 # Change the Multiplier value to achieve smoother Y axis movement
    mouse.move(xMovement,yMovement)

    aButtonState = joystick.get_button(0)
    bButtonState = joystick.get_button(1)
    performClick(aButtonState)
    performClick(bButtonState)

    hatX, hatY = joystick.get_hat(0)

    if hatY == 1:
        pyautogui.scroll(1)
    elif hatY == -1:
        pyautogui.scroll(-1)

    rightTrigger = joystick.get_axis(5)
    if rightTrigger > 0.9:
       running = False


pygame.quit()





