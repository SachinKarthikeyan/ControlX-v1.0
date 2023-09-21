import pygame
from pynput.mouse import Controller, Button
import pyautogui
import time

pygame.init()

loadingScreen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Loading...")

loadingScreen.fill((255, 255, 255))

# Update the custom font path to 'assets/Poppin.ttf'
customFont = pygame.font.Font('assets/Poppin.ttf', 36)

text = customFont.render("Loading...", True, (0, 0, 0))
textRect = text.get_rect(center=(200, 150))

loadingScreen.blit(text, textRect)
pygame.display.flip()

time.sleep(3)

pygame.display.quit()

mouse = Controller()

# Create a new screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("ControlX")

# Check for connected joysticks
numJoysticks = pygame.joystick.get_count()

if numJoysticks == 0:
    noJoystickFont = pygame.font.Font(None, 24)  # Adjusted font size
    noJoystickText = noJoystickFont.render("Sorry, there are no joysticks connected", True, (0, 0, 0))
    noJoystickRect = noJoystickText.get_rect(center=(200, 150))  # Adjusted position

    screen.fill((255, 255, 255))
    screen.blit(noJoystickText, noJoystickRect)

    pygame.display.flip()
    time.sleep(2)  # Display the message for 2 seconds

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    xMovement = 0
    yMovement = 0

    def performClick(buttonState, button):
        if buttonState:
            if button == "left":
                mouse.click(Button.left, 1)
            elif button == "right":
                mouse.click(Button.right, 1)

    print(f"Number of joysticks connected: {numJoysticks}")

    welcomeFont = pygame.font.Font(None, 36)
    welcomeText = welcomeFont.render("Welcome to ControlX", True, (0, 0, 0))
    welcomeRect = welcomeText.get_rect(center=(200, 100))

    screen.fill((255, 255, 255))
    screen.blit(welcomeText, welcomeRect)

    if numJoysticks == 1:
        joystickText = welcomeFont.render("1 joystick connected", True, (0, 0, 0))
    else:
        joystickText = welcomeFont.render(f"{numJoysticks} joysticks connected", True, (0, 0, 0))

    joystickRect = joystickText.get_rect(center=(200, 150))
    screen.blit(joystickText, joystickRect)

    optionFont = pygame.font.Font(None, 24)
    optionText = optionFont.render("Press 'P' to proceed or 'Q' to quit", True, (0, 0, 0))
    optionRect = optionText.get_rect(center=(200, 200))
    screen.blit(optionText, optionRect)

    pygame.display.flip()

    proceed = None
    while proceed is None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    proceed = True
                elif event.key == pygame.K_q:
                    proceed = False

    pygame.display.quit()

    if proceed:
        running = True
        while running:
            pygame.event.pump()

            joystickX = joystick.get_axis(0)
            joystickY = joystick.get_axis(1)

            if abs(joystickX) < 0.1:
                joystickX = 0
            if abs(joystickY) < 0.1:
                joystickY = 0

            xMovement = joystickX * 5
            yMovement = joystickY * 5
            mouse.move(xMovement, yMovement)

            aButtonState = joystick.get_button(0)
            bButtonState = joystick.get_button(1)
            if aButtonState:
                mouse.click(Button.left, 1)
            if bButtonState:
                mouse.click(Button.right, 1)

            hatX, hatY = joystick.get_hat(0)

            if hatY == 1:
                pyautogui.scroll(1)
            elif hatY == -1:
                pyautogui.scroll(-1)

            rightTrigger = joystick.get_axis(5)
            if rightTrigger > 0.9:
                running = False

pygame.quit()
