# Forest Invaders
# Summative ICS3U, Mr.Rranza
# Austin Xiong

import os
import pygame.image
from pygame import *
import time
import random
import math

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 50)

# Initializations
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
lightGreen = (186, 252, 191)

# Debugging Purposes
cheatMode = False
topScoresReset = False  # For resetting purposes during testing

# Initialize Boolean Variables
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
collideSettingEasy = False
collideSettingNorm = False
collideSettingHard = False
collideSettingInstructionReturn = False
collideSettingUp = False
collideSettingDown = False
collideSettingForward = False
collideSettingBackward = False
collideSettingShoot = False
clickSettingUp = False
clickSettingDown = False
clickSettingForward = False
clickSettingBackward = False
clickSettingShoot = False
isPaused = False
pausedAnimation = False
gameMoveUp = False
gameMoveDown = False
gameMoveForward = False
gameMoveBack = False
gameShoot = False
firstSeedBag = False
gameOverStatus = False

# Define Pages
pages = 0  # 0 For Menu, 1 for Game, 2 for Settings, 3 for Instructions
escapeReturn = 0

# Fonts
doto = "Fonts/Doto/Doto-VariableFont_ROND,wght.ttf"
pixelify = "Fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
franklin = "Fonts/Franklin_Gothic_Medium/OPTIFranklinGothic-Medium.otf"

# Define all the Rect
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
settingTitleText = Rect(300, 50, 400, 70)
settingLevelText = Rect(50, 150, 100, 50)
settingLevelEasy = Rect(650, 150, 100, 50)
settingLevelNorm = Rect(750, 150, 100, 50)
settingLevelHard = Rect(850, 150, 100, 50)
settingInstructionReturnButton = Rect(50, 60, 150, 60)
settingKeyBindText = Rect(300, 225, 400, 70)
settingKeyUpText = Rect(50, 325, 100, 50)
settingKeyDownText = Rect(50, 400, 100, 50)
settingKeyForwardText = Rect(50, 475, 100, 50)
settingKeyBackwardText = Rect(50, 550, 100, 50)
settingKeyShootText = Rect(50, 625, 100, 50)
settingKeyUp = Rect(650, 325, 300, 50)
settingKeyDown = Rect(650, 400, 300, 50)
settingKeyForward = Rect(650, 475, 300, 50)
settingKeyBackward = Rect(650, 550, 300, 50)
settingKeyShoot = Rect(650, 625, 300, 50)

# Initialization of Game Parameters
pests = []
ammoFiring = []
seedBag = []
# gameLevel = 1
waves = 1
health = 100
maxHealth = 100
score = 0
ammo = 20
maxAmmo = 20
playerx, playery = 100, 350
playerSpeed = 0
listOfRandomEnemy = ["Assets/Forest/Bear_Walk_", "Assets/Forest/GnollBrute_Walk_", "Assets/Forest/NormalMushroom_Walk_",
                     "Assets/Forest/Wolf_Walk_", "Assets/Forest/Ent_Walk_"]
listOfTreeBush = ["Assets/Lost Pixel Art - Forest/Trees/TreeResize_1 - ",
                  "Assets/Lost Pixel Art - Forest/Trees/TreeResize_2 - ",
                  "Assets/Lost Pixel Art - Forest/Bushes/BushResize - "]
treeBushPos = []

enemySpawnedWave = 0
topScore = None

# Instructions Text
instructionsText1 = ("So, Forest Protector, welcome to your forest, you will be protecting this forest and shooting "
                     "off invasive enemies.")
instructionsText2 = ("Press KEYBINDUP to move up, Press KEYBINDDOWN to move down, Press KEYBINDFORWARD to move "
                     "forward, Press KEYBINDBACK to move back, Press KEYBINDSHOOT to shoot, Press ESC to pause and "
                     "return.")
instructionsText3 = ("Change Keybinds and difficulty at the SETTINGS Option and start the game in START! You can "
                     "return to this instruction page by pressing INSTRUCTION.")
instructionsText4 = ("The enemies will get faster as you progress through the game. Shoot or collect SEEDBAGS to gain "
                     "health and ammo for your forest. Killing enemies will also have a chance of dropping ammo. GOOD"
                     " LUCK!!")
instructionList1 = list(instructionsText1.split())
instructionList2 = list(instructionsText2.split())
instructionList3 = list(instructionsText3.split())
instructionList4 = list(instructionsText4.split())

# For Debugging Purpose
if cheatMode:
    health = 10000
    maxHealth = 10000
    ammo = 2000
    maxAmmo = 2000

# movePlayerUp = "w"
# movePlayerDown = "s"
# movePlayerForward = "d"
# movePlayerBackward = "a"
# playerShoot = " "

# Reads the difficulty stored
difficultyRead = open("Data/difficulty.txt", "r")
gameLevel = float(difficultyRead.readline())
difficultyRead.close()

