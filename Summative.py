import os
import pygame.image
from pygame import *
import time
import random

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 50)

init()
screen = display.set_mode((1000, 700))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (220, 220, 220)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightBlue = (204, 255, 255)
darkBlue = (30, 144, 255)
treeGreen = (74, 153, 58)

running = True
startLoadingScreen = False
inMenu = True
collideMenuStart = False
collideMenuInstruction = False
collideMenuQuit = False
collideMenuSetting = False
collidePauseContinue = False
collidePauseInstruction = False
collidePauseSetting = False
collidePauseReturn = False
isPaused = False
pausedAnimation = False
gameMovepUp = False
gameMoveDown = False
gameMoveForward = False
gameMoveBack = False


pages = 0  # 0 For Menu, 1 for Game, 2 for Settings, 3 for Instructions
escapeReturn = 0

# Fonts
doto = "Fonts/Doto/Doto-VariableFont_ROND,wght.ttf"
pixelify = "Fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
franklin = "Fonts/Franklin_Gothic_Medium/OPTIFranklinGothic-Medium.otf"

menuTitleText = Rect(300, 165, 400, 70)
menuGameStart = Rect(300, 265, 400, 70)
menuSetting = Rect(300, 365, 400, 70)
menuInstruction = Rect(300, 465, 400, 70)
menuQuit = Rect(300, 565, 400, 70)
pauseMenu = Rect(350, 200, 300, 400)
pauseTitleText = Rect(350, 115, 300, 70)
pauseContinue = Rect(375, 215, 250, 70)
pauseInstruction = Rect(375, 315, 250, 70)
pauseSetting = Rect(375, 415, 250, 70)
pauseReturn = Rect(375, 515, 250, 70)
gameHealth = Rect(110, 20, 200, 20)
gameAmmo = Rect(110, 50, 200, 20)
gameHPText = Rect(15, 20, 40, 20)
gameAmmoText = Rect(15, 50, 40, 20)
gameWaveText = Rect(15, 80, 40, 20)
gameScoreText = Rect(110, 80, 40, 20)

pests = []
ammoFireing = []
gameLevel = 1
waves = 1
health = 100
maxHealth = 100
score = 0
ammo = 20
maxAmmo = 20
playerx,playery=100,350


movePlayerUp = "w"
movePlayerDown = "s"
movePlayerForward = "d"
movePlayerBack = "a"
keyUp = key.key_code(movePlayerUp)
keyDown = key.key_code(movePlayerDown)
keyForward = key.key_code(movePlayerForward)
keyBack = key.key_code(movePlayerBack)


# def drawPixelBorder(aRect, pixelSize=7, color=black):
#     x, y, w, h = aRect
#     pattern = [0, 1, 0, -1, 1, 0, -1, 0]
#     # Top border
#     for i in range(0, w, pixelSize):
#         # offset = random.randint(-jagAmount, jagAmount)
#         offset = pattern[(i // pixelSize) % len(pattern)]
#         draw.rect(screen, color, (x + i, y + offset, pixelSize, pixelSize))
#
#     # Bottom border
#     for i in range(0, w, pixelSize):
#         # offset = random.randint(-jagAmount, jagAmount)
#         offset = pattern[(i // pixelSize) % len(pattern)]
#         draw.rect(screen, color, (x + i, y + h - pixelSize + offset, pixelSize, pixelSize))
#
#     # Left border
#     for i in range(0, h, pixelSize):
#         # offset = random.randint(-jagAmount, jagAmount)
#         offset = pattern[(i // pixelSize) % len(pattern)]
#         draw.rect(screen, color, (x + offset, y + i, pixelSize, pixelSize))
#
#     # Right border
#     for i in range(0, h, pixelSize):
#         # offset = random.randint(-jagAmount, jagAmount)
#         offset = pattern[(i // pixelSize) % len(pattern)]
#         draw.rect(screen, color, (x + w - pixelSize + offset, y + i, pixelSize, pixelSize))