# Reads the key binds stored
keyBindRead = open("Data/keyBind.txt", "r")
listOfKeys = list(keyBindRead.readline().split(","))
keyBindRead.close()
# print(listOfKeys)\

# Set the key binds
movePlayerUp = listOfKeys[0]
movePlayerDown = listOfKeys[1]
movePlayerForward = listOfKeys[2]
movePlayerBackward = listOfKeys[3]
playerShoot = listOfKeys[4]

keyUp = key.key_code(movePlayerUp)
keyDown = key.key_code(movePlayerDown)
keyForward = key.key_code(movePlayerForward)
keyBackward = key.key_code(movePlayerBackward)
keyShoot = key.key_code(playerShoot)


# Failed Attempted of Drawing Pixelated Borders
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

# Function that helps to reset the topscore after playing, for debugging purpose
def resetTop():
    scoreData = open("Data/highScores.txt", "w")
    scoreData.write(str(0))
    scoreData.close()


# Small function that can help to draw a rectangle with border
def drawBorderRect(aRectangle, aColorRect=white, aColorBorder=black, pixel=False, pixelSize=3):
    draw.rect(screen, aColorRect, aRectangle)
    if pixel:
        # drawPixelBorder(aRectangle,pixelSize,aColorBorder)
        pass
    else:
        draw.rect(screen, aColorBorder, aRectangle, 3)


# Fonts: Franklin Gothic Medium (franklin), Pixelify Sans (pixelify), Doto Thin (doto)
# Small Function that helps to render text
def textRender(aText, loc, aFontSize=20, aFontColor=black, fontType=pixelify, sizing=False):
    if not sizing:
        screen.blit(font.Font(fontType, aFontSize).render(aText, True, aFontColor), loc)
    else:
        return font.Font(fontType, aFontSize).render(aText, True, aFontColor).get_size()


# Small Function that centers text on to a Rect
def centerTextOnRect(aText, aRect, aFontSize=20, aFontColor=black, fontType=pixelify):
    txtRender = font.Font(fontType, aFontSize).render(aText, True, aFontColor)
    screen.blit(txtRender, txtRender.get_rect(center=aRect.center))


# Small Function that helps to draw Text and Rect and center the text on the rect
def drawTextAndRect(aText, aRect, aFontSize=20, aFontColor=black, fontType=pixelify, aColorRect=white,
                    aColorBorder=black, border=True):
    if border:
        drawBorderRect(aRect, aColorRect, aColorBorder)
    else:
        draw.rect(screen, aColorRect, aRect)
    centerTextOnRect(aText, aRect, aFontSize, aFontColor, fontType)


# Function that automatically switch line for text exceeding limits
def switchLine(aList, maxLength, maxHeight, pos, aFontSize=20, aFontColor=black, fontType=pixelify):
    posx = pos[0]
    posy = pos[1]
    spaceSize = font.Font(fontType, aFontSize).render(" ", True, aFontColor).get_size()[0]
    for word in aList:
        wordWidth, wordHeight = font.Font(fontType, aFontSize).render(word, True, aFontColor).get_size()
        # print(posx,wordWidth)
        if wordWidth + posx >= maxLength:
            posx = pos[0]
            posy += wordHeight
        textRender(word, (posx, posy), aFontSize, aFontColor, fontType)
        posx += wordWidth
        posx += spaceSize


# A function that initializes game parameters, useful for restarts
def gameInit():
    global pests, ammoFiring, gameLevel, waves, health, maxHealth, score, ammo, maxAmmo, playerx, playery, enemySpawnedWave, seedBag
    global isPaused, gameMoveUp, gameMoveDown, gameMoveForward, gameMoveBack, gameShoot, firstSeedBag, gameOverStatus, playerSpeed
    global treeBushPos
    # Game Parameters
    pests = []
    ammoFiring = []
    seedBag = []
    waves = 1
    health = 100
    maxHealth = 100
    score = 0
    ammo = 20
    maxAmmo = 20
    playerx, playery = 100, 350
    playerSpeed = 0
    enemySpawnedWave = 0
    treeBushPos = []

    # Game related boolean
    isPaused = False
    gameMoveUp = False
    gameMoveDown = False
    gameMoveForward = False
    gameMoveBack = False
    gameShoot = False
    firstSeedBag = False
    gameOverStatus = False

    # For debugging
    if cheatMode:
        health = 10000
        maxHealth = 10000
        ammo = 2000
        maxAmmo = 2000

    # Spawn random trees and bushes
    for i in range(random.randint(3, 6)):
        treePOS = noCollision(100, 500, 0, treeBush=True, xa=290, xb=800)
        if treePOS != False:
            treeBushPos.append([treePOS[0], treePOS[1], random.choice(listOfTreeBush)])
    # print(treeBushPos)


# This draws the loading screen animation when entering the game
def LoadingScreenStart(isDisplayed):
    if not isDisplayed:
        textSizeX, textSizeY = textRender("Forest Invaders", (0, 0), aFontColor=white, aFontSize=60, sizing=True)
        screen.fill((0, 0, 0))
        textRender("Forest Invaders", (500 - textSizeX // 2, 350 - textSizeY // 2), aFontColor=white, aFontSize=60)
        display.update()
        time.sleep(2)
        for rgb in range(255):
            screen.fill((rgb, rgb, rgb))  # This makes it dynamically change the brightness
            textRender("Forest Invaders", (500 - textSizeX // 2, 350 - textSizeY // 2), aFontColor=white, aFontSize=60)
            time.sleep(0.001)
            display.update()
        time.sleep(0.5)
    return True


# This functions draws the menu screen
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

    # If mouse hovers, draw a border
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

# Small Function that directly draws Image on to the screen
def drawImg(aPathName, loc, aScale=1.0, reflect=False):
    img = pygame.image.load(aPathName).convert_alpha()
    w, h = img.get_size()
    img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale)))
    if reflect:
        img = transform.flip(img, True, False).convert_alpha()
    screen.blit(img.convert_alpha(), loc)


# Already merged into drawAnimated()
# def load_animation_images(aPathName, aScale=1, frameCount=4):
#     frames = []
#     for i in range(1, frameCount + 1):
#         img = pygame.image.load(aPathName + str(i) + ".png").convert_alpha()
#         w, h = img.get_size()
#         img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale))).convert_alpha()
#         frames.append(img)
#     return frames

# Creates animation for the images, display every image for a 150ms and then change, loop through and it will be
# animated
def drawAnimated(aPathName, loc, aScale=1.0, frameCount=4, frameDuration=150, reflect=False):
    frames = []
    for i in range(1, frameCount + 1):
        img = pygame.image.load(aPathName + str(i) + ".png").convert_alpha()
        w, h = img.get_size()
        img = pygame.transform.scale(img, (int(w * aScale), int(h * aScale)))
        if reflect:  # If the image needs to be reflected
            img = transform.flip(img, True, False).convert_alpha()
        frames.append(img)
    now = pygame.time.get_ticks()
    frameIndex = (now // frameDuration) % len(frames)
    screen.blit(frames[frameIndex].convert_alpha(), loc)  # Draw the corresponding image according to ticks


# This creates the enemy
def createEnemy():
    global enemySpawnedWave
    global pests
    global waves
    x = 1000
    # y = random.randint(120, 600)
    y = noCollision(120, 600, 0)
    # Pest Speed is depended on the difficulty
    if gameLevel == 2.0:
        maxSpeed = 4
    elif gameLevel == 1.0:
        maxSpeed = 3
    elif gameLevel == 0.5:
        maxSpeed = 2
    else:
        maxSpeed = 3
    if y != False:  # Spawn the enemy into the list pests
        speed = min(int(waves * gameLevel * 0.2 + 1), maxSpeed)
        enemyNamePath = random.choice(listOfRandomEnemy)
        reflect = True
        pests.append([x, y, speed, enemyNamePath, reflect])
        enemySpawnedWave += 1
        if enemySpawnedWave == 10 * math.ceil(waves / 5):
            waves += 1
            enemySpawnedWave = 0


# Returns a y or x/y coordinate that is made sure it wouldn't collide/overlap with other objects spawning
def noCollision(a, b, layer, treeBush=False, xa=0, xb=0):
    out = random.randint(a, b)
    if layer == 10:
        return False
    if treeBush:  # For trees and Bushes
        outx = random.randint(xa, xb)
        for i in treeBushPos:
            # outx=(random.randint(xa,xb))
            # if abs(i[0]-outx) <= 300 and abs(i[1]-out) <= 150:
            # print(i[0],i[1],outx,out)
            if Rect(i[0], i[1], 100, 100).colliderect(Rect(outx, out, 100, 100)):
                return noCollision(a, b, layer + 1, treeBush=treeBush, xa=xa, xb=xb)
        return [outx, out]
    else:  # For the enemies
        for i in pests:
            # if (i[1] <= out <= i[1]+64 or out<=i[1]<=out+64) and 1000-i[0]<128:
            if abs(i[1] - out) <= 64 and 1000 - i[0] < 128:
                return noCollision(a, b, layer + 1)
        for i in seedBag:
            if abs(i[1] - out) <= 64 and 1000 - i[0] < 128:
                return noCollision(a, b, layer + 1)
        return out


# Add the trees and bushes for the first time
for i in range(random.randint(3, 6)):
    treePOS = noCollision(100, 500, 0, treeBush=True, xa=290, xb=800)
    if treePOS != False:
        treeBushPos.append([treePOS[0], treePOS[1], random.choice(listOfTreeBush)])


# This functions draws trees and bushes on to the screen.
def drawTreeBush():
    for i in treeBushPos:
        if not isPaused:
            drawAnimated(i[2], (i[0], i[1]), aScale=2)
        else:  # If paused, don't draw animations
            drawImg(str(i[2]) + "4.png", (i[0], i[1]), aScale=2)


# This updates the enemy position and draw them on the screen.
def updateEnemy():
    global health
    global pests
    isHit()
    for i in pests:
        if not isPaused:
            i[0] -= i[2]
            if i[0] < 0:  # If the enemy reaches the border
                pests.remove(i)
                health -= 5 * gameLevel
                if health <= 0:  # If the player is dead
                    return True
            drawAnimated(i[3], (i[0], i[1]), aScale=2, reflect=i[4])
            # draw.rect(screen,black,(i[0],i[1],3,3))
        else:  # If paused, don't draw animations
            drawImg(i[3] + "4.png", (i[0], i[1]), aScale=2, reflect=i[4])
    return False


# Function to check if enemies are hit, if so, delete them and add scores.
def isHit():
    global pests
    global score
    global ammo
    for i in ammoFiring:
        for enemy in pests:
            if Rect(i[0], i[1], 16, 16).colliderect((enemy[0], enemy[1], 64, 64)):
                ammoFiring.remove(i)
                pests.remove(enemy)
                score += 5
                chance = random.random()
                if chance >= 0.7:  # 30% chance to gain more ammo
                    ammo += min(5, maxAmmo - ammo)
                break


# Shoot bullets and draw them
def shoot():
    global ammo
    if gameShoot and ammo > 0:
        ammoFiring.append([playerx + 55, playery + 50])
        ammo -= 1
    # for i in range(len(ammoFiring)):
    #     if not isPaused:
    #         ammoFiring[i][0] += 5
    #         drawAnimated("Assets/Bullet/Bullet_", (ammoFiring[i][0], ammoFiring[i][1]))
    #     if isPaused:
    #         drawImg("Assets/Bullet/Bullet_1.png", (ammoFiring[i][0], ammoFiring[i][1]))
    for bullet in ammoFiring:
        if not isPaused:
            bullet[0] += 5
            drawAnimated("Assets/Bullet/Bullet_", (bullet[0], bullet[1]))
        if isPaused:
            drawImg("Assets/Bullet/Bullet_1.png", (bullet[0], bullet[1]))
        if bullet[0] >= 1000:
            ammoFiring.remove(bullet)


# Define and draw a seedBAG, where it would add health, ammo and speed to the player
def seedBagBuff():
    global firstSeedBag, seedBag, score, ammo, maxAmmo, health, maxHealth, playerSpeed
    if not firstSeedBag and waves % 2 == 0:  # Only spawn under even number of waves
        x = 1000
        # y = random.randint(120, 600)
        y = noCollision(120, 600, 0)
        if gameLevel == 2.0:
            maxSpeed = 4
        elif gameLevel == 1.0:
            maxSpeed = 3
        elif gameLevel == 0.5:
            maxSpeed = 2
        else:
            maxSpeed = 3
        if y != False:
            speed = min(int(waves * gameLevel * 0.2 + 1), maxSpeed)
            enemyNamePath = "Assets/SeedBag/SeedBag32px_1.png"
            reflect = False
            seedBag.append([x, y, speed, enemyNamePath, reflect])
            firstSeedBag = True  # Prevent over spawning
    elif waves % 2 == 1:
        firstSeedBag = False  # Reset the over spawn boolean
    # Detect if a bullet hits the seedBAG, if so, add the health, ammo and speed
    for bag in seedBag:
        for i in ammoFiring:
            if Rect(i[0], i[1], 16, 16).colliderect((bag[0], bag[1], 32, 32)):
                ammoFiring.remove(i)
                seedBag.remove(bag)
                score += 10
                ammo += min(10 + 5 * int(waves / 5), 40)
                maxAmmo += min(10 + 5 * int(waves / 5), 40)
                health += min(20 + 5 * int(waves / 5), 50)
                maxHealth += min(20 + 5 * int(waves / 5), 50)
                playerSpeed += 1
                break
        # Detect if player himself hits the seedBAG, if so, add the health, ammo and speed
        if Rect(playerx, playery, 80, 80).colliderect((bag[0], bag[1], 32, 32)) and bag in seedBag:
            seedBag.remove(bag)
            score += 10
            ammo += min(10 + 5 * int(waves / 5), 40)
            maxAmmo += min(10 + 5 * int(waves / 5), 40)
            health += min(20 + 5 * int(waves / 5), 50)
            maxHealth += min(20 + 5 * int(waves / 5), 50)
            playerSpeed += 1
        if playerSpeed > 2:
            playerSpeed = 2  # Prevent player being too fast
        if not isPaused:
            bag[0] -= bag[2]
            if bag[0] < 0:
                seedBag.remove(bag)  # If reaches the end
        drawImg(bag[3], (bag[0], bag[1]), aScale=1, reflect=bag[4])


# Function that draws then HUD and HUD bars
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


# Function that helps to move the player and draw them
def moveDrawCharacter():
    global playerx, playery
    if not isPaused:
        if gameMoveUp:
            playery -= (2 + playerSpeed)
            if playery <= 100:
                playery = 100
        if gameMoveDown:
            playery += (2 + playerSpeed)
            if playery >= 600:
                playery = 600
        if gameMoveForward:
            playerx += (2 + playerSpeed)
            if playerx >= 200:
                playerx = 200
        if gameMoveBack:
            playerx -= (2 + playerSpeed)
            if playerx <= 10:
                playerx = 10
        drawAnimated("Assets/Forest/Ranger_Idle_", (playerx, playery), 2.5)
    if isPaused:  # If paused, don't draw animated
        drawImg("Assets/Forest/Ranger_Idle_4.png", (playerx, playery), 2.5)


# Function that reads the highest score
def readWriteTopScore():
    global topScore
    scoreData = open("Data/highScores.txt", "r")
    currentTop = scoreData.readline()
    scoreData.close()
    if score > int(currentTop):
        scoreData = open("Data/highScores.txt", "w")
        scoreData.write(str(score))
        scoreData.close()
        currentTop = score
    topScore = currentTop


# Main Game sequence, calls the previous game functions
def game():
    global pages
    global escapeReturn
    global playerx, playery
    global gameOverStatus, isPaused
    if initGameStart:
        gameInit()
    escapeReturn = 0
    screen.fill(treeGreen)
    drawImg("Assets/BackgroundSmall/BackgroundMoreGreenSmall.jpg", (0, 0))
    moveDrawCharacter()
    shoot()
    readWriteTopScore()
    # if len(pests) < 5 + int(min(math.floor(random.random()*waves*gameLevel),(10 * math.ceil(waves /
    # 5)-enemySpawnedWave)*0.7)):
    spawnRandomEnemy = random.randint(0, 10 * math.ceil(waves / 5) - enemySpawnedWave)
    if len(pests) < 3 + min(spawnRandomEnemy, 3):
        # if 10 * math.ceil(waves / 5)-enemySpawnedWave <= 3:
        #     createEnemy()
        #     if len(pests) <=3:
        #
        createEnemy()
    if updateEnemy():
        gameOverStatus = True
        isPaused = True
        # pages = 0  # temporary placeholder
    seedBagBuff()
    drawTreeBush()
    gameHUD()


# Draws the game over menu if the player dies
def gameOver():
    global gameMoveUp, gameMoveDown, gameMoveForward, gameMoveBack
    gameMoveUp, gameMoveDown, gameMoveForward, gameMoveBack = False, False, False, False
    overlay = Surface((1000, 700), SRCALPHA)  # Creates a new overlay so that it can darken the background
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    draw.rect(screen, white, pauseMenu)
    centerTextOnRect("Game Over", pauseTitleText, aFontSize=80, aFontColor=white)
    centerTextOnRect("Your Score", Rect(pauseContinue[0], pauseContinue[1], pauseContinue[2], pauseContinue[3] // 2),
                     aFontSize=30)
    centerTextOnRect(str(score), Rect(pauseContinue[0], pauseContinue[1] + pauseContinue[3] // 2, pauseContinue[2],
                                      pauseContinue[3] // 2),
                     aFontSize=30)
    centerTextOnRect("Top Score",
                     Rect(pauseInstruction[0], pauseInstruction[1], pauseInstruction[2], pauseInstruction[3] // 2),
                     aFontSize=30)
    centerTextOnRect(str(topScore),
                     Rect(pauseInstruction[0], pauseInstruction[1] + pauseInstruction[3] // 2, pauseInstruction[2],
                          pauseInstruction[3] // 2),
                     aFontSize=30)
    drawTextAndRect("Restart", pauseSetting, aFontSize=40, aFontColor=white, aColorRect=treeGreen, border=False)
    drawTextAndRect("Return to Menu", pauseReturn, aFontSize=28, aFontColor=white, aColorRect=treeGreen, border=False)
    if collidePauseSetting:
        draw.rect(screen, black, pauseSetting, 3)
    if collidePauseReturn:
        draw.rect(screen, black, pauseReturn, 3)


# This draws the instructions menu, is uses the switchLine function to automatically switch line
def instructions():
    screen.fill(white)
    # centerTextOnRect("This is Instructions Page (WIP)", Rect(0, 0, 1000, 700), aFontSize=60)
    centerTextOnRect("Instructions", settingTitleText, aFontSize=80)
    # print(list(instructionsText.split()))
    instructionList2[1] = movePlayerUp.upper()
    instructionList2[6] = movePlayerDown.upper()
    instructionList2[11] = movePlayerForward.upper()
    instructionList2[16] = movePlayerBackward.upper()
    instructionList2[21] = playerShoot.upper()
    switchLine(instructionList1, 950, 600, (50, 150), aFontSize=25)
    switchLine(instructionList2, 950, 600, (50, 230), aFontSize=25)
    switchLine(instructionList3, 950, 600, (50, 340), aFontSize=25)
    switchLine(instructionList4, 950, 600, (50, 450), aFontSize=25)
    settingInstructionReturn()


# Draws the Setting menu, a call of other functions
def settings():
    screen.fill(white)
    # centerTextOnRect("This is Settings Page (WIP)", Rect(0, 0, 1000, 700), aFontSize=60, aFontColor=white)
    centerTextOnRect("Settings", settingTitleText, aFontSize=80)
    settingInstructionReturn()
    settingLevel()
    settingKeyBind()


# Draws the return button in Settings and Instructions Page
def settingInstructionReturn():
    if collideSettingInstructionReturn:
        drawTextAndRect("Return", settingInstructionReturnButton, aFontSize=30, aColorRect=treeGreen, aFontColor=white,
                        border=True)
    else:
        drawTextAndRect("Return", settingInstructionReturnButton, aFontSize=30, aColorRect=treeGreen, aFontColor=white,
                        border=False)


# This draws and updates the difficulty option, it will be automatically updated to the difficulty.txt file
def settingLevel():
    textRender("Level", settingLevelText, aFontSize=30)
    drawTextAndRect("Easy", settingLevelEasy, aFontSize=25, aColorRect=treeGreen, border=False, aFontColor=white)
    drawTextAndRect("Normal", settingLevelNorm, aFontSize=25, aColorRect=treeGreen, border=False, aFontColor=white)
    drawTextAndRect("Hard", settingLevelHard, aFontSize=25, aColorRect=treeGreen, border=False, aFontColor=white)
    if gameLevel == 1.0:
        drawTextAndRect("Normal", settingLevelNorm, aFontSize=25, aColorRect=lightGreen, border=True, aFontColor=black)
    if gameLevel == 0.5:
        drawTextAndRect("Easy", settingLevelEasy, aFontSize=25, aColorRect=lightGreen, border=True, aFontColor=black)
    if gameLevel == 2.0:
        drawTextAndRect("Hard", settingLevelHard, aFontSize=25, aColorRect=lightGreen, border=True, aFontColor=black)
    draw.line(screen, black, (750, 150), (750, 199), width=2)
    draw.line(screen, black, (850, 150), (850, 199), width=2)
    if collideSettingEasy:
        draw.rect(screen, black, settingLevelEasy, 3)
    if collideSettingNorm:
        draw.rect(screen, black, settingLevelNorm, 3)
    if collideSettingHard:
        draw.rect(screen, black, settingLevelHard, 3)
    difficultyWrite = open("Data/difficulty.txt", "w")
    difficultyWrite.write(str(gameLevel))
    difficultyWrite.close()


# This draws and updates the key binds option, it will be automatically updated to the keyBind.txt file
def settingKeyBind():
    global keyUp, keyDown, keyForward, keyBackward, keyShoot
    centerTextOnRect("Key Binds", settingKeyBindText, aFontSize=60)
    textRender("Move Up", settingKeyUpText, aFontSize=25)
    textRender("Move Down", settingKeyDownText, aFontSize=25)
    textRender("Move Forward", settingKeyForwardText, aFontSize=25)
    textRender("Move Backward", settingKeyBackwardText, aFontSize=25)
    textRender("Shoot", settingKeyShootText, aFontSize=25)
    drawTextAndRect(movePlayerUp.upper(), settingKeyUp, aFontSize=20)
    drawTextAndRect(movePlayerDown.upper(), settingKeyDown, aFontSize=20)
    drawTextAndRect(movePlayerForward.upper(), settingKeyForward, aFontSize=20)
    drawTextAndRect(movePlayerBackward.upper(), settingKeyBackward, aFontSize=20)
    drawTextAndRect(playerShoot.upper(), settingKeyShoot, aFontSize=20)
    if clickSettingUp:
        drawTextAndRect(movePlayerUp.upper(), settingKeyUp, aFontSize=20, aColorRect=lightGreen)
    if clickSettingDown:
        drawTextAndRect(movePlayerDown.upper(), settingKeyDown, aFontSize=20, aColorRect=lightGreen)
    if clickSettingForward:
        drawTextAndRect(movePlayerForward.upper(), settingKeyForward, aFontSize=20, aColorRect=lightGreen)
    if clickSettingBackward:
        drawTextAndRect(movePlayerBackward.upper(), settingKeyBackward, aFontSize=20, aColorRect=lightGreen)
    if clickSettingShoot:
        drawTextAndRect(playerShoot.upper(), settingKeyShoot, aFontSize=20, aColorRect=lightGreen)

    keyUp = key.key_code(movePlayerUp)
    keyDown = key.key_code(movePlayerDown)
    keyForward = key.key_code(movePlayerForward)
    keyBackward = key.key_code(movePlayerBackward)
    keyShoot = key.key_code(playerShoot)
    keyBindWrite = open("Data/keyBind.txt", "w")
    keyBindWrite.write(",".join([movePlayerUp, movePlayerDown, movePlayerForward, movePlayerBackward, playerShoot]))
    keyBindWrite.close()


# Draw the dynamic pause menu
def paused():
    global escapeReturn
    global gameMoveUp, gameMoveDown, gameMoveForward, gameMoveBack
    gameMoveUp, gameMoveDown, gameMoveForward, gameMoveBack = False, False, False, False
    overlay = Surface((1000, 700), SRCALPHA)  # Creates a new overlay so that it can darken the background
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


# Main game function
while running:
    # Some necessary initializations per loop
    gameShoot = False
    initGameStart = False
    startLoadingScreen = LoadingScreenStart(startLoadingScreen)
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN or e.type == MOUSEMOTION:  # If mouse is pressed or moved
            if pages == 0:  # On Main Menu
                if menuGameStart.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideMenuStart = True
                    else:  # If pressed, enter the page
                        collideMenuStart = False
                        pages = 1
                        initGameStart = True
                elif menuSetting.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideMenuSetting = True
                    else:  # If pressed, enter the page
                        collideMenuSetting = False
                        pages = 2
                elif menuInstruction.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideMenuInstruction = True
                    else:  # If pressed, enter the page
                        collideMenuInstruction = False
                        pages = 3
                elif menuQuit.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideMenuQuit = True
                    else:  # If pressed, enter the page
                        collideMenuQuit = False
                        running = False
                else:
                    collideMenuStart = False
                    collideMenuSetting = False
                    collideMenuInstruction = False
                    collideMenuQuit = False
            if pages == 1:  # If in the main game
                if isPaused and not gameOverStatus:  # If paused and not game over, this will handle the paused menu
                    if pauseContinue.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseContinue = True
                        else:  # If pressed, enter the page
                            collidePauseContinue = False
                            isPaused = False
                    elif pauseSetting.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseSetting = True
                        else:  # If pressed, enter the page
                            collidePauseSetting = False
                            pages = 2
                    elif pauseInstruction.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseInstruction = True
                        else:  # If pressed, enter the page
                            collidePauseInstruction = False
                            pages = 3
                    elif pauseReturn.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseReturn = True
                        else:  # If pressed, enter the page
                            collidePauseReturn = False
                            pages = 0
                            isPaused = False
                    else:
                        collidePauseContinue = False
                        collidePauseSetting = False
                        collidePauseInstruction = False
                        collidePauseReturn = False
                elif gameOverStatus:  # If game is over
                    if pauseSetting.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseSetting = True
                        else:  # If pressed, restart the game
                            collidePauseSetting = False
                            initGameStart = True
                            gameOverStatus = False
                            isPaused = False
                    elif pauseReturn.collidepoint(e.pos):
                        if e.type == MOUSEMOTION:  # If moved, draw the border
                            collidePauseReturn = True
                        else:  # If pressed, enter the page
                            collidePauseReturn = False
                            pages = 0
                            isPaused = False
                            gameOverStatus = False
                    else:
                        collidePauseReturn = False
                        collidePauseSetting = False
            if pages == 2:  # If in the Settings Menu
                if settingLevelEasy.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideSettingEasy = True
                        collideSettingNorm = False
                        collideSettingHard = False
                    else:  # If pressed, Set the game level
                        collideSettingEasy = False
                        collideSettingNorm = False
                        collideSettingHard = False
                        gameLevel = 0.5
                elif settingLevelNorm.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideSettingNorm = True
                        collideSettingEasy = False
                        collideSettingHard = False
                    else:  # If pressed, Set the game level
                        collideSettingNorm = False
                        collideSettingEasy = False
                        collideSettingHard = False
                        gameLevel = 1.0
                elif settingLevelHard.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideSettingHard = True
                        collideSettingEasy = False
                        collideSettingNorm = False
                    else:  # If pressed, Set the game level
                        collideSettingHard = False
                        collideSettingEasy = False
                        collideSettingNorm = False
                        gameLevel = 2.0
                else:
                    collideSettingEasy = False
                    collideSettingNorm = False
                    collideSettingHard = False
                if settingKeyUp.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # Does nothing, this variable is not used anymore
                        collideSettingUp = True
                    else:  # If pressed, prepare for inputs
                        clickSettingUp = True
                        collideSettingUp = False
                elif settingKeyDown.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # Does nothing, this variable is not used anymore
                        collideSettingDown = True
                    else:  # If pressed, prepare for inputs
                        clickSettingDown = True
                        collideSettingDown = False
                elif settingKeyForward.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # Does nothing, this variable is not used anymore
                        collideSettingForward = True
                    else:  # If pressed, prepare for inputs
                        clickSettingForward = True
                        collideSettingForward = False
                elif settingKeyBackward.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # Does nothing, this variable is not used anymore
                        collideSettingBackward = True
                    else:  # If pressed, prepare for inputs
                        clickSettingBackward = True
                        collideSettingBackward = False
                elif settingKeyShoot.collidepoint(e.pos):
                    if e.type == MOUSEMOTION:  # Does nothing, this variable is not used anymore
                        collideSettingShoot = True
                    else:  # If pressed, prepare for inputs
                        clickSettingShoot = True
                        collideSettingShoot = False
                else:
                    collideSettingUp = False
                    collideSettingDown = False
                    collideSettingForward = False
                    collideSettingBackward = False
                    collideSettingShoot = False
                    clickSettingUp = False
                    clickSettingDown = False
                    clickSettingForward = False
                    clickSettingBackward = False
                    clickSettingShoot = False

                if settingInstructionReturnButton.collidepoint(e.pos):  # The return button
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideSettingInstructionReturn = True
                    else:  # If pressed, Return to the original page
                        pages = escapeReturn
                        collideSettingInstructionReturn = False
                else:
                    collideSettingInstructionReturn = False
            if pages == 3:  # If in the instructions page
                if settingInstructionReturnButton.collidepoint(e.pos):  # The return button
                    if e.type == MOUSEMOTION:  # If moved, draw the border
                        collideSettingInstructionReturn = True
                    else:  # If pressed, Return to the original page
                        pages = escapeReturn
                        collideSettingInstructionReturn = False
                else:
                    collideSettingInstructionReturn = False
        if e.type == KEYDOWN:  # If key are pressed
            gameShoot = False  # Reset the shooting
            if pages == 1 and not isPaused:  # If in game and not paused
                if e.key == keyUp:  # Move Up
                    gameMoveUp = True
                elif e.key == keyDown:  # Move Down
                    gameMoveDown = True
                if e.key == keyForward:  # Move Right
                    gameMoveForward = True
                elif e.key == keyBackward:  # Move Left
                    gameMoveBack = True
                if e.key == keyShoot:  # Shoot
                    gameShoot = True
            if e.key == K_ESCAPE and (pages == 2 or pages == 3):  # If in settings or instructions page, return to
                # previous page
                pages = escapeReturn
            elif e.key == K_ESCAPE and pages == 1 and not gameOverStatus:  # If ESC is pressed, set isPaused to the
                # opposite value
                isPaused = not isPaused
            # Detect Special keys for key binds, only support SPACE and ENTER/RETURN
            if e.key == K_SPACE and pages == 2 and clickSettingShoot:
                playerShoot = "space"
                clickSettingShoot = False
            elif e.key == K_RETURN and pages == 2 and clickSettingShoot:
                playerShoot = "return"
                clickSettingShoot = False
            elif e.key == K_SPACE and pages == 2 and clickSettingUp:
                movePlayerUp = "space"
                clickSettingUp = False
            elif e.key == K_RETURN and pages == 2 and clickSettingUp:
                movePlayerUp = "return"
                clickSettingUp = False
            elif e.key == K_SPACE and pages == 2 and clickSettingDown:
                movePlayerDown = "space"
                clickSettingDown = False
            elif e.key == K_RETURN and pages == 2 and clickSettingDown:
                movePlayerDown = "return"
                clickSettingDown = False
            elif e.key == K_SPACE and pages == 2 and clickSettingForward:
                movePlayerForward = "space"
                clickSettingForward = False
            elif e.key == K_RETURN and pages == 2 and clickSettingForward:
                movePlayerForward = "return"
                clickSettingForward = False
            elif e.key == K_SPACE and pages == 2 and clickSettingBackward:
                movePlayerBackward = "space"
                clickSettingBackward = False
            elif e.key == K_RETURN and pages == 2 and clickSettingBackward:
                movePlayerBackward = "return"
                clickSettingBackward = False
            # For other keys, just set them directly
            elif clickSettingShoot:
                playerShoot = e.unicode
                clickSettingShoot = False
            elif clickSettingUp:
                movePlayerUp = e.unicode
                clickSettingUp = False
            elif clickSettingDown:
                movePlayerDown = e.unicode
                clickSettingDown = False
            elif clickSettingForward:
                movePlayerForward = e.unicode
                clickSettingForward = False
            elif clickSettingBackward:
                movePlayerBackward = e.unicode
                clickSettingBackward = False
        if e.type == KEYUP:  # If key is up, stop moving
            gameShoot = False
            if pages == 1 and not isPaused:
                if e.key == keyUp:
                    gameMoveUp = False
                if e.key == keyDown:
                    gameMoveDown = False
                if e.key == keyForward:
                    gameMoveForward = False
                if e.key == keyBackward:
                    gameMoveBack = False

    # Draw different menus for different pages
    if pages == 0:
        menu()
    if pages == 1:
        game()
    if gameOverStatus:
        gameOver()
    if isPaused and not gameOverStatus:
        paused()
    if pages == 2:
        settings()
        # pass  # placeholder
    if pages == 3:
        instructions()
        # pass  # placeholder
    display.update()

# Debugging Purposes
if topScoresReset:
    resetTop()