def drawBorderRect(aRectangle, aColorRect=white, aColorBorder=black, pixel=False, pixelSize=3):
    draw.rect(screen, aColorRect, aRectangle)
    if pixel:
        # drawPixelBorder(aRectangle,pixelSize,aColorBorder)
        pass
    else:
        draw.rect(screen, aColorBorder, aRectangle, 3)


# Fonts: Franklin Gothic Medium (franklin), Pixelify Sans (pixelify), Doto Thin (doto)
def textRender(aText, loc, aFontSize=20, aFontColor=black, fontType=pixelify, sizing=False):
    if not sizing:
        screen.blit(font.Font(fontType, aFontSize).render(aText, True, aFontColor), loc)
    else:
        return font.Font(fontType, aFontSize).render(aText, True, aFontColor).get_size()


def centerTextOnRect(aText, aRect, aFontSize=20, aFontColor=black, fontType=pixelify):
    txtRender = font.Font(fontType, aFontSize).render(aText, True, aFontColor)
    screen.blit(txtRender, txtRender.get_rect(center=aRect.center))


def drawTextAndRect(aText, aRect, aFontSize=20, aFontColor=black, fontType=pixelify, aColorRect=white,
                    aColorBorder=black, border=True):
    if border:
        drawBorderRect(aRect, aColorRect, aColorBorder)
    else:
        draw.rect(screen, aColorRect, aRect)
    centerTextOnRect(aText, aRect, aFontSize, aFontColor, fontType)


def LoadingScreenStart(isDisplayed):
    if not isDisplayed:
        textSizeX, textSizeY = textRender("Forest Invaders", (0, 0), aFontColor=white, aFontSize=60, sizing=True)
        screen.fill((0, 0, 0))
        textRender("Forest Invaders", (500 - textSizeX // 2, 350 - textSizeY // 2), aFontColor=white, aFontSize=60)
        display.update()
        time.sleep(2)
        for rgb in range(255):
            screen.fill((rgb, rgb, rgb))
            textRender("Forest Invaders", (500 - textSizeX // 2, 350 - textSizeY // 2), aFontColor=white, aFontSize=60)
            time.sleep(0.001)
            display.update()
        time.sleep(0.5)
    return True


def menu():
    global running
    global pages
    global escapeReturn
    escapeReturn = 0
    screen.fill(white)
    # drawBorderRect(menuGameStart)
    centerTextOnRect("Forest Invaders", menuTitleText, aFontSize=80, aFontColor=treeGreen)
    drawTextAndRect("Start!", menuGameStart, aFontSize=40, fontType=doto, aColorRect=treeGreen, aFontColor=white,
                    border=False)
    drawTextAndRect("Settings", menuSetting, aFontSize=40, fontType=doto, aColorRect=treeGreen,
                    aFontColor=white, border=False)
    drawTextAndRect("Instructions", menuInstruction, aFontSize=40, fontType=doto, aColorRect=treeGreen,
                    aFontColor=white, border=False)
    drawTextAndRect("Quit", menuQuit, aFontSize=40, fontType=doto, aColorRect=treeGreen, aFontColor=white, border=False)
    if collideMenuStart:
        draw.rect(screen, black, menuGameStart, 3)
    if collideMenuSetting:
        draw.rect(screen, black, menuSetting, 3)
    if collideMenuInstruction:
        draw.rect(screen, black, menuInstruction, 3)
    if collideMenuQuit:
        draw.rect(screen, black, menuQuit, 3)


# def drawAnimated(aPathName,loc,aScale=1):
#     for i in range(1,5):
#         img=pygame.image.load(aPathName+str(i)+".png").convert_alpha()
#         w,h=img.get_size()
#         img=transform.scale(img,(w*aScale,h*aScale))
#         screen.blit(img,loc)
#         display.update()
#         time.sleep(0.1)

def drawImg(aPathName,loc, aScale=1.0):
    img = pygame.image.load(aPathName).convert_alpha()
    w, h = img.get_size()
    img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale)))
    screen.blit(img, loc)

def load_animation_images(aPathName, aScale=1, frameCount=4):
    frames = []
    for i in range(1, frameCount + 1):
        img = pygame.image.load(aPathName + str(i) + ".png").convert_alpha()
        w, h = img.get_size()
        img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale)))
        frames.append(img)
    return frames


def drawAnimated(aPathName, loc, aScale=1.0, frameCount=4, frameDuration=150):
    frames = []
    for i in range(1, frameCount + 1):
        img = pygame.image.load(aPathName + str(i) + ".png").convert_alpha()
        w, h = img.get_size()
        img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale)))
        frames.append(img)
    now = pygame.time.get_ticks()
    frameIndex = (now // frameDuration) % len(frames)
    screen.blit(frames[frameIndex], loc)


def createEnemy():
    global pests
    x = 1000
    y = random.randint(100, 650)
    speed = waves * gameLevel * 0.2 + 2
    pests.append([x, y, speed])


def updateEnemy():
    global health
    global pests
    for i in pests:
        i[0] -= i[2]
        if i[0] < 0:
            pests.remove(i)
            health -= 10 * gameLevel


def isHit():
    global pests
    global score
    for i in ammoFireing:
        for enemy in pests:
            if Rect(i[0], i[1], 8, 8).colliderect((enemy[0], enemy[1], 16, 16)):
                ammoFireing.remove(i)
                pests.remove(enemy)
                score += 5
                break


def gameHUD():
    healthBar = int((health / maxHealth) * 200)
    ammoBar = int((ammo / maxAmmo) * 200)
    draw.rect(screen, black, gameHealth)
    draw.rect(screen, red, (gameHealth[0], gameHealth[1], healthBar, gameHealth[3]))
    draw.rect(screen, black, gameAmmo)
    draw.rect(screen, darkBlue, (gameAmmo[0], gameAmmo[1], ammoBar, gameAmmo[3]))
    if (health / maxHealth) <= 0.2:
        textRender("HP: " + str(health), gameHPText, aFontColor=red)
    else:
        textRender("HP: " + str(health), gameHPText, aFontColor=white)
    if (ammo / maxAmmo) <= 0.2:
        textRender("Ammo: " + str(ammo), gameAmmoText, aFontColor=red)
    else:
        textRender("Ammo: " + str(ammo), gameAmmoText, aFontColor=white)
    textRender("Wave: " + str(waves), gameWaveText, aFontColor=white)
    textRender("Score: " + str(score), gameScoreText, aFontColor=white)

def moveDrawCharacter():
    global playerx, playery
    if not isPaused:
        if gameMovepUp:
            playery-=2
            if playery<=100:
                playery=100
        if gameMoveDown:
            playery+=2
            if playery>=600:
                playery=600
        if gameMoveForward:
            playerx+=2
            if playerx>=200:
                playerx=200
        if gameMoveBack:
            playerx-=2
            if playerx<=10:
                playerx=10
        drawAnimated("Assets/Forest/Ranger_Idle_", (playerx, playery), 2.5)
    if isPaused:
        drawImg("Assets/Forest/Ranger_Idle_4.png", (playerx, playery), 2.5)
def game():
    global escapeReturn
    global playerx,playery
    escapeReturn = 0
    screen.fill(treeGreen)
    gameHUD()
    moveDrawCharacter()


def instructions():
    screen.fill(white)


def settings():
    screen.fill(black)


def paused():
    global escapeReturn
    global gameMovepUp,gameMoveDown,gameMoveForward,gameMoveBack
    gameMovepUp,gameMoveDown,gameMoveForward,gameMoveBack = False,False,False,False
    overlay = Surface((1000, 700), SRCALPHA)
    escapeReturn = 1
    # Dynamically Render the darkening, failed
    # if not pausedAnimation:
    #     for i in range(0,180):
    #         overlay.fill((0,0,0,i))
    #         screen.blit(overlay, (0, 0))
    #         display.update()
    #         time.sleep(0.1)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    draw.rect(screen, white, pauseMenu)
    centerTextOnRect("Paused", pauseTitleText, aFontSize=80, aFontColor=white)
    drawTextAndRect("Continue", pauseContinue, aFontSize=40, aFontColor=white, aColorRect=treeGreen, border=False)
    drawTextAndRect("Instructions", pauseInstruction, aFontSize=33, aFontColor=white, aColorRect=treeGreen,
                    border=False)
    drawTextAndRect("Settings", pauseSetting, aFontSize=40, aFontColor=white, aColorRect=treeGreen, border=False)
    drawTextAndRect("Return to Menu", pauseReturn, aFontSize=28, aFontColor=white, aColorRect=treeGreen, border=False)
    if collidePauseContinue:
        draw.rect(screen, black, pauseContinue, 3)
    if collidePauseInstruction:
        draw.rect(screen, black, pauseInstruction, 3)
    if collidePauseSetting:
        draw.rect(screen, black, pauseSetting, 3)
    if collidePauseReturn:
        draw.rect(screen, black, pauseReturn, 3)
    # display.update()
    # pausedAnimation = True


while running:
    startLoadingScreen = LoadingScreenStart(startLoadingScreen)
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN or e.type == MOUSEMOTION:
            if pages == 0:
                if menuGameStart.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:
                        collideMenuStart = True
                    else:
                        collideMenuStart = False
                        pages = 1
                elif menuSetting.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:
                        collideMenuSetting = True
                    else:
                        collideMenuSetting = False
                        pages = 2
                elif menuInstruction.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:
                        collideMenuInstruction = True
                    else:
                        collideMenuInstruction = False
                        pages = 3
                elif menuQuit.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:
                        collideMenuQuit = True
                    else:
                        collideMenuQuit = False
                        running = False
                else:
                    collideMenuStart = False
                    collideMenuSetting = False
                    collideMenuInstruction = False
                    collideMenuQuit = False
            if pages == 1:
                if isPaused:
                    if pauseContinue.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:
                            collidePauseContinue = True
                        else:
                            collidePauseContinue = False
                            isPaused = False
                    elif pauseSetting.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:
                            collidePauseSetting = True
                        else:
                            collidePauseSetting = False
                            pages = 2
                    elif pauseInstruction.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:
                            collidePauseInstruction = True
                        else:
                            collidePauseInstruction = False
                            pages = 3
                    elif pauseReturn.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:
                            collidePauseReturn = True
                        else:
                            collidePauseReturn = False
                            pages = 0
                            isPaused = False
                    else:
                        collidePauseContinue = False
                        collidePauseSetting = False
                        collidePauseInstruction = False
                        collidePauseReturn = False
        if e.type==KEYDOWN:
            if pages==1 and not isPaused:
                if e.key==keyUp:
                    gameMovepUp = True
                elif e.key==keyDown:
                    gameMoveDown = True
                if e.key==keyForward:
                    gameMoveForward = True
                elif e.key==keyBack:
                    gameMoveBack = True
        if e.type==KEYUP:
            if pages == 1 and not isPaused:
                if e.key==keyUp:
                    gameMovepUp = False
                if e.key==keyDown:
                    gameMoveDown = False
                if e.key ==keyForward:
                    gameMoveForward=False
                if e.key==keyBack:
                    gameMoveBack=False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and (pages == 2 or pages == 3):
                pages = escapeReturn
            elif e.key == K_ESCAPE and pages == 1:
                isPaused = not isPaused
    if pages == 0:
        menu()
    if pages == 1:
        game()
    if isPaused:
        paused()
    if pages == 2:
        settings()
        # pass  # placeholder
    if pages == 3:
        instructions()
        # pass  # placeholder
    display.update()
